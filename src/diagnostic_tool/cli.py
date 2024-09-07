import click
import logging
from urllib.parse import urlparse
from .dns_checker import check_dns
from .ssl_checker import check_ssl
from .http_checker import make_request_with_different_configs

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('domain')
def check_dns_cli(domain):
    click.echo(check_dns(domain))

@cli.command()
@click.argument('domain')
def check_ssl_cli(domain):
    click.echo(check_ssl(domain))

@cli.command()
@click.argument('url')
def check_http_cli(url):
    results = make_request_with_different_configs(url)
    for config, result in results.items():
        click.echo(f"{config}: {result}")

@cli.command()
@click.argument('url')
def run_all(url):
    domain = urlparse(url).netloc
    click.echo("DNS Check:")
    click.echo(check_dns(domain))
    click.echo("\nSSL Check:")
    click.echo(check_ssl(domain))
    click.echo("\nHTTP Checks:")
    results = make_request_with_different_configs(url)
    for config, result in results.items():
        click.echo(f"{config}: {result}")

if __name__ == '__main__':
    cli()