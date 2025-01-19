from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta

T = TypeVar('T', bound=DeclarativeMeta)

class BaseDAO(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model
    
    def create(self, db: Session, **kwargs) -> T:
        instance = self.model(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance
    
    def get_by_id(self, db: Session, id: int) -> Optional[T]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, db: Session) -> List[T]:
        return db.query(self.model).all()
    
    def update(self, db: Session, id: int, **kwargs) -> Optional[T]:
        instance = self.get_by_id(db, id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            db.commit()
            db.refresh(instance)
        return instance
    
    def delete(self, db: Session, id: int) -> bool:
        instance = self.get_by_id(db, id)
        if instance:
            db.delete(instance)
            db.commit()
            return True
        return False
