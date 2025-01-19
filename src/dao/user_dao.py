from typing import Optional
from sqlalchemy.orm import Session
from .base_dao import BaseDAO
from ..model.user import User

class UserDAO(BaseDAO[User]):
    def __init__(self):
        super().__init__(User)
    
    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()
    
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()