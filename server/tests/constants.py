"""_summary_
This is the file in charge of storing the variable constants

Raises:
    ValueError: _description_
    KeyError: _description_
    KeyError: _description_
    RuntimeError: _description_

Returns:
    _type_: _description_
"""
import json
from os import getpid
from uuid import uuid4
from random import randint
from typing import Dict, Any
from string import ascii_letters, digits

import toml
import dotenv
from display_tty import IDISP


# Variable that will enable/disable the debug logging of the functions
DEBUG = False
DEBUG = True
IDISP.debug = DEBUG

IDISP.logger.name = "Constants_tests"

DB_PORT = 3307
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "terarea"

SERVER_HOST = "0.0.0.0"
QUERY_HOST = "http://127.0.0.1"
PORT = 6000

# For the client
QUERY_DELAY = 2

SUCCESS = 0
ERROR = 1

APP_NAME = "Area - Testing"


# Creating a string that is void of injection material
SAFE_STRING = ascii_letters+digits
SAFE_STRING_LENGTH = len(SAFE_STRING)


def get_cache_busting() -> str:
    """_summary_
        This function is in charge of generating a cache busting string.
        This is done in order to avoid creating already existing accounts

    Returns:
        str: _description_
    """
    cache: str = ""
    length: int = 20
    iterations: int = 0

    cache += "startCacheBusting"
    cache += str(getpid())
    cache += str(uuid4()).replace("-", "")
    while iterations < length:
        cache += SAFE_STRING[
            randint(
                0, SAFE_STRING_LENGTH - 1
            )
        ]
        iterations += 1
    cache += str(getpid())
    cache += "endCacheBusting"
    return cache


def _get_env_node(env: Dict[str, Any], key: str, default: str) -> Any:
    """_summary_
        Load the variable from the environement.
        Otherwise, use the default value provided.
    Args:
        key (_type_): _description_
        default (_type_): _description_

    Returns:
        Any: _description_
    """
    node = env.get(key)
    if node is None:
        return default
    return node


def _get_environement_variable(environement: dotenv, variable_name: str) -> str:
    """_summary_
        Get the content of an environement variable.

    Args:
        variable_name (str): _description_

    Returns:
        str: _description_: the value of that variable, otherwise an exception is raised.
    """
    data = environement.get(variable_name)
    if data is None:
        raise ValueError(
            f"Variable {variable_name} not found in the environement"
        )
    return data


def _get_toml_variable(toml_conf: dict, section: str, key: str, default=None) -> str:
    """
    Get the value of a configuration variable from the TOML file.

    Args:
        toml_conf (dict): The loaded TOML configuration as a dictionary.
        section (str): The section of the TOML file to search in.
        key (str): The key within the section to fetch.
        default: The default value to return if the key is not found. Defaults to None.

    Returns:
        str: The value of the configuration variable, or the default value if the key is not found.

    Raises:
        KeyError: If the section is not found in the TOML configuration.
    """
    try:
        keys = section.split('.')
        current_section = toml_conf

        for k in keys:
            if k in current_section:
                current_section = current_section[k]
            else:
                raise KeyError(
                    f"Section '{section}' not found in TOML configuration."
                )

        if key in current_section:
            return current_section[key]
        if default is None:
            msg = f"Key '{key}' not found in section '{section}' "
            msg += "of TOML configuration."
            raise KeyError(msg)
        return default

    except KeyError as err:
        IDISP.log_warning(f"{err}", "_get_toml_variable")
        return default


def _password_generator(length: int = 20, encapsulation_node: str = "password") -> str:
    """_summary_
        This is a function in charge of generating a password for on the fly accounts.

    Args:
        length (int, optional): _description_. Defaults to 20.

    Returns:
        str: _description_
    """
    password = ""

    password += str(encapsulation_node)
    password += "_"

    iterations = 0
    while iterations < length:
        password += SAFE_STRING[
            randint(
                0,
                SAFE_STRING_LENGTH - 1
            )
        ]
        iterations += 1
    password += "_"
    password += str(encapsulation_node)
    return password


