"""_summary_
    File in charge of testing the variables class
"""
import os
import sys

sys.path.append(os.path.join("..", os.getcwd()))
sys.path.append(os.getcwd())

try:
    import constants as TCONST
except ImportError as e:
    raise ImportError("Failed to import the unit test constants module") from e

try:
    from src.lib.actions import constants as ACONST
    from src.lib.actions.main import ActionsMain
    from src.lib.sql.sql_manager import SQL
    from src.lib.components import constants as CONST
    from src.lib.components.runtime_data import RuntimeData
    from src.lib.boilerplates.non_web import BoilerplateNonHTTP
    from src.lib.boilerplates.responses import BoilerplateResponses
    from src.lib.components.password_handling import PasswordHandling
except ImportError as e:
    raise ImportError("Failed to import the src module") from e


ERROR = TCONST.ERROR
SUCCESS = TCONST.SUCCESS
DEBUG = TCONST.DEBUG


RDI = RuntimeData(TCONST.SERVER_HOST, TCONST.PORT, "Area", ERROR, SUCCESS)
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

SQLI = SQL(
    url=CONST.DB_HOST,
    port=CONST.DB_PORT,
    username=CONST.DB_USER,
    password=CONST.DB_PASSWORD,
    db_name=CONST.DB_DATABASE,
    debug=DEBUG
)
RDI.database_link = SQLI

RDI.boilerplate_responses_initialised = BRI

AMI = ActionsMain(
    runtime_data=RDI,
    success=SUCCESS,
    error=ERROR,
    debug=DEBUG
)

PHI = PasswordHandling(
    error=ERROR,
    success=SUCCESS,
    debug=DEBUG
)


def test_random_delay() -> None:
    """_summary_
        Function in charge of testing the log types.
    """
    title = "test_random_delay"
    max_value = 1
    min_value = 0
    iterations = 20
    msg = f"max_value = {max_value}, min_value = {min_value}"
    msg += f" iterations = {iterations}"
    AMI.disp.log_debug(msg, title)
    for i in range(iterations):
        delay = AMI.random_delay(max_value)
        AMI.disp.log_debug(f"iteration: {i}, delay = {delay}")
        assert delay >= min_value
        assert delay <= max_value
