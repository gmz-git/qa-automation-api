import os
import pytest
import requests

@pytest.fixture
def base_url():
    return "https://reqres.in"
    
    
@pytest.fixture
def api_key():
    return os.getenv("REQRES_API_KEY")
    
@pytest.fixture
def headers(api_key):
    return {"x-api-key": api_key} if api_key else {}
    
@pytest.fixture
def session():
    return requests.Session()
    