def are_json_responses_identical(json_response1: Dict[str, Any], json_response2: Dict[str, Any], test_name: str = "are_json_responses_identical") -> bool:
    """_summary_
        This function is in charge of comparing two json responses to see if they are identical.

    Args:
        json_response1 (Dict[str,Any]): _description_: The first json response you wish to compare
        json_response2 (Dict[str,Any]): _description_: The json response that the first response will be compared against

    Returns:
        bool: _description_: Returns True if they are identical, False otherwise.
    """
    try:
        json_response1_str = json.dumps(json_response1)
    except TypeError:
        IDISP.log_warning(
            "Failed to convert json_response1 to json format", test_name
        )
        return False
    try:
        json_response2_str = json.dumps(json_response2)
    except TypeError:
        IDISP.log_warning(
            "Failed to convert json_response2 to json format", test_name
        )
        return False
    if json_response1_str == json_response2_str:
        return True
    msg = "The content of json_response1 is different from json_response2:\n"
    msg += f"- json_response1_str = {json_response1_str}\n"
    msg += f"- json_response2_str = {json_response2_str}\n"
    IDISP.log_warning(msg, test_name)
    return False


CACHE_BUSTER = get_cache_busting()
CACHE_BUSTER_ADMIN = f"admin_{get_cache_busting()}_admin"

TEST_ENV = ".env"
try:
    dotenv.load_dotenv(TEST_ENV)
    ENV = dict(dotenv.dotenv_values())

    DB_PORT = int(_get_env_node(ENV, "DB_PORT", DB_PORT))
    DB_HOST = _get_env_node(ENV, "DB_HOST", DB_HOST)
    DB_USER = _get_env_node(ENV, "DB_USER", DB_USER)
    DB_PASSWORD = _get_environement_variable(ENV, "DB_PASSWORD")
    DB_DATABASE = _get_env_node(ENV, "DB_DATABASE", DB_DATABASE)
    MINIO_HOST = _get_env_node(ENV, "MINIO_HOST", "minio")
    MINIO_PORT = int(_get_env_node(ENV, "MINIO_PORT", 9000))
    MINIO_ROOT_USER = _get_env_node(ENV, "MINIO_ROOT_USER", "root")
    MINIO_ROOT_PASSWORD = _get_environement_variable(
        ENV, "MINIO_ROOT_PASSWORD"
    )


except Exception as e:
    raise RuntimeError(
        f"Environement {TEST_ENV} failed to load, aborting"
    ) from e

TOML_CONF = toml.load("config.toml")

# |- Toml status codes
SUCCESS = int(_get_toml_variable(
    TOML_CONF, "Status_codes", "success", SUCCESS
))
ERROR = int(_get_toml_variable(TOML_CONF, "Status_codes", "error", ERROR))
# |- Toml test configuration
SERVER_HOST = str(_get_toml_variable(
    TOML_CONF, "Test.host", "server", SERVER_HOST
))
QUERY_HOST = str(_get_toml_variable(
    TOML_CONF, "Test.host", "client", QUERY_HOST
))
PORT = int(_get_toml_variable(
    TOML_CONF, "Test.host", "port", PORT
))

# Endpoints to test the server
PATH_GET_HOME = "/"
PATH_GET_API_HOME = "/api/v1/"
PATH_PUT_REGISTER = "/api/v1/register"
PATH_POST_LOGIN = "/api/v1/login"
PATH_PATCH_USER = "/api/v1/user"
PATH_PUT_USER = "/api/v1/user"
PATH_DELETE_USER = "/api/v1/user"
PATH_GET_USER = "/api/v1/user"
PATH_GET_USER_ID = "/api/v1/user_id"
PATH_POST_LOGOUT = "/api/v1/logout"

# Token key references
LAMBDA_USER_TOKEN_KEY: str = "lambda_user"
ADMIN_USER_TOKEN_KEY: str = "admin_user"
TOKEN_AUTH_ID_STR: str = "Authorization"
PRETTY_TOKEN_KEY: str = "token_header"
RAW_TOKEN_KEY: str = "token_key"

# User data (test input)
USER_DATA_EMAIL = f"some_email_{CACHE_BUSTER}@company.example"
USER_DATA_USERNAME = USER_DATA_EMAIL.split("@")[0]
USER_DATA_PASSWORD = _password_generator(
    length=20, encapsulation_node="some_user"
)
USER_DATA_METHOD = "local"
USER_DATA_FAVICON = "NULL"
USER_DATA_ADMIN = "0"
USER_DATA_TOKEN = f"some_token_{CACHE_BUSTER}_some_token"
USER_DATA_TOKEN_LIFESPAN = 3600  # seconds

# User data rebind
USER_DATA_EMAIL_REBIND = f"some_email_{CACHE_BUSTER}_rebind@company.example"
USER_DATA_USERNAME_REBIND = USER_DATA_EMAIL_REBIND.split("@")[0]
USER_DATA_PASSWORD_REBIND = _password_generator(
    length=20, encapsulation_node="some_user_rebind"
)

