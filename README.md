# Flask REST API

A simple RESTful API built with Flask, Flask-RESTful, and SQLAlchemy that provides CRUD operations for user management.

## REST API Diagram

<img width="817" alt="Screenshot 2025-05-13 at 9 46 40 AM" src="https://github.com/user-attachments/assets/4786be3f-313e-4401-8752-bfbd99c93ba9" />

## Features

- Create, read, update, and delete users
- SQLite database for data persistence
- RESTful architecture
- JSON response formatting

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flask-rest-api.git
   cd flask-rest-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create the database:
   ```
   python create_db.py
   ```

5. Run the application:
   ```
   python api.py
   ```

The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users/` | GET | Get all users |
| `/api/users/` | POST | Create a new user |
| `/api/users/<id>` | GET | Get a specific user by ID |
| `/api/users/<id>` | PATCH | Update a specific user by ID |
| `/api/users/<id>` | DELETE | Delete a specific user by ID |

## Request & Response Examples

### GET /api/users/
**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com"
  }
]
```

### POST /api/users/
**Request:**
```json
{
  "name": "Alice Johnson",
  "email": "alice@example.com"
}
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com"
  },
  {
    "id": 3,
    "name": "Alice Johnson",
    "email": "alice@example.com"
  }
]
```

### GET /api/users/1
**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

### PATCH /api/users/1
**Request:**
```json
{
  "name": "John Updated",
  "email": "john.updated@example.com"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Updated",
  "email": "john.updated@example.com"
}
```

### DELETE /api/users/1
**Response:**
Status code: 204 No Content

## Project Structure

```
flask-rest-api/
├── api.py              # Main application file with API endpoints
├── create_db.py        # Script to create the database
├── example.db          # SQLite database file (created after running create_db.py)
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore file
```

## Technologies Used

- Python 3.x
- Flask 3.1.0
- Flask-RESTful 0.3.10
- Flask-SQLAlchemy 3.1.1
- SQLite

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
