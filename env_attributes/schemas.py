class EnvTypes:
    """
    Use this class to specify type annotations for environment variables

    Example:
        [.env file]
            BOOL=False
            INT=123456789
            FLOAT=3.14159265
            STRING='Hello World!'
            LIST='[123, 2.22, [1, 2, 3], {"key1": "val1", "key2": "val2"}]'
            TUPLE='(1, 22, 333, 4444)'
            DICT='{"key1": "val1", "key2": "val2", "key3": {"key3.1": 1, "key3.2": 2}}'
            CUSTOM='1, 2, 3, 4, 5, 6, 7, 8, 999'

        [Usage in code]
            class EnvironmentTypes(EnvTypes):
                bool: bool
                int: int
                float: float
                string: str
                list: list
                tuple: tuple
                dict: dict
                custom: CustomType

            env = Environment(env_types=EnvironmentTypes)
    """
