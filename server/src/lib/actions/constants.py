"""_summary_
    This file contains the constants for the actions program.
    These are used to standardise error logging and other sections of the program.
"""
# ---------------------------------- Imports  ----------------------------------
from typing import Union
import operator
from datetime import datetime, date
from .secrets import Secrets

# ---------------------------------- log type ----------------------------------

TYPE_UNKNOWN = "UNKNOWN LOGGING TYPE"
TYPE_API = "API"
TYPE_SERVICE = "SERVICE"
TYPE_SERVICE_TRIGGER = "SERVICE TRIGGER"
TYPE_SERVICE_ACTION = "SERVICE ACTION"
TYPE_ACTION = "ACTION"
TYPE_UNDEFINED = "UNDEFINED"
TYPE_MISMATCH = "MISMATCH"
TYPE_BEFORE_ASSIGNEMENT = "REFERENCED BEFORE ASSIGNEMENT"
TYPE_DIV_ZERO = "DIVISION BY ZERO"
TYPE_SYNTAX_ERROR = "SYNTAX ERROR"
TYPE_RUNTIME_ERROR = "RUNTIME ERROR"
TYPE_INCOMPARABLE = "INCOMPARABLE TYPES"
TYPE_OVERFLOW = "VALUE OVERFLOW"
TYPE_UNDERFLOW = "VALUE UNDERFLOW"

# -------------------------------- Error codes  --------------------------------

CODE_UNKNOWN = -1
CODE_INFO = 0
CODE_SUCCESS = 1
CODE_DEBUG = 2
CODE_WARNING = 3
CODE_ERROR = 4
CODE_CRITICAL = 5
CODE_FATAL = 6

# -------------------------------- Error level  --------------------------------

LEVEL_UNKNOWN = "UNKNOWN"
LEVEL_INFO = "INFO"
LEVEL_SUCCESS = "SUCCESS"
LEVEL_DEBUG = "DEBUG"
LEVEL_WARNING = "WARNING"
LEVEL_ERROR = "ERROR"
LEVEL_CRITICAL = "CRITICAL"
LEVEL_FATAL = "FATAL"

# ------------------------------- Error messages -------------------------------

MSG_UNKNOWN = "Unknown: Operation executed with unknown status."
MSG_INFO = "Information: Operation executed without any issues."
MSG_SUCCESS = "Success: Operation completed successfully."
MSG_DEBUG = "Debug: Tracking detailed operational data for diagnostics."
MSG_WARNING = "Warning: Potential issue detected. Review is recommended."
MSG_ERROR = "Error: Operation could not be completed successfully."
MSG_CRITICAL = "Critical: Immediate attention required to prevent severe impact."
MSG_FATAL = "Fatal: System failure imminent. Immediate intervention necessary."

# ----------------------------- Error equivalence  -----------------------------

LOG_EQUIVALENCE = {
    CODE_UNKNOWN: LEVEL_UNKNOWN,
    CODE_INFO: LEVEL_INFO,
    CODE_SUCCESS: LEVEL_SUCCESS,
    CODE_DEBUG: LEVEL_DEBUG,
    CODE_WARNING: LEVEL_WARNING,
    CODE_ERROR: LEVEL_ERROR,
    CODE_CRITICAL: LEVEL_CRITICAL,
    CODE_FATAL: LEVEL_FATAL,
}

LOG_MESSAGE_EQUIVALENCE = {
    CODE_UNKNOWN: MSG_UNKNOWN,
    CODE_INFO: MSG_INFO,
    CODE_SUCCESS: MSG_SUCCESS,
    CODE_DEBUG: MSG_DEBUG,
    CODE_WARNING: MSG_WARNING,
    CODE_ERROR: MSG_ERROR,
    CODE_CRITICAL: MSG_CRITICAL,
    CODE_FATAL: MSG_FATAL,
}

# -------------------------------- List checks  --------------------------------

