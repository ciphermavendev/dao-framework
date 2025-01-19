from .user import User, Base

__all__ = [
    'User',
    'Base',
]

# Version of the model package
__version__ = '0.1.0'

# Model metadata
MODEL_METADATA = {
    'User': {
        'table_name': 'users',
        'indices': ['username', 'email'],
        'relationships': []
    }
}

# Initialize models
def init_models(engine):
    """Initialize all models in the database."""
    Base.metadata.create_all(bind=engine)
    
def drop_models(engine):
    """Drop all models from the database."""
    Base.metadata.drop_all(bind=engine)