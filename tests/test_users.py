'''import os
import requests

BASE_URL = "https://reqres.in"
API_KEY = os.getenv("REQRES_API_KEY")

def _headers():
    return{"x-api-key": API_KEY} if API_KEY else {}
    
def test_get_users_success():
    url = f"{BASE_URL}/api/users"
    resp = requests.get(
        url,
        params={"page": 2},
        headers=_headers(),
        timeout=10
    )
    
    assert resp.status_code == 200
    
    content_type = resp.headers.get("Content-Type","")
    assert "application/json" in content_type
    
    body = resp.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0
    
    for k in ["page", "per_page", "total", "total_pages"]:
        assert k in body
        
    user0 = body["data"][0]
    for k in ["id", "email", "first_name", "last_name", "avatar"]:
        assert k in user0
        
    assert "@" in user0["email"]
    '''

'''
def test_get_users_success(base_url, headers, session):
    url = f"{base_url}/api/users"
    resp = session.get(
        url,
        params={"page": 2},
        headers=headers,
        timeout=10,
    )
     
     
    assert resp.status_code == 200

    content_type =resp.headers.get("Content-Type","")
    assert "application/json" in content_type


    body = resp.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


    for k in ["page", "per_page", "total", "total_pages"]:
        assert k in body

    user0 = body["data"][0]
    for k in ["id", "email", "first_name", "last_name", "avatar"]:
        assert k in user0

    assert "@" in user0["email"]    
'''

import pytest

@pytest.mark.parametrize("page",[1,2])
def test_get_users_success(base_url, headers,session, page):
    url = f"{base_url}/api/users"
    resp = session.get(
        url,
        params = {"page": page},
        headers = headers,
        timeout = 10,
    )    
    
    assert resp.status_code == 200
    
    content_type = resp.headers.get("Content-Type", "")
    assert "application/json" in content_type
    
    
    body = resp.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0
    
    for k in ["page", "per_page", "total", "total_pages"]:
        assert k in body
    
    user0 = body["data"][0]
    for k in ["id", "email", "first_name", "last_name", "avatar"]:
        assert k in user0
        
    assert "@" in user0["email"]
    