LIST_TYPE = [
    TYPE_UNKNOWN,
    TYPE_API,
    TYPE_SERVICE,
    TYPE_SERVICE_TRIGGER,
    TYPE_SERVICE_ACTION,
    TYPE_ACTION,
    TYPE_UNDEFINED,
    TYPE_MISMATCH,
    TYPE_BEFORE_ASSIGNEMENT,
    TYPE_DIV_ZERO,
    TYPE_SYNTAX_ERROR,
    TYPE_RUNTIME_ERROR,
    TYPE_INCOMPARABLE,
    TYPE_OVERFLOW,
    TYPE_UNDERFLOW
]

LIST_CODE = [
    CODE_UNKNOWN,
    CODE_INFO,
    CODE_SUCCESS,
    CODE_DEBUG,
    CODE_WARNING,
    CODE_ERROR,
    CODE_CRITICAL,
    CODE_FATAL
]

LIST_LEVEL_INFO = [
    LEVEL_UNKNOWN,
    LEVEL_INFO,
    LEVEL_SUCCESS,
    LEVEL_DEBUG,
    LEVEL_WARNING,
    LEVEL_ERROR,
    LEVEL_CRITICAL,
    LEVEL_FATAL
]

LIST_MSG = [
    MSG_UNKNOWN,
    MSG_INFO,
    MSG_SUCCESS,
    MSG_DEBUG,
    MSG_WARNING,
    MSG_ERROR,
    MSG_CRITICAL,
    MSG_FATAL
]

# ---------------------------- Operator equivalence ----------------------------


def _spaceship(a, b) -> int:
    """Compares two values and returns:
        -1 if a < b
         0 if a == b
         1 if a > b

    Args:
        a: The first value to compare.
        b: The second value to compare.

    Returns:
        int: -1, 0, or 1 based on the comparison.
    """
    if a < b:
        return -1
    if a == b:
        return 0
    return 1


OPERATOR_EXCHANGE = {
    "==": operator.eq,
    "===": operator.eq,
    "=": operator.eq,  # Bash string equality
    "eq": operator.eq,
    "-eq": operator.eq,
    "!=": operator.ne,
    "<>": operator.ne,  # Not equal in SQL-like contexts
    "ne": operator.ne,
    "-ne": operator.ne,
    "<": operator.lt,
    "lt": operator.lt,
    "-lt": operator.lt,
    ">": operator.gt,
    "gt": operator.gt,
    "-gt": operator.gt,
    "<=": operator.le,
    "le": operator.le,
    "-le": operator.le,
    ">=": operator.ge,
    "ge": operator.ge,
    "-ge": operator.ge,
    "<=>": _spaceship,  # Custom spaceship operator
    "equal to": operator.eq,
    "less than": operator.lt,
    "not equal to": operator.ne,
    "greater than": operator.gt,
    "less than or equal to": operator.le,
    "greater than or equal to": operator.ge,
}

# ---------------------------------- Secrets  ----------------------------------
SECRETS_EQUIVALENCE = {
    "secrets.now": Secrets.now_server,
    "secrets.current_date": Secrets.current_date,
    "secrets.current_time": Secrets.current_time,
    "secrets.now_utc": Secrets.now_utc,
    "secrets.current_date_utc": Secrets.current_date_utc,
    "secrets.current_time_utc": Secrets.current_time_utc,
    "secrets.now_server": Secrets.now_server,
    "secrets.current_date_server": Secrets.current_date_server,
    "secrets.current_time_server": Secrets.current_time_server,
    "secret.now": Secrets.now_server,
    "secret.current_date": Secrets.current_date,
    "secret.current_time": Secrets.current_time,
    "secret.now_utc": Secrets.now_utc,
    "secret.current_date_utc": Secrets.current_date_utc,
    "secret.current_time_utc": Secrets.current_time_utc,
    "secret.now_server": Secrets.now_server,
    "secret.current_date_server": Secrets.current_date_server,
    "secret.current_time_server": Secrets.current_time_server,
    "now": Secrets.now_server,
    "current_date": Secrets.current_date,
    "current_time": Secrets.current_time,
    "now_utc": Secrets.now_utc,
    "current_date_utc": Secrets.current_date_utc,
    "current_time_utc": Secrets.current_time_utc,
    "now_server": Secrets.now_server,
    "current_date_server": Secrets.current_date_server,
    "current_time_server": Secrets.current_time_server
}


