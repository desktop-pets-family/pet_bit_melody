"""_summary_
    File in charge or referencing the boilerplate classes for the server.
"""

from .responses import BoilerplateResponses
from .incomming import BoilerplateIncoming
from .non_web import BoilerplateNonHTTP

__all__ = [
    "BoilerplateResponses",
    "BoilerplateIncoming",
    "BoilerplateNonHTTP"
]
