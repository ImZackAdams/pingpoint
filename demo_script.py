import socket
import ssl
import urllib.parse
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_dns(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return f"Resolved to IP: {ip_address}"
    except socket.gaierror as e:
        return f"DNS resolution failed: {str(e)}"


def check_ssl(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:
                return secure_sock.version()
    except Exception as e:
        return f"SSL connection failed: {str(e)}"


def make_request_with_different_configs(url):
    configs = [
        ("Default", {}),
        ("No SSL Verify", {"verify": False}),
        ("Custom User-Agent", {"headers": {"User-Agent": "CustomBot/1.0"}}),
        ("Increased Timeout", {"timeout": 30}),
        ("All Options", {"verify": False, "headers": {"User-Agent": "CustomBot/1.0"}, "timeout": 30})
    ]

    results = {}
    for config_name, config in configs:
        try:
            response = requests.get(url, **config)
            results[config_name] = f"Status: {response.status_code}, Content: {response.text[:100]}..."
        except Exception as e:
            results[config_name] = f"Error: {str(e)}"

    return results


def diagnose_api_issues(url):
    logger.info(f"Diagnosing issues for URL: {url}")

    # Parse the domain from the URL
    domain = urllib.parse.urlparse(url).netloc

    # Check DNS
    logger.info("Checking DNS...")
    dns_result = check_dns(domain)
    logger.info(f"DNS result: {dns_result}")

    # Check SSL
    logger.info("Checking SSL...")
    ssl_result = check_ssl(domain)
    logger.info(f"SSL result: {ssl_result}")

    # Make requests with different configurations
    logger.info("Making requests with different configurations...")
    request_results = make_request_with_different_configs(url)
    for config, result in request_results.items():
        logger.info(f"{config}: {result}")

    return {
        "dns": dns_result,
        "ssl": ssl_result,
        "requests": request_results
    }


if __name__ == "__main__":
    test_url = "http://www.baseball-reference.com/teams/ARI/2024-schedule-scores.shtml"
    results = diagnose_api_issues(test_url)
    print(results)