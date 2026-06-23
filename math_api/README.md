# Simple Python Math API demo

A very simple API using Python’s built-in HTTP server to perform basic math operations when two parameters are specified

## What it does

You can:
- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers

## ToRun it

```bash
python math_basic_api.py
````

Server runs at:

```
http://localhost:1234
```

## Sample calls

### Add

```
http://localhost:1234/add?a=5&b=3
```

### Subtract

```
http://localhost:1234/subtract?a=5&b=3
```

### Multiply

```
http://localhost:1234/multiply?a=5&b=3
```

## Example result

```json
{"message": "The result of dividing 5 and 3 is 1.6666666666666667."}
{"message": "The result of adding 5 and 3 is 8."}
{"message": "The result of multiplying 5 and 3 is 15."}
{"message": "The result of subtracting 5 and 3 is 2."}

```

 

