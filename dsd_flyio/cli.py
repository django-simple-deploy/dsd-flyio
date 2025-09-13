"""Extends the core django-simple-deploy CLI."""

import json
import shlex
import subprocess

from django_simple_deploy.management.commands.utils.command_errors import (
    DSDCommandError,
)


class PluginCLI:

    def __init__(self, parser):
        """Add plugin-specific args."""

        parser.add_argument(
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
    cmd = "fly platform vm-sizes --json"
    cmd_parts = shlex.split(cmd)
    output = subprocess.run(cmd_parts, capture_output=True)
    allowed_sizes = list(json.loads(output.stdout).keys())

    if vm_size and vm_size not in allowed_sizes:
        msg = f"The vm-size {vm_size} requested is not available."
        msg += f"\n  Allowed sizes: {' '.join(allowed_sizes)}"
        raise DSDCommandError(msg)