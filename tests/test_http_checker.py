import pytest
from api_diagnostic_tool.http_checker import make_request_with_different_configs

def test_make_request_with_different_configs():
    results = make_request_with_different_configs("http://example.com")
    assert len(results) == 5  # We expect 5 different configurations
    assert "Default" in results
    assert "No SSL Verify" in results
    assert "Custom User-Agent" in results
    assert "Increased Timeout" in results
    assert "All Options" in results

def test_make_request_with_different_configs_failure():
    results = make_request_with_different_configs("http://nonexistent.example.com")
    assert all("Error:" in result for result in results.values())