"""Manages all Fly.io-specific aspects of the deployment process.

Notes:
- Internal references to Fly.io will almost always be flyio. Public references, may be fly_io.
- self.deployed_project_name and self.app_name are identical. The first is used in the
  simple_deploy CLI, but Fly refers to "apps" in their docs. This redundancy makes it
  easier to code Fly CLI commands.
"""

import django_simple_deploy

from dsd_flyio.platform_deployer import PlatformDeployer
# from .plugin_config import PluginConfig
from .plugin_config import plugin_config
from .cli import PluginCLI, validate_cli


@django_simple_deploy.hookimpl
def dsd_get_plugin_config():
    """Get platform-specific attributes needed by core."""
    return plugin_config

@django_simple_deploy.hookimpl
def dsd_get_plugin_cli(parser):
    """Get plugin's CLI extension."""
    plugin_cli = PluginCLI(parser)


@django_simple_deploy.hookimpl
def dsd_validate_cli(options):
    """Validate and parse plugin-specific CLI args."""
    validate_cli(options)


@django_simple_deploy.hookimpl
def dsd_deploy():
    """Carry out platform-specific deployment steps."""
    platform_deployer = PlatformDeployer()
    platform_deployer.deploy()
