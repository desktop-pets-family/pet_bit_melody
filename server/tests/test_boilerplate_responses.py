"""_summary_
    File in charge of testing the boilerplate Boilerplate non http class.
"""
import os
import sys

from fastapi import FastAPI
import constants as TCONST

sys.path.append(os.getcwd())

try:
    from src.lib.sql.sql_manager import SQL
    from src.lib.components.http_codes import HCI
    from src.lib.components import constants as CONST
    from src.lib.components.runtime_data import RuntimeData
    from src.lib.components.endpoints_routes import Endpoints
    from src.lib.boilerplates.non_web import BoilerplateNonHTTP
    from src.lib.boilerplates.responses import BoilerplateResponses
    from src.lib.components.password_handling import PasswordHandling
except ImportError as e:
    raise ImportError("Failed to import the src module") from e

ERROR = TCONST.ERROR
SUCCESS = TCONST.SUCCESS
DEBUG = TCONST.DEBUG


RDI = RuntimeData(TCONST.SERVER_HOST, TCONST.PORT, "Area", ERROR, SUCCESS)
RDI.app = FastAPI()
RDI.endpoints_initialised = Endpoints(
    runtime_data=RDI,
    success=SUCCESS,
    error=ERROR,
    debug=DEBUG
)
BRI = BoilerplateResponses(
    runtime_data=RDI,
    debug=DEBUG
)
RDI.boilerplate_responses_initialised = BRI
RDI.boilerplate_non_http_initialised = BoilerplateNonHTTP(
    runtime_data_initialised=RDI,
    success=SUCCESS,
    error=ERROR,
    debug=DEBUG
)

RDI.database_link = SQL(
    url=CONST.DB_HOST,
    port=CONST.DB_PORT,
    username=CONST.DB_USER,
    password=CONST.DB_PASSWORD,
    db_name=CONST.DB_DATABASE,
    debug=DEBUG
)

RDI.boilerplate_responses_initialised = BRI

PHI = PasswordHandling(
    error=ERROR,
    success=SUCCESS,
    debug=DEBUG
)


def _register_fake_user() -> None:
    """_summary_
        Function in charge of registering a fake user.
    """
    input_data = [
        TCONST.USER_DATA_USERNAME,
        TCONST.USER_DATA_EMAIL,
        PHI.hash_password(str(TCONST.USER_DATA_PASSWORD)),
        TCONST.USER_DATA_METHOD,
        TCONST.USER_DATA_FAVICON,
        TCONST.USER_DATA_ADMIN
    ]
    column_names = RDI.database_link.get_table_column_names(CONST.TAB_ACCOUNTS)
    column_names.pop(0)
    RDI.database_link.insert_or_update_data_into_table(
        table=CONST.TAB_ACCOUNTS,
        data=input_data,
        columns=column_names
    )


def _unregister_fake_user() -> None:
    """_summary_
        Function in charge of deregistering a fake user.
    """
    RDI.database_link.remove_data_from_table(
        table=CONST.TAB_ACCOUNTS,
        where=f"email='{TCONST.USER_DATA_EMAIL}'"
    )


def _sing_fake_user_in() -> None:
    """_summary_
        Function in charge of signing in a fake user.
    """
    _register_fake_user()
    user_id = RDI.database_link.get_data_from_table(
        table=CONST.TAB_ACCOUNTS,
        column="id",
        where=f"email='{TCONST.USER_DATA_EMAIL}'",
        beautify=False
    )
    table_columns = RDI.database_link.get_table_column_names(
        CONST.TAB_CONNECTIONS
    )
    table_columns.pop(0)
    input_data = [
        TCONST.USER_DATA_TOKEN,
        str(user_id[0][0]),
        RDI.database_link.datetime_to_string(
            RDI.boilerplate_non_http_initialised.set_lifespan(
                TCONST.USER_DATA_TOKEN_LIFESPAN
            )
        )
    ]
    RDI.database_link.insert_or_update_data_into_table(
        table=CONST.TAB_CONNECTIONS,
        data=input_data,
        columns=table_columns
    )


def _sign_fake_user_out() -> None:
    """_summary_
        Function in charge of signing out a fake user.
    """
    RDI.database_link.remove_data_from_table(
        table=CONST.TAB_CONNECTIONS,
        where=f"token='{TCONST.USER_DATA_TOKEN}'"
    )
    _unregister_fake_user()


def test_build_response_body_no_error() -> None:
    """_summary_
        Function in charge of testing the build response body function.
    """
    title = "Hello World"
    message = "Some hello world !"
    response = "hw"
    token = None
    error = False
    data = BRI.build_response_body(
        title=title,
        message=message,
        resp=response,
        token=token,
        error=error
    )
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = message
    resp[CONST.JSON_RESP] = response
    resp[CONST.JSON_LOGGED_IN] = False
    assert data == resp


def test_build_response_body_error() -> None:
    """_summary_
        Function in charge of testing the build response body function.
    """
    title = "Hello World"
    message = "Some hello world !"
    response = "hw"
    token = None
    error = True
    data = BRI.build_response_body(
        title=title,
        message=message,
        resp=response,
        token=token,
        error=error
    )
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = message
    resp[CONST.JSON_ERROR] = response
    resp[CONST.JSON_LOGGED_IN] = False
    assert data == resp


