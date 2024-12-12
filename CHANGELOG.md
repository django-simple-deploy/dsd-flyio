Changelog: dsd-flyio
===

0.9 - Simplified usage from core
---

### 0.9.2 (unreleased)

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