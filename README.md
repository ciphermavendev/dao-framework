# DAO Framework

A robust and type-safe Data Access Object (DAO) framework for Python applications.

## Features

- Generic DAO implementation for any model
- Type-safe database operations
- Connection pooling and management
- Environment-based configuration
- Comprehensive testing suite
- Database migration support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dao-framework.git
cd dao-framework
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your database:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

## Usage

```python
from src.dao import UserDAO
from src.util.db_connection import get_db

# Create a user
user_dao = UserDAO()
with get_db() as db:
    new_user = user_dao.create(
        db,
        username="john_doe",
        email="john@example.com"
    )
```

## Project Structure

```
dao-framework/
├── src/
│   ├── config/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── dao/
│   │   ├── __init__.py
│   │   ├── base_dao.py
│   │   └── user_dao.py
│   ├── model/
│   │   ├── __init__.py
│   │   └── user.py
│   └── util/
│       ├── __init__.py
│       └── db_connection.py
├── tests/
├── .env
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Testing

Run tests using pytest:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request