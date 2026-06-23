

# Simple Math API

A beginner-friendly Python API built using the built-in `http.server` library.

## Features

- Add two numbers
- Subtract two numbers
- Multiply two numbers

## Requirements

- Python 3

No external libraries are required.

## Run the Server

```bash
python app.py
```

You should see:

```text
Server running on http://localhost:5000
```

## API Endpoints

### Add

**Request**

```http
GET /add?a=5&b=3
```

**Example**

```text
http://localhost:5000/add?a=5&b=3
```

**Response**

```json
{
  "a": 5,
  "b": 3,
  "operation": "addition",
  "result": 8
}
```

---

### Subtract

**Request**

```http
GET /subtract?a=5&b=3
```

**Example**

```text
http://localhost:5000/subtract?a=5&b=3
```

**Response**

```json
{
  "a": 5,
  "b": 3,
  "operation": "subtraction",
  "result": 2
}
```

---

### Multiply

**Request**

```http
GET /multiply?a=5&b=3
```

**Example**

```text
http://localhost:5000/multiply?a=5&b=3
```

**Response**

```json
{
  "a": 5,
  "b": 3,
  "operation": "multiplication",
  "result": 15
}
```

## Project Structure

```text
.
├── app.py
└── README.md
```

## Notes

- This project is intended for learning purposes.
- Query parameters `a` and `b` must be provided.
- The server runs on port `5000`.
````
