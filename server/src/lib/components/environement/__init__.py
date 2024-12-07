"""
This module contains the environment variables for the application.
"""

from .secrets import Secrets
from .variables import Variables


class Environment:
    """The environment variables for the application."""
    Secrets = Secrets
    Variables = Variables
