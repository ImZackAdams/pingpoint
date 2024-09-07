import socket
import logging

logger = logging.getLogger(__name__)

def check_dns(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        logger.info(f"DNS resolution successful for {domain}")
        return f"Resolved to IP: {ip_address}"
    except socket.gaierror as e:
        logger.error(f"DNS resolution failed for {domain}: {str(e)}")
        return f"DNS resolution failed: {str(e)}"