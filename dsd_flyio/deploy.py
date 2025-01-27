"""Manages all Fly.io-specific aspects of the deployment process.

Notes:
- Internal references to Fly.io will almost always be flyio. Public references, may be fly_io.
- self.deployed_project_name and self.app_name are identical. The first is used in the
  simple_deploy CLI, but Fly refers to "apps" in their docs. This redundancy makes it
  easier to code Fly CLI commands.
"""

import django_simple_deploy

from dsd_flyio.platform_deployer import PlatformDeployer
from .plugin_config import PluginConfig


@django_simple_deploy.hookimpl
def dsd_get_plugin_config():
    """Get platform-specific attributes needed by core."""
    plugin_config = PluginConfig()
    return plugin_config


@django_simple_deploy.hookimpl
def dsd_deploy():
    """Carry out platform-specific deployment steps."""
    platform_deployer = PlatformDeployer()
    platform_deployer.deploy()
