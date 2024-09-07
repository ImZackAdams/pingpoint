import pytest
from api_diagnostic_tool.dns_checker import check_dns

def test_check_dns_success():
    result = check_dns("example.com")
    assert "Resolved to IP:" in result

def test_check_dns_failure():
    result = check_dns("nonexistent.example.com")
    assert "DNS resolution failed:" in result