Changelog: dsd-flyio
===

1.0 - Stable release of core django-simple-deploy
---

The stable 1.0 release of core django-simple-deploy is now available, and this project is at 1.0 to match that.

### 1.2.1

#### External changes

- Adds `--vm-size` option to CLI.
- Adds `[[vm]]` section to `fly.toml` when appropriate.
- 

#### Internal changes

- Adds `vm_size` attribute to `plugin_config` object.
- Defines `plugin_config` in `plugin_config.py`.
- Validates vm size option against `flyctl` call returning valid sizes.
- Integration test for vm-size arg.
- Test for plugin-specific output in `--help` call.

### 1.1.1

#### External changes

- N/A

#### Internal changes

- Use `secrets["name"]` instead of `secrets["Name"]` when checking for existing secrets.

### 1.1.0

#### External changes

- Specify Python 3.12 instead of 3.10 in Dockerfile.

#### Internal changes

- Update requirements; remove unneeded requirements.in file.

### 1.0.0

#### External changes

- NA

#### Internal changes

- Updated requirements.txt, for dev work.
- Add dependabot config.
  - Daily for main requirements.
  - Monthly for tests/, until tests refactored to pull version from sample_project/.

0.9 - Simplified usage from core
---

### 0.9.3

#### External changes

- Updated to match core app name change from `simple_deploy` to `django-simple-deploy`.

#### Internal changes

- Minor naming changes to make project consistent with current names in core.

### 0.9.2

#### External changes

- Use Fly.io as platform name, in logs.
- More consistent use of deploy command instead of deprecated simple_deploy command in messaging.

#### Internal changes

- Uses config instead of returning individual attributes to core.
- Simplified packaging; all setup.cfg config moved to pyproject.toml.

### 0.9.1

#### External changes

- Includes necessary templates.

#### Internal changes

- Adds required MANIFEST.in file.

### 0.9.0 (broken)

#### External changes

- (Bug) Does not include required template files.
- Success message shows updated `fly apps open` command.

#### Internal changes

- Hook implementation returns platform name.
- Simplifies packaging config.

0.8 - First use of external plugins with django-simple-deploy
---

### 0.8.4

#### External changes

- None

#### Internal changes

- Requires django-simple-deploy. This is more important for non-default plugins, but it means you can just install the plugin without having to also explicitly install django-simple-deploy.

### 0.8.3

#### External changes

- Bugfix: Includes templates dir in package.

#### Internal changes

- None

### 0.8.2

#### External changes

- Updated links in setup.cfg, for PyPI.

#### Internal changes

- None

### 0.8.1

#### External changes

- Added README and CHANGELOG.

#### Internal changes

- None

### 0.8.0

#### External changes

- Initial release.

#### Internal changes

- Initial release.