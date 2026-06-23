# Simple Math API (Python)

A very simple API using Python’s built-in HTTP server.

## What it does

You can:
- Add two numbers
- Subtract two numbers
- Multiply two numbers

## Run it

```bash
python app.py
````

Server runs at:

```
http://localhost:5000
```

## How to use

### Add

```
/add?a=5&b=3
```

### Subtract

```
/subtract?a=5&b=3
```

### Multiply

```
/multiply?a=5&b=3
```

## Example result

```json
{
  "a": 5,
  "b": 3,
  "operation": "addition",
  "result": 8
}
```

## Note

* You must provide `a` and `b`
* Only for learning

```

