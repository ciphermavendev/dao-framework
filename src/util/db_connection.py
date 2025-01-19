from contextlib import contextmanager
from ..config.database import SessionLocal

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()