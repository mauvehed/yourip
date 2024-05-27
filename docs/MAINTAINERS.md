# Maintainers Guide

This document provides a structured approach to maintaining and releasing new versions of the project, ensuring consistency and clarity in the process. If you have any further questions or need assistance, feel free to ask.

## Publish a New Version on GitHub.com

1. [Draft New Release Notes](https://github.com/mauvehed/yourIP/releases/new) on GitHub.com
1. Create a new `Tag` matching the current format (e.g. "`v0.1.5`")
1. Leave Target set to `main`
1. Set the `Release Title` to the same as the `Tag`
1. Click `Generate Release Notes`
1. Leave `Set as the latest release` checked
1. Click on `Publish Release`

## Releasing a New Version

Releases are automated via GitHub Actions. When a new tag is pushed following the format `v*.*.*`, a new release is created and the `requirements.txt` and `dev-requirements.txt` files are included.

To create a new release:

1. Update the `version` in `pyproject.toml`.
2. Push a new tag following the format `v*.*.*` (e.g., `v1.2.3`).

   ```bash
   git tag v1.2.3
   git push origin v1.2.3
   ```

## Miscellaneous Tasks

### Updating Dependencies via Poetry

```bash
poetry update
```

### Updating Supported Versions of Python

1. Update `python-version` in `.github/workflows/create-new-release.yml`
1. Update `python-version` in `.github/workflows/generate-requirements.yml`
1. Update `python-version` in `.github/workflows/mypy-linting.yml`
1. Update `python-version` in `.github/workflows/pytestts-coverage.yml`
1. Update `python-version` in `.github/workflows/sourcery.yml`
1. Update `python-version` in `.sourcery.yaml`
1. Update `tool.poetry.dependencies.python` field in pyproject.toml

### Updating `requirements.txt` and `dev-requirements.txt`

The `requirements.txt` and `dev-requirements.txt` files are automatically updated on any changes to `pyproject.toml` or `poetry.lock` via a GitHub Actions workflow.
