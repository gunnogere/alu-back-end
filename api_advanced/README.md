# API Advanced

This project focuses on interacting with the Reddit API using Python. It introduces advanced API concepts such as pagination, recursive data retrieval, JSON parsing, and data processing. The tasks demonstrate how to consume RESTful APIs efficiently while adhering to Python best practices and project constraints.

## Learning Objectives

By the end of this project, you should be able to:

* Read API documentation and identify the appropriate endpoints for a task.
* Use APIs that implement pagination.
* Parse and process JSON responses from an API.
* Make recursive API calls to retrieve complete datasets.
* Sort dictionaries by their values.
* Handle API errors and invalid resources gracefully.
* Work with HTTP requests using the Python Requests module.

## Project Tasks

### 0. Subs

Create a function that queries the Reddit API and returns the total number of subscribers for a given subreddit.

### 1. Top Ten

Create a function that prints the titles of the first ten hot posts listed for a subreddit.

### 2. Recurse It!

Create a recursive function that retrieves and returns the titles of all hot articles for a given subreddit by following Reddit's pagination.

### 3. Count It!

Create a recursive function that parses the titles of hot articles and counts occurrences of specified keywords, printing the results sorted by frequency and alphabetically when counts are equal.

## Requirements

* Python 3.4.3
* Ubuntu 14.04 LTS
* Requests module for HTTP requests
* PEP 8 compliant code
* Executable Python scripts
* Proper module documentation
* Recursive solutions where required
* Custom User-Agent headers for Reddit API requests
* No redirect following for invalid subreddit validation

## Repository Structure

```text
api_advanced/
├── 0-subs.py
├── 1-top_ten.py
├── 2-recurse.py
├── 3-count.py
└── README.md
```

## Key Concepts

* REST APIs
* HTTP Requests
* JSON Parsing
* API Pagination
* Recursion
* Data Aggregation
* Dictionary Sorting
* Error Handling

## Author

Developed as part of the ALU Scripting curriculum.
