from json import loads
from .schemas import EnvTypes
from dotenv import dotenv_values
from typing import Any, Optional, Type, List, Dict, Tuple, Iterator


class Environment:
    def __init__(self, env_path: str = '.env', env_types: Type[EnvTypes] = EnvTypes):
        """
        Parameters:
            env_path(str): Path to environment file.
            env_types(Type[EnvTypes]): An annotated class for environment variables.
        """
        self._env_types: Dict = env_types.__annotations__
        self._env_values: Dict = self._get_env_values(env_path=env_path)
        self._set_attributes()

    def _set_types(self, env_values: Dict) -> Dict:
        """
        Parameters:
            env_values(Dict): Values of environment variables.
        Returns:
            (Dict): Values of environment variables with the required data types.
        """
        for key, value in env_values.items():
            env_type = self._env_types.get(key.lower(), str)
            if issubclass(env_type, (List, Dict)):
                value = loads(value)
            elif issubclass(env_type, Tuple):
                value = value.lstrip('(').rstrip(')').split(',')
            elif issubclass(env_type, bool):
                value = value.lower() in ("yes", "true", "t", "1")
            env_values[key] = env_type(value)
        return env_values

    def _get_env_values(self, env_path: str) -> Dict:
        """
        Parameters:
            env_path(str): Path to environment file.
        Returns:
            (Dict): Values of environment variables.
        """
        env_values: Dict = dict(dotenv_values(dotenv_path=env_path))
        if self._env_types:
            env_values = self._set_types(env_values)
        return env_values

    def _set_attributes(self) -> None:
        """Adds environment variables to class attributes"""
        for key, values in self._env_values.items():
            object.__setattr__(self, key.lower(), values)

    def __getattribute__(self, key: str) -> Any:
        return object.__getattribute__(self, key.lower())

    def __setattr__(self, key: str, value: Any) -> None:
        object.__setattr__(self, key.lower(), value)

    def __getattr__(self, key: str) -> Optional[Any]:
        try:
            return object.__getattribute__(self, key.lower())
        except AttributeError:
            return None

    def __delattr__(self, key: str) -> None:
        object.__delattr__(self, key.lower())

    def __getitem__(self, key: str) -> Optional[Any]:
        return self.__getattr__(key=key)

    def __setitem__(self, key: str, value: Any) -> None:
        object.__setattr__(self, key.lower(), value)

    def __iter__(self) -> Iterator:
        return iter(self.__dict__.__iter__())

    def __repr__(self) -> str:
        return f'<{type(self).__module__}.{type(self).__qualname__}> object at {hex(id(self))}'

    def __str__(self) -> str:
        return str(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)

    def keys(self) -> List:
        return list(self.__dict__.keys())

    def values(self) -> List:
        return list(self.__dict__.values())

    def get(self, key: str, default: Optional[Any] = None) -> Optional[Any]:
        """
        Parameters:
            key(str): Key to get the value.
            default(Optional[Any]): Default value if not found.
        Returns:
            (Optional[Any]): Value.
        """
        value = self.__getattr__(key=key)
        return value if value else default

    @property
    def __version__(self) -> str:
        return '1.1.0'
