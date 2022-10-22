# EnvAttributes

### Loads environment into class attributes

## Install:
```bash
pip install env_attributes
```

## Example:

### Environment:
```dotenv
HOST=localhost
PORT=5050
```

### Usage:

#### Variant 1:

```python
from env_attributes import Environment

path_to_env = 'example/.env'
env = Environment(env_path=path_to_env)

print(env.host, env.port)
```
output:
```
localhost 5050
```

#### Variant 2:
Correct if the .env file is in the root directory

```python
from env_attributes import env

print(env.host, env.port)
```
output:
```
localhost 5050
```

### Additional usage:
```python
print(env.get('host'), env['port'])
```

#### Register is not important:
```python
print(env.get('HoSt'), env['PORT'])
```

#### You can work with the env object as with a dict:
```python
for key in env:
    value = env.get(key)
    print(key, value)
```
output:
```
host localhost
port 5050
```

#### You can output all environment variables:
```python
print(env)
```
output:
```json
{"host": "localhost", "port": "5050"}
```

#### You can also get all keys or values from env:
```python
print(env.keys())
print(env.values())
```
output:
```
['host', 'port']
['localhost', '5050']
```

#### You can get length of env:
```python
print(len(env))
```
output:
```
2
```

# NEW
#### Added ability to specify type annotations for environment variables

## Example:

### Environment:
```dotenv
BOOL=False
INT=123456789
FLOAT=3.14159265
STRING='Hello World!'
LIST='[123, 2.22, [1, 2, 3], {"key1": "val1", "key2": "val2"}]'
TUPLE='(1, 22, 333, 4444)'
DICT='{"key1": "val1", "key2": "val2", "key3": {"key3.1": 1, "key3.2": 2}}'
CUSTOM='1, 2, 3, 4, 5, 6, 7, 8, 9'
```

### Usage
```python
from env_attributes import Environment, EnvTypes


class EnvironmentTypes(EnvTypes):
    bool: bool
    int: int
    float: float
    string: str
    list: list
    tuple: tuple
    dict: dict

env = Environment(env_types=EnvironmentTypes)

print(env.bool, type(env.bool))
print(env.int, type(env.int))
print(env.float, type(env.float))
print(env.string, type(env.string))
print(env.list, type(env.list))
print(env.tuple, type(env.tuple))
print(env.dict, type(env.dict))
```
output:
```
False <class 'bool'>
123456789 <class 'int'>
3.14159265 <class 'float'>
Hello World! <class 'str'>
[123, 2.22, [1, 2, 3], {'key1': 'val1', 'key2': 'val2'}] <class 'list'>
('1', ' 22', ' 333', ' 4444') <class 'tuple'>
{'key1': 'val1', 'key2': 'val2', 'key3': {'key3.1': 1, 'key3.2': 2}} <class 'dict'>
```
