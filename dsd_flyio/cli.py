"""Extends the core django-simple-deploy CLI."""

class PluginCLI:

    def __init__(self, parser):
        """Add plugin-specific args."""

        parser.add_argument(
            "--vm-size",
            type=str,
            help="Name for a preset vm-size configuration on Fly.io, ie `shared-cpu-2x`.",
            default="",
        )