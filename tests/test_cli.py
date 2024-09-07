import pytest
from click.testing import CliRunner
from api_diagnostic_tool.cli import cli

@pytest.fixture
def runner():
    return CliRunner()

def test_check_dns_cli(runner):
    result = runner.invoke(cli, ['check-dns-cli', 'example.com'])
    assert result.exit_code == 0
    assert "Resolved to IP:" in result.output

def test_check_ssl_cli(runner):
    result = runner.invoke(cli, ['check-ssl-cli', 'example.com'])
    assert result.exit_code == 0
    assert "SSL Version:" in result.output

def test_check_http_cli(runner):
    result = runner.invoke(cli, ['check-http-cli', 'http://example.com'])
    assert result.exit_code == 0
    assert "Default:" in result.output
    assert "No SSL Verify:" in result.output
    assert "Custom User-Agent:" in result.output
    assert "Increased Timeout:" in result.output
    assert "All Options:" in result.output

def test_run_all(runner):
    result = runner.invoke(cli, ['run-all', 'http://example.com'])
    assert result.exit_code == 0
    assert "DNS Check:" in result.output
    assert "SSL Check:" in result.output
    assert "HTTP Checks:" in result.output