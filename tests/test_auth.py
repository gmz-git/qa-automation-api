import json
from pathlib import Path

import pytest

from utils.assertions import (
    assert_json_content_type,
    assert_non_empty_string,
    assert_required_keys,
    assert_status_code,
)

login_file = Path(__file__).parent.parent / "data" / "login.json"
with open(login_file, "r", encoding="utf-8") as f:
    login_payload = json.load(f)
    
login_invalid_file = Path(__file__).parent.parent / "data" / "login_invalid.json"
with open(login_invalid_file, "r", encoding="utf-8") as f:
    login_invalid_payload = json.load(f)
    

@pytest.mark.smoke
def test_login_success(client):
    resp = client.post("/api/login", json=login_payload)
    
    assert_status_code(resp, 200)
    assert_json_content_type(resp)
    
    body = resp.json()
    assert_required_keys(body, ["token"])
    assert_non_empty_string(body["token"], "token")  

@pytest.mark.regression
def test_login_missing_password(client):
    resp = client.post("/api/login", json=login_invalid_payload)

    assert_status_code(resp, 400)
    assert_json_content_type(resp)
    
    body = resp.json()
    assert_required_keys(body, ["error"])
    assert body["error"] == "Missing password"
    
    
    
    
    
    
    