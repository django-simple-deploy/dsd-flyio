"""Helper functions specific to Fly.io."""

import re, time
import json
import subprocess
import sys

from tests.e2e_tests.utils.it_helper_functions import make_sp_call


def create_project():
    """Create a project on Fly.io."""
    print("\n\nCreating a project on Fly.io...")
    create_cmd = "fly apps create --generate-name"
    if sys.platform == "linux":
        output = (
            subprocess.run(create_cmd, capture_output=True, shell=True)
            .stdout.decode()
            .strip()
        )
    else:
        output = make_sp_call(create_cmd, capture_output=True).stdout.decode().strip()
    print("create_project output:", output)

    re_app_name = r"New app created: (.*)"
    app_name = re.search(re_app_name, output).group(1)
    print(f"  App name: {app_name}")

    return app_name


def deploy_project(app_name):
    """Make a non-automated deployment."""
    # Consider pausing before the deployment. Some platforms need a moment
    #   for the newly-created resources to become fully available.
    # time.sleep(30)

    print("Deploying to Fly.io...")
    if sys.platform == "linux":
        subprocess.run("fly deploy", shell=True)
    else:
        make_sp_call("fly deploy")

    # Open project and get URL.
    open_cmd = f"fly apps open -a {app_name}"
    if sys.platform == "linux":
        output = (
            subprocess.run(open_cmd, capture_output=True, shell=True)
            .stdout.decode()
            .strip()
        )
    else:
        output = make_sp_call(open_cmd, capture_output=True).stdout.decode().strip()
    print("fly open output:", output)

    re_url = r"opening (http.*) \.\.\."
    project_url = re.search(re_url, output).group(1)
    if "https" not in project_url:
        project_url = project_url.replace("http", "https")

    print(f"  Project URL: {project_url}")

    return project_url


def get_project_url_name():
    """Get project URL and app name of a deployed project.
    This is used when testing the automate_all workflow.
    """
    status_cmd = "fly status --json"
    if sys.platform == "linux":
        output = (
            subprocess.run(status_cmd, capture_output=True, shell=True)
            .stdout.decode()
            .strip()
        )
    else:
        output = (
            make_sp_call("fly status --json", capture_output=True)
            .stdout.decode()
            .strip()
        )
    status_json = json.loads(output)

    app_name = status_json["Name"]
    project_url = f"https://{app_name}.fly.dev"

    print(f"  Found app name: {app_name}")
    print(f"  Project URL: {project_url}")

    return project_url, app_name


def check_log(tmp_proj_dir):
    """Check the log that was generated during a full deployment.

    Checks that log file exists, and that DATABASE_URL is not logged.
    """
    path = tmp_proj_dir / "dsd_logs"
    if not path.exists():
        return False

    log_files = list(path.glob("dsd_*.log"))
    if not log_files:
        return False

    log_str = log_files[0].read_text()
    if "DATABASE_URL" in log_str:
        return False

    return True


def destroy_project(request):
    """Destroy the deployed project, and all remote resources."""
    print("\nCleaning up:")

    app_name = request.config.cache.get("app_name", None)
    if not app_name:
        print("  No app name found; can't destroy any remote resources.")
        return None

    destroy_app_cmd = f"fly apps destroy -y {app_name}"
    destroy_db_cmd = f"fly apps destroy -y {app_name}-db"
    print("  Destroying Fly.io project...")
    if sys.platform == "linux":
        subprocess.run(destroy_app_cmd, shell=True)
    else:
        make_sp_call(destroy_app_cmd)

    print("  Destroying Fly.io database...")
    if sys.platform == "linux":
        subprocess.run(destroy_db_cmd, shell=True)
    else:
        make_sp_call(destroy_db_cmd)
