"""
The file to export every endpoints class
"""

from .bonus import Bonus
from .user_endpoints import UserEndpoints
from .applets import Applets

__all__ = [
    "Bonus",
    "UserEndpoints",
    "Applets"
]