# --------------------------------- Data types ---------------------------------

CONTENT_TYPE_KEY = "type"
CONTENT_KEY = "content"

CONTENT_TYPES_JSON = {"application/json", "application/ld+json"}
CONTENT_TYPES_TEXT = {
    "text/html",
    "text/plain",
    "text/csv",
    "text/xml",
    "text/css"
}
CONTENT_TYPES_XML = {"application/xml", "application/xhtml+xml", "text/xml"}
CONTENT_TYPES_BINARY = {
    "application/octet-stream",
    "application/pdf",
    "application/zip",
    "application/x-gzip",
    "application/x-tar",
    "application/x-7z-compressed",
    "application/x-rar-compressed",
    "application/x-bzip2",
    "application/x-xz",
    "application/x-lzip",
    "application/x-lzma",
    "application/x-lzop",
    "application/x-snappy-framed",
    "application/xz",
    "application/x-arj",
    "application/x-cpio",
    "application/x-shar",
    "application/x-compress",
    "application/x-ace",
    "application/x-stuffit",
    "application/x-stuffitx",
    "application/x-iso9660-image",
    "application/x-nrg",
    "application/x-gear",
    "application/x-dms",
    "application/x-cfs-compressed",
    "application/x-astrotite-afa",
    "application/x-squeeze",
    "application/x-lzh-compressed",
    "application/x-lha",
    "application/x-lrzip",
    "application/x-lrzip-compressed-tar",
    "application/x-arc",
    "application/x-ear",
    "application/x-war",
    "application/x-cab",
    "application/x-msi",
    "application/x-alz",
    "application/x-ar",
    "application/x-deb",
    "application/x-rpm",
    "application/x-sis",
    "application/x-apk",
    "application/x-ipk",
    "application/x-xpi",
    "application/x-java-archive",
    "application/x-webarchive",
    "application/x-b1",
    "application/x-b6z",
    "application/x-cbr",
    "application/x-cb7",
    "application/x-cbt",
    "application/x-cbz",
    "application/x-cba",
    "application/java-archive",
    "application/x-shockwave-flash",
    "application/x-www-form-urlencoded",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.ms-powerpoint",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.android.package-archive"
}
CONTENT_TYPES_AUDIO = {
    "audio/midi",
    "audio/mpeg",
    "audio/webm",
    "audio/ogg",
    "audio/wav",
    "audio/flac",
    "audio/aac",
    "audio/mp4",
    "audio/opus",
    "audio/x-ms-wma",
    "audio/vnd.rn-realaudio"
}
CONTENT_TYPES_IMAGES = {
    "image/gif",
    "image/jpeg",
    "image/png",
    "image/webp",
    "image/svg+xml",
    "image/bmp",
    "image/vnd.microsoft.icon",
    "image/tiff",
    "image/x-icon",
    "image/vnd.djvu"
}
CONTENT_TYPES_VIDEO = {
    "video/mpeg",
    "video/mp4",
    "video/quicktime",
    "video/x-ms-wmv",
    "video/x-msvideo",
    "video/x-flv",
    "video/webm"
}

# ---------------- Compiled response nodes for the request info ----------------
RESPONSE_NODE_BODY_KEY = "body"
RESPONSE_NODE_BODY_TYPE_KEY = "body_type"
RESPONSE_NODE_HEADERS_KEY = "headers"
RESPONSE_NODE_HEADERS_TYPE_KEY = "headers_type"
RESPONSE_NODE_ENCODING_KEY = "encoding"
RESPONSE_NODE_HISTORY_KEY = "history"
RESPONSE_NODE_COOKIES_KEY = "cookies"
RESPONSE_NODE_ELAPSED_KEY = "elapsed"
RESPONSE_NODE_REASON_KEY = "reason"
RESPONSE_NODE_URL_KEY = "url"
RESPONSE_NODE_METHOD_KEY = "method"
RESPONSE_NODE_STATUS_CODE_KEY = "status_code"

