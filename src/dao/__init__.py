from .base_dao import BaseDAO
from .user_dao import UserDAO

__all__ = [
    'BaseDAO',
    'UserDAO',
]

# Version of the DAO package
__version__ = '0.1.0'

# Initialize default DAOs
default_user_dao = UserDAO()
