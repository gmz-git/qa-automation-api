#QA Automation API

This is a practice API automation project build with Python, pytest, and requests.
The goal of this project is to build a small but structured API test framework step by step, including positive tests, negative tests, reusable fixtures, and parameterized tests.

## Tech Stack

-Python
-pytest
-requests
-Git / GitHub

## Project Structure
qa-automation-api/
- tests/
  - conftest.py
  - test_smoke.py
  - test_user.py
- README.md

## How to Run
1. Activate the virtual environment
.\.venv\Scripts\Activate.ps1

2. Run all tests
pytest -vv

3 Run only the user-related tests
pytest -k get_users -vv

## Current Test Coverage.
1. Smoke test
   - basic pytest smoke check
 
2. Positive API tests  
   - get user list successfully
   - validate JSON structure and key fields
   - test multiple pages with parameterizd input

3. Negative API tests
   - get single user with nonexistent id returns 404
   - get unknown resource returns 404
   
# Notes
This project is being built incrementally as part of a learning plan for API automation and test framework development