def test_build_response_body_no_error_logged_in() -> None:
    """_summary_
        Function in charge of testing the build response body function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    message = "Some hello world !"
    response = "hw"
    error = False
    data = BRI.build_response_body(
        title=title,
        message=message,
        resp=response,
        token=TCONST.USER_DATA_TOKEN,
        error=error
    )
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = message
    resp[CONST.JSON_RESP] = response
    resp[CONST.JSON_LOGGED_IN] = True
    _sign_fake_user_out()
    assert data == resp


def test_build_response_body_error_logged_in() -> None:
    """_summary_
        Function in charge of testing the build response body function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    message = "Some hello world !"
    response = "hw"
    error = True
    data = BRI.build_response_body(
        title=title,
        message=message,
        resp=response,
        token=TCONST.USER_DATA_TOKEN,
        error=error
    )
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = message
    resp[CONST.JSON_ERROR] = response
    resp[CONST.JSON_LOGGED_IN] = True
    _sign_fake_user_out()
    assert data == resp


def test_invalid_token() -> None:
    """_summary_
        Function in charge of testing the invalid token function.
    """
    title = "Hello World"
    data = BRI.invalid_token(title)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The token you entered is invalid."
    resp[CONST.JSON_ERROR] = "Invalid token"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.invalid_token(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_not_logged_in() -> None:
    """_summary_
        Function in charge of testing the not logged in function.
    """
    title = "Hello World"
    data = BRI.not_logged_in(title)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "You need to be logged in to be able to run this endpoint."
    resp[CONST.JSON_ERROR] = "User not logged in"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.unauthorized(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_login_failed() -> None:
    """_summary_
        Function in charge of testing the login failed function.
    """
    title = "Hello World"
    data = BRI.login_failed(title)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "Login failed, invalid credentials or username."
    resp[CONST.JSON_ERROR] = "Invalid credentials or username."
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.unauthorized(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_insuffisant_rights_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.insuffisant_rights(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "You do not have enough permissions to execute this endpoint."
    resp[CONST.JSON_ERROR] = "Insufficient rights for given account."
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.forbidden(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_insuffisant_rights_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.insuffisant_rights(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "You do not have enough permissions to execute this endpoint."
    resp[CONST.JSON_ERROR] = "Insufficient rights for given account."
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.forbidden(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_bad_request_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.bad_request(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The request was not formatted correctly."
    resp[CONST.JSON_ERROR] = "Bad request"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_bad_request_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.bad_request(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The request was not formatted correctly."
    resp[CONST.JSON_ERROR] = "Bad request"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_internal_server_error_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.internal_server_error(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The server has encountered an error."
    resp[CONST.JSON_ERROR] = "Internal server error"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.internal_server_error(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_internal_server_error_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.internal_server_error(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The server has encountered an error."
    resp[CONST.JSON_ERROR] = "Internal server error"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.internal_server_error(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_unauthorized_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.unauthorized(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "You do not have permission to run this endpoint."
    resp[CONST.JSON_ERROR] = "Access denied"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.unauthorized(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_unauthorized_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.unauthorized(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "You do not have permission to run this endpoint."
    resp[CONST.JSON_ERROR] = "Access denied"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.unauthorized(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_invalid_verification_code_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.invalid_verification_code(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The verification code you have entered is incorrect."
    resp[CONST.JSON_ERROR] = "Invalid verification code"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_invalid_verification_code_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.invalid_verification_code(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The verification code you have entered is incorrect."
    resp[CONST.JSON_ERROR] = "Invalid verification code"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_user_not_found_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.user_not_found(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The current user was not found."
    resp[CONST.JSON_ERROR] = "Not found"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.not_found(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_user_not_found_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.user_not_found(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The current user was not found."
    resp[CONST.JSON_ERROR] = "Not found"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.not_found(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_no_access_token_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.no_access_token(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "Access token not found."
    resp[CONST.JSON_ERROR] = "No access token"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_no_access_token_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.no_access_token(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "Access token not found."
    resp[CONST.JSON_ERROR] = "No access token"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_provider_not_found_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.provider_not_found(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The provider you are looking for was not found."
    resp[CONST.JSON_ERROR] = "Provider not found"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.not_found(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_provider_not_found_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.provider_not_found(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "The provider you are looking for was not found."
    resp[CONST.JSON_ERROR] = "Provider not found"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.not_found(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_provider_not_given_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.provider_not_given(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "You have not given a provider."
    resp[CONST.JSON_ERROR] = "Provider missing"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_provider_not_given_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.provider_not_given(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "You have not given a provider."
    resp[CONST.JSON_ERROR] = "Provider missing"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_missing_variable_in_body_invalid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    title = "Hello World"
    data = BRI.missing_variable_in_body(title, "not_a_token")
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "A variable is missing in the body of the request."
    resp[CONST.JSON_ERROR] = "Missing variable"
    resp[CONST.JSON_LOGGED_IN] = False
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body


def test_missing_variable_in_body_valid_token() -> None:
    """_summary_
        Function in charge of testing the insuffisant rights function.
    """
    _sing_fake_user_in()
    title = "Hello World"
    data = BRI.missing_variable_in_body(title, TCONST.USER_DATA_TOKEN)
    resp = {}
    resp[CONST.JSON_TITLE] = title
    resp[CONST.JSON_MESSAGE] = "A variable is missing in the body of the request."
    resp[CONST.JSON_ERROR] = "Missing variable"
    resp[CONST.JSON_LOGGED_IN] = True
    compiled_response = HCI.bad_request(
        content=resp,
        content_type=CONST.CONTENT_TYPE,
        headers=RDI.json_header
    )
    _sign_fake_user_out()
    assert data.status_code == compiled_response.status_code
    assert data.headers == compiled_response.headers
    assert data.body == compiled_response.body