RESPONSE_NODE_KEY_EQUIVALENCE = {
    "elapsed": RESPONSE_NODE_ELAPSED_KEY,
    "url": RESPONSE_NODE_URL_KEY,
    "urls": RESPONSE_NODE_URL_KEY,
    "reason": RESPONSE_NODE_REASON_KEY,
    "reasons": RESPONSE_NODE_REASON_KEY,
    "encoding": RESPONSE_NODE_ENCODING_KEY,
    "encodings": RESPONSE_NODE_ENCODING_KEY,
    "cookie": RESPONSE_NODE_COOKIES_KEY,
    "cookies": RESPONSE_NODE_COOKIES_KEY,
    "header": RESPONSE_NODE_HEADERS_KEY,
    "headers": RESPONSE_NODE_HEADERS_KEY,
    "method": RESPONSE_NODE_METHOD_KEY,
    "methods": RESPONSE_NODE_METHOD_KEY,
    "history": RESPONSE_NODE_HISTORY_KEY,
    "historie": RESPONSE_NODE_HISTORY_KEY,
    "historys": RESPONSE_NODE_HISTORY_KEY,
    "histore": RESPONSE_NODE_HISTORY_KEY,
    "histores": RESPONSE_NODE_HISTORY_KEY,
    "histories": RESPONSE_NODE_HISTORY_KEY,
    "body_type": RESPONSE_NODE_BODY_TYPE_KEY,
    "body_types": RESPONSE_NODE_BODY_TYPE_KEY,
    "bodys_type": RESPONSE_NODE_BODY_TYPE_KEY,
    "bodies_type": RESPONSE_NODE_BODY_TYPE_KEY,
    "bodies_types": RESPONSE_NODE_BODY_TYPE_KEY,
    "header_type": RESPONSE_NODE_HEADERS_TYPE_KEY,
    "headers_type": RESPONSE_NODE_HEADERS_TYPE_KEY,
    "header_types": RESPONSE_NODE_HEADERS_TYPE_KEY,
    "headers_types": RESPONSE_NODE_HEADERS_TYPE_KEY,
    "body": RESPONSE_NODE_BODY_KEY,
    "bodys": RESPONSE_NODE_BODY_KEY,
    "bodies": RESPONSE_NODE_BODY_KEY,
    "bodie": RESPONSE_NODE_BODY_KEY,
    "status_code": RESPONSE_NODE_STATUS_CODE_KEY,
    "status_codes": RESPONSE_NODE_STATUS_CODE_KEY,
    "statuses_codes": RESPONSE_NODE_STATUS_CODE_KEY,
    "statuses_code": RESPONSE_NODE_STATUS_CODE_KEY,
    "statuss_code": RESPONSE_NODE_STATUS_CODE_KEY,
    "statuss_codes": RESPONSE_NODE_STATUS_CODE_KEY

}

# --------------------------------- Functions  ---------------------------------


def check_if_oauth_is_valid(oauth_token: str) -> bool:
    from datetime import datetime

    current_time = datetime.now().isoformat(sep="T", timespec="seconds")
    expiration = datetime.fromisoformat(oauth_token)

    if current_time >= expiration:
        return False
    return True


# -------------------- Bruteforce type conversion attempts  --------------------

BRUTEFORCE_DATETIME_FORMATS = [
    "%Y-%m-%dT%H:%M:%S.%f%z",
    "%Y-%m-%dT%H:%M:%S%z",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M:%S"
]

BRUTEFORCE_DATE_FORMATS = [
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%m/%d/%Y"
]


def detect_and_convert(value: str) -> Union[int, float, bool, None, datetime, date, str]:
    """
    Detects the type of the input string and converts it to the appropriate Python type.

    Args:
        value (str): The string to be converted.

    Returns:
        int, float, bool, None, datetime, date, or str: The converted value based on its detected type.
    """
    if isinstance(value, str) is False:
        return value
    value = value.strip()
    lvalue = value.lower()
    if lvalue == "none":
        return None
    if lvalue == "true":
        return True
    if lvalue == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass

    for fmt in BRUTEFORCE_DATETIME_FORMATS:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue

    for fmt in BRUTEFORCE_DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue

    return value
