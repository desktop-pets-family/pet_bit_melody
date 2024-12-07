"""
The file to export every endpoints class
"""

from .bonus import Bonus
from .user_endpoints import UserEndpoints
from .applets import Applets
from .project import Project
from .edit import Edit

__all__ = [
    "Bonus",
    "Applets",
    "Project",
    "UserEndpoints",
    "Edit"
]
