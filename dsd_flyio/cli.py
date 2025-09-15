"""Extends the core django-simple-deploy CLI."""

import json
import shlex
import subprocess

from django_simple_deploy.management.commands.utils.plugin_utils import dsd_config
from django_simple_deploy.management.commands.utils.command_errors import (
    DSDCommandError,
)

from .plugin_config import plugin_config


class PluginCLI:

    def __init__(self, parser):
        """Add plugin-specific args."""
        group_desc = "Full documentation: https://django-simple-deploy.readthedocs.io/en/latest/quick_starts/quick_start_flyio/#customizing-the-deployment"
        plugin_group = parser.add_argument_group(
            title="Options for dsd-flyio",
            description = group_desc,
        )

        plugin_group.add_argument(
            "--vm-size",
            type=str,
            help="Name for a preset vm-size configuration on Fly.io, ie `shared-cpu-2x`.",
            default="",
        )

def validate_cli(options):
    """Validate options that were passed to CLI."""
    vm_size = options["vm_size"]
    _validate_vm_size(vm_size)


# --- Helper functions ---

def _validate_vm_size(vm_size):
    """Validate the vm size arg that was passed."""
    if not vm_size:
        return

    if not dsd_config.unit_testing:
        cmd = "fly platform vm-sizes --json"
        cmd_parts = shlex.split(cmd)
        output = subprocess.run(cmd_parts, capture_output=True)
        allowed_sizes = list(json.loads(output.stdout).keys())
    else:
        allowed_sizes = ["shared-cup-1x", "shared-cpu-2x"]

    if vm_size not in allowed_sizes:
        msg = f"The vm-size {vm_size} requested is not available."
        msg += f"\n  Allowed sizes: {' '.join(allowed_sizes)}"
        raise DSDCommandError(msg)

    # vm_size is valid.
    plugin_config.vm_size = vm_size
