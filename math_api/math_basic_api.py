from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

class API_Main(BaseHTTPRequestHandler):
    def do_GET(self):      
        url_parts = urlparse(self.path)  # Parse URL into dictionary 
        params = parse_qs(url_parts.query) #get queries passed in api call

        a = int(params["a"][0])
        b = int(params["b"][0])

        # Map endpoints to mehtods defined above
        operations = {
            "/add": ("adding", add),
            "/subtract": ("subtracting", subtract),
            "/multiply": ("multiplying", multiply),
            "/divide": ("dividing", divide),
        }

        if url_parts.path in operations:
            operation_name, func = operations[url_parts.path]
            answer = func(a, b)

            result = {
                "message": f"The result of {operation_name} {a} and {b} is {answer}."
            }
        else:
            result = {
                "error": "Invalid endpoint"
            }

        # Send JSON response
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(result).encode())

# Start server
server = HTTPServer(("localhost", 1234), API_Main)

print("Server running on http://localhost:1234")
server.serve_forever()