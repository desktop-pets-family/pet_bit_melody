"""
The file in charge of allowing the files in this folder to be run as is, without any issues
"""

import sys
try:
    from .server_main import Main, CONST
except ImportError:
    from server_main import Main, CONST

MI = Main(
    success=CONST.SUCCESS,
    error=CONST.ERROR
)
sys.exit(MI.main())
