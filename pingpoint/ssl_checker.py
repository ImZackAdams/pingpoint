import ssl
import socket
import logging

logger = logging.getLogger(__name__)

def check_ssl(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:
                version = secure_sock.version()
        logger.info(f"SSL connection successful for {domain}")
        return f"SSL Version: {version}"
    except Exception as e:
        logger.error(f"SSL connection failed for {domain}: {str(e)}")
        return f"SSL connection failed: {str(e)}"