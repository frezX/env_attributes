from setuptools import setup
from env_attributes import env


NAME = 'env_attributes'
VERSION = env.__version__
README = 'README.md'
DESCRIPTION = 'Loads environment into class attributes'

LONG_DESCRIPTION = '\n'
with open(README, encoding='utf-8') as f:
    lines = f.readlines()
    lines[0] += f'\n_v{VERSION}_\n'
    LONG_DESCRIPTION += ''.join(lines)

AUTHOR = 'frezX'
EMAIL = 'fffrrreeezzz.xxx@gmail.com'
URL = 'https://github.com/frezX/env_attributes'
REQUIRES_PYTHON = '>=3.7.0'
PACKAGES = ['env_attributes']
REQUIRED = ['python-dotenv']
KEYWORDS = ['python', 'dotenv', 'python-dotenv', 'python_dotenv', 'env_attributes', 'attributes', 'env', 'environment']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    python_requires=REQUIRES_PYTHON,
    packages=PACKAGES,
    install_requires=REQUIRED,
    include_package_data=True,
    keywords=KEYWORDS,
    classifiers=[
        "Intended Audience :: Developers",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
