import pytest
from api_diagnostic_tool.ssl_checker import check_ssl

def test_check_ssl_success():
    result = check_ssl("example.com")
    assert "SSL Version:" in result

def test_check_ssl_failure():
    result = check_ssl("nonexistent.example.com")
    assert "SSL connection failed:" in result