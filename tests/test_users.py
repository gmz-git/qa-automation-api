import json
from pathlib import Path

import pytest

from utils.assertions import (
    assert_json_content_type,
    assert_non_empty_string,
    assert_positive_int,
    assert_required_keys,
    assert_status_code,
)


data_file = Path(__file__).parent.parent / "data" / "users_pages.json"
with open(data_file, "r", encoding="utf-8") as f:
    users_test_data = json.load(f)
pages = users_test_data["pages"]


create_user_file = Path(__file__).parent.parent / "data" / "create_user.json"
with open(create_user_file, "r", encoding="utf-8") as f:
    create_user_payload = json.load(f)
        
'''    
login_file = Path(__file__).parent.parent / "data" / "login.json"

with open(login_file, "r", encoding="utf-8") as f:
    login_payload = json.load(f)


login_invalid_file = Path(__file__).parent.parent / "data" / "login_invalid.json"

with open(login_invalid_file, "r", encoding="utf-8") as f:
    login_invalid_payload = json.load(f)
    
'''
@pytest.mark.smoke
@pytest.mark.parametrize("page", pages)
def test_get_users_success(client, page):
    resp = client.get("/api/users", params={"page": page})

    assert_status_code(resp, 200)
    assert_json_content_type(resp)

    body = resp.json()
    assert_required_keys(body, ["page", "per_page", "total", "total_pages", "data"])
    
    assert body["page"] == page
    assert_positive_int(body["per_page"], "per_page")
    assert_positive_int(body["total"], "total")
    assert_positive_int(body["total_pages"], "total_pages")
    
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0
    assert len(body["data"]) <= body["per_page"]
    assert body["total_pages"] >= page

    for user in body["data"]:
        assert_required_keys(
            user,
            ["id", "email", "first_name", "last_name", "avatar" ]
        )
        assert_positive_int(user["id"], "id")
        assert_non_empty_string(user["email"], "email")
        assert_non_empty_string(user["first_name"], "first_name")
        assert_non_empty_string(user["last_name"], "last_name")
        assert_non_empty_string(user["avatar"], "avatar")
        
        assert "@" in user["email"]
        assert user["avatar"].startswith("http")

@pytest.mark.regression
def test_get_single_user_not_found(client):
    resp = client.get("/api/users/23")
    assert resp.status_code == 404

@pytest.mark.regression
def test_get_unknown_resource_not_found(client):
    resp = client.get("/api/unknown/23")
    assert resp.status_code == 404

@pytest.mark.regression
def test_create_user_success(client):
    resp = client.post("/api/users", json=create_user_payload)

    assert_status_code(resp, 201)
    assert_json_content_type(resp)

    body = resp.json()
    assert_require_keys(body, ["name", "job", "id", "createdAt"])

    assert body["name"] == create_user_payload["name"]
    assert body["job"] == create_user_payload["job"]
    assert_non_empty_string(body["id"], "id")
    assert_non_empty_string(body["createdAt"], "createdAt")
    assert "T" in body["createdAt"]
    
'''    
def test_login_success(client):
    resp = client.post("/api/login", json=login_payload)

    assert resp.status_code == 200

    body = resp.json()

    assert "token" in body
    assert isinstance(body["token"], str)
    assert len(body["token"]) > 0

def test_login_missing_password(client):
    resp = client.post("/api/login", json=login_invalid_payload)

    assert resp.status_code == 400

    body = resp.json()

    assert "error" in body
'''