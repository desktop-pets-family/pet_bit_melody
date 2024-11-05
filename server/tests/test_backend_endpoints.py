##
# EPITECH PROJECT, 2024
# Desktop_pet (Workspace)
# File description:
# test_character_server.py
##

"""_summary_
This file is in charge of testing the endpoints of the character server.
"""

import os
import sys
import time
import asyncio
from typing import Dict
from threading import Thread

import pytest

from status_check import QueryStatus
from query_boilerplate import QueryEndpoint
import constants as TCONST

sys.path.append(os.getcwd())


try:
    from src import Server
    from src import CONST
except ImportError as e:
    raise ImportError("Failed to import the src module") from e


def pytest_configure(config: pytest.Config):
    """_summary_
        This function is called when the pytest configuration is being set up.
    Args:
        config (pytest.Config): _description_
    """
    config.addinivalue_line(
        "markers",
        "critical: mark test as critical to determine final server stop"
    )
    config.addinivalue_line(
        "markers",
        "last: mark test to run after all other tests"
    )


@pytest.fixture(scope="module")
def setup_environment(request: pytest.FixtureRequest):
    """Fixture for setting up the environment once per module."""

    query: QueryEndpoint = QueryEndpoint(
        host=TCONST.QUERY_HOST,
        port=TCONST.PORT,
        delay=TCONST.QUERY_DELAY
    )

    status: QueryStatus = QueryStatus()

    server: Server = Server(
        host=TCONST.SERVER_HOST,
        port=TCONST.PORT,
        success=TCONST.SUCCESS,
        error=TCONST.ERROR,
        app_name="Area",
        debug=TCONST.DEBUG
    )

    active_thread: Thread = Thread(
        target=server.main,
        daemon=True, name=f"{TCONST.APP_NAME}_server_thread"
    )
    active_thread.start()

    # Let the server start
    print("Waiting for server to start (5 seconds delay)...")
    time.sleep(5)
    if active_thread.is_alive() is not True:
        pytest.skip("(test_server) thread failed to start")
    if server.is_running() is not True:
        pytest.skip("(test_server) Server is not running")
    call = server.runtime_data_initialised.database_link.get_table_names()
    if isinstance(call, int) and call == server.error:
        pytest.skip(
            "(test_server) Server failed to connect to the database"
        )
    print("Server started.")

    async def teardown():
        if server is not None:
            print("Shutting down server...")
            server.stop_server()
            print("Server stopped")
        if active_thread.is_alive() is True:
            print("Stopping thread (5 seconds grace) ...")
            active_thread.join(timeout=5)
            print("Thread stopped.")
        else:
            print("Thread already stopped.")
        return TCONST.SUCCESS

    def teardown_sync():
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(teardown())

    request.addfinalizer(teardown_sync)

    return {
        "query": query,
        "status": status,
        "server": server,
        "success": TCONST.SUCCESS,
        "error": TCONST.ERROR,
        "thread": active_thread,
        "tokens": {
            TCONST.LAMBDA_USER_TOKEN_KEY: {
                TCONST.PRETTY_TOKEN_KEY: {TCONST.TOKEN_AUTH_ID_STR: ""},
                TCONST.RAW_TOKEN_KEY: ""
            },
            TCONST.ADMIN_USER_TOKEN_KEY: {
                TCONST.PRETTY_TOKEN_KEY: {TCONST.TOKEN_AUTH_ID_STR: ""},
                TCONST.RAW_TOKEN_KEY: ""
            },
        },
        "accounts": {
            "lambda_user": {
                TCONST.USER_NORMAL_MODE: {
                    TCONST.UNODE_EMAIL_KEY: f"endpoint_{TCONST.USER_DATA_EMAIL}",
                    TCONST.UNODE_PASSWORD_KEY: f"endpoint_{TCONST.USER_DATA_PASSWORD}",
                    TCONST.UNODE_USERNAME_KEY: f"endpoint_{TCONST.USER_DATA_USERNAME}",
                    TCONST.UNODE_METHOD_KEY: f"{TCONST.USER_DATA_METHOD}",
                    TCONST.UNODE_FAVICON_KEY: f"{TCONST.USER_DATA_FAVICON}",
                    TCONST.UNODE_ADMIN_KEY: f"{TCONST.USER_DATA_ADMIN}"
                },
                TCONST.USER_PUT_MODE: {
                    TCONST.UNODE_EMAIL_KEY: f"endpoint_{TCONST.USER_DATA_EMAIL_REBIND}",
                    TCONST.UNODE_PASSWORD_KEY: f"endpoint_{TCONST.USER_DATA_PASSWORD_REBIND}",
                    TCONST.UNODE_USERNAME_KEY: f"endpoint_{TCONST.USER_DATA_USERNAME_REBIND}",
                    TCONST.UNODE_METHOD_KEY: f"{TCONST.USER_DATA_METHOD}",
                    TCONST.UNODE_FAVICON_KEY: f"{TCONST.USER_DATA_FAVICON}",
                    TCONST.UNODE_ADMIN_KEY: f"{TCONST.USER_DATA_ADMIN}"
                },
                TCONST.USER_PATCH_MODE: {
                    TCONST.UNODE_EMAIL_KEY: f"endpoint_{TCONST.USER_DATA_EMAIL_PATCH}",
                    TCONST.UNODE_PASSWORD_KEY: f"endpoint_{TCONST.USER_DATA_PASSWORD_PATCH}",
                    TCONST.UNODE_USERNAME_KEY: f"endpoint_{TCONST.USER_DATA_USERNAME_PATCH}",
                    TCONST.UNODE_METHOD_KEY: f"{TCONST.USER_DATA_METHOD}",
                    TCONST.UNODE_FAVICON_KEY: f"{TCONST.USER_DATA_FAVICON}",
                    TCONST.UNODE_ADMIN_KEY: f"{TCONST.USER_DATA_ADMIN}"
                }
            },
            "admin_user": {
                TCONST.USER_NORMAL_MODE: {
                    TCONST.UNODE_EMAIL_KEY: f"endpoint_{TCONST.ADMIN_DATA_EMAIL}",
                    TCONST.UNODE_PASSWORD_KEY: f"endpoint_{TCONST.ADMIN_DATA_PASSWORD}",
                    TCONST.UNODE_USERNAME_KEY: f"endpoint_{TCONST.ADMIN_DATA_USERNAME}",
                    TCONST.UNODE_METHOD_KEY: f"{TCONST.ADMIN_DATA_METHOD}",
                    TCONST.UNODE_FAVICON_KEY: f"{TCONST.ADMIN_DATA_FAVICON}",
                    TCONST.UNODE_ADMIN_KEY: f"{TCONST.ADMIN_DATA_ADMIN}"
                },
                TCONST.USER_PUT_MODE: {
                    TCONST.UNODE_EMAIL_KEY: f"endpoint_{TCONST.ADMIN_DATA_EMAIL_REBIND}",
                    TCONST.UNODE_PASSWORD_KEY: f"endpoint_{TCONST.ADMIN_DATA_PASSWORD_REBIND}",
                    TCONST.UNODE_USERNAME_KEY: f"endpoint_{TCONST.ADMIN_DATA_USERNAME_REBIND}",
                    TCONST.UNODE_METHOD_KEY: f"{TCONST.ADMIN_DATA_METHOD}",
                    TCONST.UNODE_FAVICON_KEY: f"{TCONST.ADMIN_DATA_FAVICON}",
                    TCONST.UNODE_ADMIN_KEY: f"{TCONST.ADMIN_DATA_ADMIN}"
                },
                TCONST.USER_PATCH_MODE: {
                    TCONST.UNODE_EMAIL_KEY: f"endpoint_{TCONST.ADMIN_DATA_EMAIL_PATCH}",
                    TCONST.UNODE_PASSWORD_KEY: f"endpoint_{TCONST.ADMIN_DATA_PASSWORD_PATCH}",
                    TCONST.UNODE_USERNAME_KEY: f"endpoint_{TCONST.ADMIN_DATA_USERNAME_PATCH}",
                    TCONST.UNODE_METHOD_KEY: f"{TCONST.ADMIN_DATA_METHOD}",
                    TCONST.UNODE_FAVICON_KEY: f"{TCONST.ADMIN_DATA_FAVICON}",
                    TCONST.UNODE_ADMIN_KEY: f"{TCONST.ADMIN_DATA_ADMIN}"
                }
            }
        },
        TCONST.RUNTIME_NODE_CRITICAL_KEY: False,
        "teardown_func": teardown_sync
    }


