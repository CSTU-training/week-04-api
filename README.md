# Book Tracker API

Week 3 Lab — CSE 552 Fullstack Software Development in the Age of AI Agents

A REST API built with **FastAPI** and **Pydantic** for tracking books you've read, are reading, or want to read. Data is stored in-memory (no database yet — that's Week 4).

---

## Tech Stack

- Python 3
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic v2](https://docs.pydantic.dev/)
- Uvicorn (ASGI server)

---

## Setup

```bash
# Clone and enter the project
cd week-03-api

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.
Interactive docs (Swagger UI) at `http://localhost:8000/docs`.

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/books` | List all books (optional `?status=` filter) |
| GET | `/books/stats` | Summary statistics |
| GET | `/books/{id}` | Get a single book |
| POST | `/books` | Create a new book |
| PUT | `/books/{id}` | Update a book's status or rating |
| DELETE | `/books/{id}` | Delete a book |

### Query Parameters

- `GET /books?status=reading` — filter by status (`reading`, `read`, `want_to_read`)

### Book Schema

```json
{
  "title": "Dune",
  "author": "Frank Herbert",
  "status": "read",
  "rating": 5
}
```

- `status`: `"want_to_read"` (default) | `"reading"` | `"read"`
- `rating`: `1–5`, optional (typically set when status is `"read"`)

### Stats Response

```json
{
  "total": 3,
  "by_status": {
    "want_to_read": 1,
    "reading": 1,
    "read": 1
  },
  "average_rating": 4.5
}
```

---

## Example Usage

```bash
# Add a book
curl -X POST http://localhost:8000/books \
  -H "Content-Type: application/json" \
  -d '{"title": "Dune", "author": "Frank Herbert", "status": "read", "rating": 5}'

# List all books
curl http://localhost:8000/books

# Filter by status
curl http://localhost:8000/books?status=reading

# Update a book
curl -X PUT http://localhost:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "read", "rating": 4}'

# Delete a book
curl -X DELETE http://localhost:8000/books/1

# Get stats
curl http://localhost:8000/books/stats
```

---

## Project Structure

```
week-03-api/
├── main.py           # FastAPI app and all endpoints
├── requirements.txt  # Python dependencies
└── reflection.md     # Week 3 reflection answers
```

---

## Notes

- Data is stored in-memory (`books_db` list). All data is lost on server restart.
- `/books/stats` is registered **before** `/books/{id}` in the router so FastAPI doesn't interpret `"stats"` as an integer book ID.
- Week 4 will replace in-memory storage with PostgreSQL + SQLAlchemy.
