import requests
import logging

logger = logging.getLogger(__name__)

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
            logger.info(f"Request successful for {url} with config {config_name}")
        except Exception as e:
            results[config_name] = f"Error: {str(e)}"
            logger.error(f"Request failed for {url} with config {config_name}: {str(e)}")

    return results