@pytest.mark.usefixtures("setup_environment")
class TestServer:
    """Class for running tests on the character server endpoint."""

    def check_server(self, setup_environment, critical: bool = False):
        """Helper function to check if the server is still running."""
        server: Server = setup_environment["server"]
        if server is None or setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] is True:
            if critical is True:
                setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
            pytest.skip(
                "(test_server) Server is not running, skipping the test."
            )

    def test_home(self, setup_environment):
        """ Test the / endpoint of the server. """
        self.check_server(setup_environment)

        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        response = query.get_endpoint(TCONST.PATH_GET_HOME)
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_GET_HOME_RESPONSE_NOT_LOGGED_IN,
            "test_home"
        ) is True

    def test_api_home(self, setup_environment):
        """ Test the / endpoint of the server. """
        self.check_server(setup_environment)

        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        response = query.get_endpoint(TCONST.PATH_GET_API_HOME)
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_GET_HOME_API_RESPONSE_NOT_LOGGED_IN,
            "test_api_home"
        ) is True

    @pytest.mark.critical
    def test_post_register_lambda(self, setup_environment):
        """_summary_
            Test the /register endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment, True)
        path: str = TCONST.PATH_PUT_REGISTER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["lambda_user"][TCONST.USER_NORMAL_MODE]
        body = {
            "email": accounts[TCONST.UNODE_EMAIL_KEY],
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        TCONST.IDISP.log_info(f"body = {body}")
        response = query.post_endpoint(path, content=body)
        TCONST.IDISP.log_info(f"response.json() = {response.json()}")
        token_node = ""
        if status.success(response) is True:
            token_node = f"{response.json()['token']}"
        else:
            setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
        correct_node = TCONST.RESPONSE_POST_REGISTER
        correct_node['msg'] = f"Welcome {accounts['username']}"
        correct_node['token'] = token_node
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            correct_node,
            "test_post_register_lambda"
        ) is True

    @pytest.mark.critical
    def test_post_login_lambda(self, setup_environment):
        """_summary_
            Test the /login endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment, True)
        path: str = TCONST.PATH_POST_LOGIN
        token: Dict[str, Dict[str, str]] = setup_environment["tokens"]
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["lambda_user"][TCONST.USER_NORMAL_MODE]
        body = {
            "email": accounts[TCONST.UNODE_EMAIL_KEY],
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        TCONST.IDISP.log_info(f"body = {body}")
        response = query.post_endpoint(path, content=body)
        TCONST.IDISP.log_info(f"response.json() = {response.json()}")
        if status.success(response) is True:
            token_node = f"{response.json()['token']}"
            msg = f"Bearer {token_node}"
            token[TCONST.LAMBDA_USER_TOKEN_KEY][TCONST.PRETTY_TOKEN_KEY][TCONST.TOKEN_AUTH_ID_STR] = msg
            token[TCONST.LAMBDA_USER_TOKEN_KEY][TCONST.RAW_TOKEN_KEY] = token_node
        else:
            setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
        correct_node = TCONST.RESPONSE_POST_LOGIN
        correct_node['msg'] = f"Welcome {accounts['username']}"
        correct_node["token"] = token_node
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            correct_node,
            "test_post_login_lambda"
        ) is True

    @pytest.mark.critical
    def test_post_register_admin(self, setup_environment):
        """_summary_
            Test the /register endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment, True)
        server: Server = setup_environment["server"]
        path = TCONST.PATH_PUT_REGISTER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["admin_user"][TCONST.USER_NORMAL_MODE]
        body = {
            "email": accounts[TCONST.UNODE_EMAIL_KEY],
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        TCONST.IDISP.log_info(f"body = {body}")
        response = query.post_endpoint(path, content=body)
        TCONST.IDISP.log_info(f"response.json() = {response.json()}")
        if status.success(response) is True:
            column = server.runtime_data_initialised.database_link.get_table_column_names(
                CONST.TAB_ACCOUNTS
            )
            if column == server.error or len(column) == 0:
                setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
                assert column == server.success
            user_node = server.runtime_data_initialised.database_link.get_data_from_table(
                CONST.TAB_ACCOUNTS,
                column,
                f"email='{accounts['email']}'"
            )
            if user_node == server.error:
                setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
                assert user_node == server.success
            column.pop(0)
            uid = user_node[0].pop("id")
            user_node[0]['admin'] = str(TCONST.ADMIN_DATA_ADMIN)
            user_node_list = list(user_node[0].values())
            msg = f"user_node_list = {user_node_list}\n"
            msg += f"user_node = {user_node}"
            server.disp.log_debug(msg, "test_post_register_admin")
            command_status = server.runtime_data_initialised.database_link.update_data_in_table(
                CONST.TAB_ACCOUNTS,
                user_node_list,
                column,
                f"id='{uid}'"
            )
            assert command_status == server.success
        token_node = ""
        if status.success(response) is True:
            token_node = f"{response.json()['token']}"
        else:
            setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
        correct_node = TCONST.RESPONSE_POST_REGISTER
        correct_node['msg'] = f"Welcome {accounts['username']}"
        correct_node['token'] = token_node
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            correct_node,
            "test_post_register_admin"
        ) is True

    @pytest.mark.critical
    def test_post_login_admin(self, setup_environment):
        """_summary_
            Test the /login endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment, True)
        path = TCONST.PATH_POST_LOGIN
        token: Dict[str, Dict[str, str]] = setup_environment["tokens"]
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["admin_user"][TCONST.USER_NORMAL_MODE]
        body = {
            "email": accounts[TCONST.UNODE_EMAIL_KEY],
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        TCONST.IDISP.log_info(f"body = {body}")
        response = query.post_endpoint(path, content=body)
        TCONST.IDISP.log_info(f"response.json() = {response.json()}")
        if status.success(response) is True:
            token_node = f"{response.json()['token']}"
            msg = f"Bearer {token_node}"
            token[TCONST.ADMIN_USER_TOKEN_KEY][TCONST.PRETTY_TOKEN_KEY][TCONST.TOKEN_AUTH_ID_STR] = msg
            token[TCONST.ADMIN_USER_TOKEN_KEY][TCONST.RAW_TOKEN_KEY] = token_node
        else:
            setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
        correct_node = TCONST.RESPONSE_POST_LOGIN
        correct_node['msg'] = f"Welcome {accounts['username']}"
        correct_node["token"] = token_node
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            correct_node,
            "test_post_login_admin"
        ) is True

    def test_put_user_lambda(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_PUT_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.LAMBDA_USER_TOKEN_KEY]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["lambda_user"][TCONST.USER_PUT_MODE]
        body = {
            "username": accounts[TCONST.UNODE_USERNAME_KEY],
            "email": accounts[TCONST.UNODE_EMAIL_KEY],
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }

        response = query.put_endpoint(
            path, content=body, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_PUT_USER,
            "test_put_user_lambda"
        ) is True

    def test_put_user_admin(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_PUT_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.ADMIN_USER_TOKEN_KEY]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["admin_user"][TCONST.USER_PUT_MODE]
        body = {
            "username": accounts[TCONST.UNODE_USERNAME_KEY],
            "email": accounts[TCONST.UNODE_EMAIL_KEY],
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        response = query.put_endpoint(
            path, content=body, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_PUT_USER,
            "test_put_user_admin"
        ) is True

    def test_patch_user_lambda_username(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_PATCH_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.LAMBDA_USER_TOKEN_KEY]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["lambda_user"][TCONST.USER_PATCH_MODE]
        body = {
            "username": accounts[TCONST.UNODE_USERNAME_KEY]
        }
        response = query.patch_endpoint(
            path, content=body, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_PATCH_USER,
            "test_patch_user_lambda_username"
        ) is True

    def test_patch_user_lambda_email(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_PATCH_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.LAMBDA_USER_TOKEN_KEY]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["lambda_user"][TCONST.USER_PATCH_MODE]
        body = {
            "email": accounts[TCONST.UNODE_EMAIL_KEY]
        }
        response = query.patch_endpoint(
            path, content=body, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_PATCH_USER,
            "test_path_user_lambda_email"
        ) is True

    def test_patch_user_lambda_password(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_PATCH_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.LAMBDA_USER_TOKEN_KEY]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["lambda_user"][TCONST.USER_PATCH_MODE]
        body = {
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        response = query.patch_endpoint(
            path, content=body, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_PATCH_USER,
            "test_patch_user_lambda_password"
        ) is True

    def test_patch_user_admin_username(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_PATCH_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.ADMIN_USER_TOKEN_KEY]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["admin_user"][TCONST.USER_PATCH_MODE]
        body = {
            "username": accounts[TCONST.UNODE_USERNAME_KEY]
        }
        response = query.patch_endpoint(
            path, content=body, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_PATCH_USER,
            "test_patch_user_admin_username"
        ) is True

    def test_patch_user_admin_email(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_PATCH_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.ADMIN_USER_TOKEN_KEY]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["admin_user"][TCONST.USER_PATCH_MODE]
        body = {
            "email": accounts[TCONST.UNODE_EMAIL_KEY]
        }
        response = query.patch_endpoint(
            path, content=body, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_PATCH_USER,
            "test_path_user_admin_email"
        ) is True

    def test_patch_user_admin_password(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_PATCH_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.ADMIN_USER_TOKEN_KEY]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["admin_user"][TCONST.USER_PATCH_MODE]
        body = {
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        response = query.patch_endpoint(
            path, content=body, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_PATCH_USER,
            "test_patch_user_admin_password"
        ) is True

    def test_get_user_lambda(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        title = "test_get_user_lambda"
        self.check_server(setup_environment)
        server: Server = setup_environment["server"]
        path = TCONST.PATH_GET_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.LAMBDA_USER_TOKEN_KEY]
        response = query.get_endpoint(
            path, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        response_node = TCONST.RESPONSE_GET_USER
        if status.success(response) is True:
            usr_id = server.runtime_data_initialised.boilerplate_non_http_initialised.get_user_id_from_token(
                title, token[TCONST.RAW_TOKEN_KEY]
            )
            TCONST.IDISP.log_debug(f"usr_id={usr_id}", title)
            if isinstance(usr_id, str) is False:
                TCONST.IDISP.log_error(f"Failed to find user: {usr_id}", title)
                assert usr_id == server.error
            column = server.runtime_data_initialised.database_link.get_table_column_names(
                CONST.TAB_ACCOUNTS
            )
            TCONST.IDISP.log_debug(f"column = {column}", title)
            if column == server.error or len(column) == 0:
                setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
                assert column == server.success
            user_node = server.runtime_data_initialised.database_link.get_data_from_table(
                CONST.TAB_ACCOUNTS,
                column,
                f"id={usr_id}",
                beautify=True
            )
            TCONST.IDISP.log_debug(f"user_node={user_node}", title)
            if user_node == server.error or len(user_node) == 0:
                assert user_node == server.success
            new_profile = user_node[0]
            for i in CONST.USER_INFO_BANNED:
                if i in new_profile:
                    new_profile.pop(i)
            if CONST.USER_INFO_ADMIN_NODE in new_profile:
                new_profile[CONST.USER_INFO_ADMIN_NODE] = bool(
                    new_profile[CONST.USER_INFO_ADMIN_NODE]
                )
            response_node["msg"] = new_profile
            TCONST.IDISP.log_debug(f"final node = {response_node}", title)
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            response_node,
            title
        ) is True

    def test_get_user_admin(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        title = "test_get_user_admin"
        self.check_server(setup_environment)
        server: Server = setup_environment["server"]
        path = TCONST.PATH_GET_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.ADMIN_USER_TOKEN_KEY]
        response = query.get_endpoint(
            path, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        response_node = TCONST.RESPONSE_GET_USER
        if status.success(response) is True:
            usr_id = server.runtime_data_initialised.boilerplate_non_http_initialised.get_user_id_from_token(
                title, token[TCONST.RAW_TOKEN_KEY]
            )
            TCONST.IDISP.log_debug(f"usr_id={usr_id}", title)
            if isinstance(usr_id, str) is False:
                TCONST.IDISP.log_error(f"Failed to find user: {usr_id}", title)
                assert usr_id == server.error
            column = server.runtime_data_initialised.database_link.get_table_column_names(
                CONST.TAB_ACCOUNTS
            )
            TCONST.IDISP.log_debug(f"column = {column}", title)
            if column == server.error or len(column) == 0:
                setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
                assert column == server.success
            user_node = server.runtime_data_initialised.database_link.get_data_from_table(
                CONST.TAB_ACCOUNTS,
                column,
                f"id={usr_id}",
                beautify=True
            )
            TCONST.IDISP.log_debug(f"user_node={user_node}", title)
            if user_node == server.error or len(user_node) == 0:
                assert user_node == server.success
            new_profile = user_node[0]
            for i in CONST.USER_INFO_BANNED:
                if i in new_profile:
                    new_profile.pop(i)
            if CONST.USER_INFO_ADMIN_NODE in new_profile:
                new_profile[CONST.USER_INFO_ADMIN_NODE] = bool(
                    new_profile[CONST.USER_INFO_ADMIN_NODE]
                )
            response_node["msg"] = new_profile
            TCONST.IDISP.log_debug(f"final node = {response_node}", title)
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            response_node,
            title
        ) is True

    def test_get_user_id_lambda(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        title = "test_get_user_id_lambda"
        self.check_server(setup_environment)
        server: Server = setup_environment["server"]
        path = TCONST.PATH_GET_USER_ID
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.LAMBDA_USER_TOKEN_KEY]
        response = query.get_endpoint(
            path, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        response_node = TCONST.RESPONSE_GET_USER_ID
        if status.success(response) is True:
            usr_id = server.runtime_data_initialised.boilerplate_non_http_initialised.get_user_id_from_token(
                title, token[TCONST.RAW_TOKEN_KEY]
            )
            TCONST.IDISP.log_debug(f"usr_id={usr_id}", title)
            if isinstance(usr_id, str) is False:
                TCONST.IDISP.log_error(f"Failed to find user: {usr_id}", title)
                assert usr_id == server.error
            response_node["msg"] = f"Your id is {usr_id}"
            response_node["resp"] = usr_id
            TCONST.IDISP.log_debug(f"final node = {response_node}", title)
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            response_node,
            title
        ) is True

    def test_get_user_id_admin(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        title = "test_get_user_id_admin"
        self.check_server(setup_environment)
        server: Server = setup_environment["server"]
        path = TCONST.PATH_GET_USER_ID
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[
            str, Dict[str, str]
        ] = setup_environment["tokens"][TCONST.ADMIN_USER_TOKEN_KEY]
        response = query.get_endpoint(
            path, header=token[TCONST.PRETTY_TOKEN_KEY]
        )
        response_node = TCONST.RESPONSE_GET_USER_ID
        if status.success(response) is True:
            usr_id = server.runtime_data_initialised.boilerplate_non_http_initialised.get_user_id_from_token(
                title, token[TCONST.RAW_TOKEN_KEY]
            )
            TCONST.IDISP.log_debug(f"usr_id={usr_id}", title)
            if isinstance(usr_id, str) is False:
                TCONST.IDISP.log_error(f"Failed to find user: {usr_id}", title)
                assert usr_id == server.error
            response_node["msg"] = f"Your id is {usr_id}"
            response_node["resp"] = usr_id
            TCONST.IDISP.log_debug(f"final node = {response_node}", title)
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            response_node,
            title
        ) is True

    def test_logout_user_lambda(self, setup_environment):
        """_summary_
            Test the /logout endpoint of the server.

        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment, True)
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["lambda_user"][TCONST.USER_PATCH_MODE]
        body = {
            "email": accounts[TCONST.UNODE_EMAIL_KEY],
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        TCONST.IDISP.log_info(f"body = {body}")
        response = query.post_endpoint(TCONST.PATH_POST_LOGIN, content=body)
        TCONST.IDISP.log_info(f"response.json() = {response.json()}")
        pretty_token = ""
        if status.success(response) is True:
            token_node = f"{response.json()['token']}"
            active_token = f"Bearer {token_node}"
            pretty_token = {TCONST.TOKEN_AUTH_ID_STR: active_token}
        else:
            assert status.success(response) is True
        logout_response = query.post_endpoint(
            TCONST.PATH_POST_LOGOUT, header=pretty_token
        )
        correct_node = TCONST.RESPONSE_POST_LOGOUT
        assert status.success(response) is True
        assert status.success(logout_response) is True
        assert TCONST.are_json_responses_identical(
            logout_response.json(),
            correct_node,
            "test_post_logout_lambda"
        ) is True

    def test_logout_user_admin(self, setup_environment):
        """_summary_
            Test the /logout endpoint of the server.

        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment, True)
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        accounts: Dict[
            str, any
        ] = setup_environment["accounts"]["admin_user"][TCONST.USER_PATCH_MODE]
        body = {
            "email": accounts[TCONST.UNODE_EMAIL_KEY],
            "password": accounts[TCONST.UNODE_PASSWORD_KEY]
        }
        response = query.post_endpoint(TCONST.PATH_POST_LOGIN, content=body)
        pretty_token = ""
        if status.success(response) is True:
            token_node = f"{response.json()['token']}"
            active_token = f"Bearer {token_node}"
            pretty_token = {TCONST.TOKEN_AUTH_ID_STR: active_token}
        else:
            setup_environment[TCONST.RUNTIME_NODE_CRITICAL_KEY] = True
        logout_response = query.post_endpoint(
            TCONST.PATH_POST_LOGOUT, header=pretty_token
        )
        correct_node = TCONST.RESPONSE_POST_LOGOUT
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            logout_response.json(),
            correct_node,
            "test_post_logout_admin"
        ) is True

    @pytest.mark.last
    def test_delete_user_lambda(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_DELETE_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[str, Dict[str, str]] = setup_environment["tokens"]
        response = query.delete_endpoint(
            path, header=token[TCONST.LAMBDA_USER_TOKEN_KEY][TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_DELETE_USER,
            "test_delete_user_lambda"
        ) is True

    @pytest.mark.last
    def test_delete_user_admin(self, setup_environment):
        """_summary_
            Test the /user endpoint of the server.
        Args:
            setup_environment (_type_): _description_
        """
        self.check_server(setup_environment)
        path = TCONST.PATH_DELETE_USER
        query: QueryEndpoint = setup_environment["query"]
        status: QueryStatus = setup_environment["status"]
        token: Dict[str, Dict[str, str]] = setup_environment["tokens"]
        response = query.delete_endpoint(
            path, header=token[TCONST.ADMIN_USER_TOKEN_KEY][TCONST.PRETTY_TOKEN_KEY]
        )
        assert status.success(response) is True
        assert TCONST.are_json_responses_identical(
            response.json(),
            TCONST.RESPONSE_DELETE_USER,
            "test_delete_user_admin"
        ) is True

    # @pytest.mark.last
    # def test_post_stop_server(self, setup_environment):
    #     """ Test the /stop endpoint of the server. """
    #     self.check_server(setup_environment)
    #     teardown_func: callable = setup_environment["teardown_func"]
    #     success: int = setup_environment["success"]
    #     status = teardown_func()
    #     assert status == success
