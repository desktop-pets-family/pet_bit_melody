"""_summary_
    File in charge of testing the paths class.
"""
import os
import sys
from fastapi import Request, Response, FastAPI
import constants as TCONST

sys.path.append(os.getcwd())
try:
    from src.lib.components.paths import ServerPaths
    from src.lib.components.runtime_data import RuntimeData
    from src.lib.components.endpoints_routes import Endpoints
    from src.lib.components.oauth_authentication import OAuthAuthentication
    from src.lib.components.constants import PATH_KEY, ENDPOINT_KEY,  METHOD_KEY, ALLOWED_METHODS
except ImportError as e:
    raise ImportError("Failed to import the src module") from e


def dummy_path(request: Request) -> Response:
    """_summary_
        Function in charge of testing if the current password is the same as the hashed version.
    """
    return {"msg": "Hello World !"}


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
RDI.oauth_authentication_initialised = OAuthAuthentication(
    runtime_data=RDI,
    success=SUCCESS,
    error=ERROR,
    debug=DEBUG
)
SPI = ServerPaths(
    runtime_data=RDI,
    success=SUCCESS,
    error=ERROR,
    debug=DEBUG
)
RDI.paths_initialised = SPI


def test_path_adding() -> None:
    """_summary_
        Function in charge of testing if the current password is the same as the hashed version.
    """
    status = SPI.add_path(
        "/dummy_path",
        dummy_path,
        "GET"
    )
    assert status == SUCCESS
    assert len(SPI.routes) == 1
    assert SPI.routes[0][PATH_KEY] == "/dummy_path"
    assert SPI.routes[0][ENDPOINT_KEY] is dummy_path
    assert SPI.routes[0][METHOD_KEY] == ["GET"]


def test_load_default_paths() -> None:
    """_summary_
        Function in charge of testing the load_default_paths_initialised
    """
    SPI.load_default_paths_initialised()
    assert len(SPI.routes) > 0
    for i in SPI.routes:
        assert isinstance(i[PATH_KEY], str) is True
        assert callable(i[ENDPOINT_KEY]) is True
        assert isinstance(i[METHOD_KEY], list) is True
        assert len(i[METHOD_KEY]) > 0
        for methods in i[METHOD_KEY]:
            assert isinstance(methods, str) is True
            assert methods in ALLOWED_METHODS


def test_inject_routes() -> None:
    """_summary_
        Function in charge of testing the inject_routes
    """
    SPI.add_path("/dd", dummy_path, "GET")
    SPI.load_default_paths_initialised()
    try:
        SPI.inject_routes()
    except Exception as e:
        print(f"error: {str(e)}")
        assert False
