# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change. Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Development environment setup

> **[TODO]**
> Proceed to describe how to setup local development environment.
> e.g:

To set up a development environment, please follow these steps:

1. Clone the repo

   ```sh
   git clone https://github.com/mauvehed/yourip
   ```

2. TODO

## Testing locally

Please utilize the `debug.sh` script to run a local copy of the app. This will execute and bind to localhost on port 80

## Issues and feature requests

You've found a bug in the source code, a mistake in the documentation or maybe you'd like a new feature?  You can help us by [submitting an issue on GitHub](https://github.com/mauvehed/yourip/issues). Before you create an issue, make sure to search the issue archive -- your issue may have already been addressed!

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

**Even better: Submit a pull request with a fix or new feature!**

### How to submit a Pull Request

1. Search our repository for open or closed
   [Pull Requests](https://github.com/mauvehed/yourip/pulls)
   that relate to your submission. You don't want to duplicate effort.
2. Fork the project
3. Create your feature branch (`git checkout -b feat/amazing_feature`)
4. Commit your changes (`git commit -m 'feat: add amazing_feature'`) yourIP uses [conventional commits](https://www.conventionalcommits.org), so please follow the specification in your commit messages.
5. Push to the branch (`git push origin feat/amazing_feature`)
6. [Open a Pull Request](https://github.com/mauvehed/yourip/compare?expand=1)

## Maintainers

This document is intended to assist the maintainers of this repository and software package with various tasks.

### Miscellaneous tasks

#### Updating dependencies via poetry

```bash
poetry update
```

#### Updating supported versions of python

##### Update GitHub Actions

1. Update `python-version` in `.github/workflows/pylint.yml`
2. Update `python-version` in `.github/workflows/sourcery.yml`
3. Update `python-version` in `.sourcery.yaml`

##### Update pyproject.toml

Update the tool.poetry.dependencies.python field in `pyproject.toml`

#### Updating requirements.txt

```bash
poetry export --without-hashes -f requirements.txt --output requirements.txt
```

### Releasing a new version

#### Update all the things

1. Update dependencies via `Updating dependencies via poetry` above
2. Update requirements.txt via `Updating requirements.txt` above
3. Update the value of `version` in pyproject.toml to match the new release number
4. Push a new branch for the release
5. Merge branch
6. Proceed to `Publish a new version on Github.com` below

#### Publish a new version on Github.com

1. [Draft New Release Notes](https://github.com/mauvehed/trackerstatus/releases/new) on Github.com
2. Create a new `Tag` matching the current format (e.g. "v0.1.5")
3. Leave Target set to `main``
4. Set the `Release Title` to the same as the `Tag`
5. Click `Generate Release Notes`
6. Leave `Set as the latest release` checked
7. Click on `Publish Release`
