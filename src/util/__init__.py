from .db_connection import get_db
from datetime import datetime
from typing import Any, Dict, Optional

__all__ = [
    'get_db',
    'get_timestamp',
    'validate_entity',
    'create_error_response'
]

__version__ = '0.1.0'

def get_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.utcnow().isoformat()

def validate_entity(data: Dict[str, Any], required_fields: list) -> Optional[str]:
    """
    Validate if all required fields are present in the data.
    
    Args:
        data: Dictionary containing entity data
        required_fields: List of required field names
        
    Returns:
        Error message if validation fails, None otherwise
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return f"Missing required fields: {', '.join(missing_fields)}"
    return None

def create_error_response(message: str, code: int = 400) -> Dict[str, Any]:
    """
    Create a standardized error response.
    
    Args:
        message: Error message
        code: HTTP status code
        
    Returns:
        Dictionary containing error details
    """
    return {
        "error": message,
        "code": code,
        "timestamp": get_timestamp()
    }