import json
from pathlib import Path

import pytest


data_file = Path(__file__).parent.parent / "data" / "users_pages.json"

with open(data_file, "r", encoding="utf-8") as f:
    users_test_data = json.load(f)

pages = users_test_data["pages"]


@pytest.mark.parametrize("page", pages)
def test_get_users_success(client, page):
    resp = client.get("/api/users", params={"page": page})

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


def test_get_single_user_not_found(client):
    resp = client.get("/api/users/23")
    assert resp.status_code == 404


def test_get_unknown_resource_not_found(client):
    resp = client.get("/api/unknown/23")
    assert resp.status_code == 404