# User data patch
USER_DATA_EMAIL_PATCH = f"some_email_{CACHE_BUSTER}_patch@company.com"
USER_DATA_USERNAME_PATCH = USER_DATA_EMAIL_PATCH.split("@")[0]
USER_DATA_PASSWORD_PATCH = _password_generator(
    length=20, encapsulation_node="some_user_patch"
)

# Admin data (test input)
ADMIN_DATA_EMAIL = f"some_email_{CACHE_BUSTER_ADMIN}@company.example"
ADMIN_DATA_USERNAME = ADMIN_DATA_EMAIL.split("@")[0]
ADMIN_DATA_PASSWORD = _password_generator(
    length=20, encapsulation_node="some_admin"
)
ADMIN_DATA_METHOD = "local"
ADMIN_DATA_FAVICON = "NULL"
ADMIN_DATA_ADMIN = "1"
ADMIN_DATA_TOKEN = f"some_token_{CACHE_BUSTER_ADMIN}_some_token"
ADMIN_DATA_TOKEN_LIFESPAN = 3600  # seconds

# Admin data rebind
ADMIN_DATA_EMAIL_REBIND = f"some_email_{CACHE_BUSTER_ADMIN}_"
ADMIN_DATA_EMAIL_REBIND += "rebind@company.example"
ADMIN_DATA_USERNAME_REBIND = ADMIN_DATA_EMAIL_REBIND.split("@")[0]
ADMIN_DATA_PASSWORD_REBIND = _password_generator(
    length=20, encapsulation_node="some_admin_rebind"
)

# Admin data patch
ADMIN_DATA_EMAIL_PATCH = f"some_email_{CACHE_BUSTER_ADMIN}_patch@company.com"
ADMIN_DATA_USERNAME_PATCH = ADMIN_DATA_EMAIL_PATCH.split("@")[0]
ADMIN_DATA_PASSWORD_PATCH = _password_generator(
    length=20, encapsulation_node="some_admin_patch"
)

# User dictionnary keys
UNODE_EMAIL_KEY = "email"
UNODE_PASSWORD_KEY = "password"
UNODE_USERNAME_KEY = "username"
UNODE_METHOD_KEY = "method"
UNODE_FAVICON_KEY = "favicon"
UNODE_ADMIN_KEY = "admin"

# Sets of info per users
USER_NORMAL_MODE = "normal"
USER_PUT_MODE = "put"
USER_PATCH_MODE = "patch"

# Critical node (tracking)
RUNTIME_NODE_CRITICAL_KEY = "critical"

# Pre-built response bodies for certain endpoints
RESPONSE_GET_HOME_RESPONSE_NOT_LOGGED_IN = {
    'title': 'Home',
    'msg': 'Welcome to the control server.',
    'resp': '',
    'logged in': False
}
RESPONSE_GET_HOME_API_RESPONSE_NOT_LOGGED_IN = {
    'title': 'Home',
    'msg': 'Welcome to the control server.',
    'resp': '',
    'logged in': False
}
RESPONSE_POST_LOGIN = {
    'title': 'Login',
    'msg': 'Welcome {name}',
    'resp': 'success',
    'logged in': True,
    'token': ''
}
RESPONSE_POST_REGISTER = {
    'title': 'Register',
    "msg": "Account created successfully.",
    'resp': 'success',
    'logged in': True
}
RESPONSE_PUT_USER = {
    "title": "Put user",
    "msg": "The account information has been updated.",
    "resp": "success",
    "logged in": True
}
RESPONSE_PATCH_USER = {
    "title": "Patch user",
    "msg": "The account information has been updated.",
    "resp": "success",
    "logged in": True
}
RESPONSE_GET_USER = {
    "title": "Get user",
    "msg": "The user information has been retrieved.",
    "resp": "success",
    "logged in": True
}
RESPONSE_GET_USER_ID = {
    "title": "Get user id",
    "msg": "The user information has been retrieved.",
    "resp": 0,
    "logged in": True
}
RESPONSE_POST_LOGOUT = {
    "title": "Logout",
    "msg": "You have successfully logged out...",
    "resp": "success",
    "logged in": False
}
RESPONSE_DELETE_USER = {
    "title": "Delete user",
    "msg": "The account has successfully been deleted.",
    "resp": "success",
    "logged in": False
}
