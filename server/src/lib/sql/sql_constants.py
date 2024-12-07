"""
    File in charge of storing information that is required for the sql library, but is constant.
"""

from typing import List

# initialisation arguments to remove if empty (or equal to None)
UNWANTED_ARGUMENTS = [
    "option_files"

]

# Sql sanitisation for word that can be considered as commands
RISKY_KEYWORDS: List[str] = [
    "add", "all", "alter", "analyze", "and", "as", "asc", "asensitive", "before", "between",
    "bigint", "binary", "blob", "both", "by", "call", "cascade", "case", "change", "char",
    "character", "check", "collate", "column", "condition", "constraint", "continue",
    "convert", "create", "cross", "current_date", "current_time", "current_timestamp",
    "cursor", "database", "databases", "day_hour", "day_microsecond", "day_minute",
    "day_second", "dec", "decimal", "declare", "default", "delayed", "delete", "desc",
    "describe", "deterministic", "distinct", "distinctrow", "div", "double", "drop",
    "dual", "each", "else", "elseif", "enclosed", "escaped", "exists", "exit", "explain",
    "false", "fetch", "float", "for", "force", "foreign", "from", "fulltext", "general",
    "grant", "group", "having", "high_priority", "hour_microsecond", "hour_minute",
    "hour_second", "if", "ignore", "in", "index", "infile", "inner", "inout",
    "insensitive", "insert", "int", "integer", "interval", "into", "is", "iterate", "join",
    "key", "keys", "kill", "leading", "leave", "left", "like", "limit", "linear", "lines",
    "load", "localtime", "localtimestamp", "lock", "long", "longblob", "longtext", "loop",
    "low_priority", "master_ssl_verify_server_cert", "match", "maxvalue", "mediumblob",
    "mediumint", "mediumtext", "middleint", "minute_microsecond", "minute_second", "mod",
    "modifies", "natural", "not", "no_write_to_binlog", "null", "numeric", "on", "optimize",
    "option", "optionally", "or", "order", "out", "outer", "outfile", "precision", "primary",
    "procedure", "purge", "range", "read", "reads", "read_write", "real", "references",
    "regexp", "release", "rename", "repeat", "replace", "require", "resignal", "restrict",
    "return", "revoke", "right", "rlike", "schema", "schemas", "second_microsecond",
    "select", "sensitive", "separator", "set", "show", "signal", "smallint", "spatial",
    "specific", "sql", "sqlexception", "sqlstate", "sqlwarning", "sql_big_result",
    "sql_calc_found_rows", "sql_small_result", "ssl", "starting", "stored", "straight_join",
    "table", "terminated", "then", "tinyblob", "tinyint", "tinytext", "to", "trailing",
    "trigger", "true", "undo", "union", "unique", "unlock", "unsigned", "update", "usage",
    "use", "using", "utc_date", "utc_time", "utc_timestamp", "values", "varbinary",
    "varchar", "varcharacter", "varying", "virtual", "when", "where", "while", "with",
    "write", "xor", "year_month", "zerofill"
]

KEYWORD_LOGIC_GATES: List[str] = [
    'and', 'or', 'not', 'xor', 'between', 'in', 'is', 'like', 'regexp', 'rlike', 'null', 'true', 'false', 'exists',
    'distinct', 'limit', 'having', 'join', 'union', 'current_date', 'current_time', 'current_timestamp', 'utc_date',
    'utc_time', 'utc_timestamp', 'mod', 'if'
]


DATE_ONLY: str = '%Y-%m-%d'

DATE_AND_TIME: str = '%Y-%m-%d %H:%M:%S'

# Error messages
CONNECTION_FAILED: str = "Connection to the database is non-existant, aborting command."

CURSOR_FAILED: str = "Cursor to the database is non-existant, aborting command."

# Specific error codes
GET_TABLE_SIZE_ERROR: int = (-1)
