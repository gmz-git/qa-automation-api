def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {response.status_code}. "
        f"Response body: {response.text}"
    )
    
def assert_json_content_type(response):
    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type, (
        f"Expected JSON reponse, but got Content-Type={content_type}"
    )

def assert_required_keys(data, required_keys):
    for key in required_keys:
        assert key in data, (
            f"Missing key  '{key}'. Actual keys: {list(data.keys())}"
        )
    
def assert_non_empty_string(value, field_name):
    assert isinstance(value, str), (
        f"{field_name} should be str, got {type(value).__name__}"
    )
    assert value.strip()!="", f"{field_name} should not be empty"  

def assert_positive_int(value, field_name):
    assert isinstance(value, int), (
        f"{field_name} should be int, got {type(value).__name__}"
    )
    assert value > 0, f"{field_name} should be >0, got {value}"    