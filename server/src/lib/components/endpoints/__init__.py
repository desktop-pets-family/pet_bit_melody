"""
The file to export every endpoints class
"""

from .bonus import Bonus
from .services import Services
from .user_endpoints import UserEndpoints
from .mandatory import Mandatory
from .applets import Applets

__all__ = [
    "Bonus",
    "Services",
    "Mandatory",
    "UserEndpoints",
    "Applets"
]
