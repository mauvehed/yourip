# Contributing Guidelines

Welcome! We're excited that you're interested in contributing to this project. Below are guidelines to help you get started.

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change. Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Table of Contents

1. Getting Started
2. Testing Locally
3. Running Tests
4. Code Coverage
5. Continuous Integration
6. Submitting Changes

## Getting Started

1. Fork the repository.
2. Clone your fork:

```bash
git clone https://github.com/your-username/yourIP.git
```

3. Install dependencies using Poetry:

```bash
poetry install --with dev
```

## Testing Locally

To test the application locally:

1. Activate the virtual environment:

```bash
poetry shell
```

2. Run the Flask app:

```bash
flask --app app/main.py --debug run --host 127.0.0.1
```

3. Visit <http://127.0.0.1:5000> in your browser.

## Running Tests

We use pytest for testing. To run tests:

1. Ensure you're in the virtual environment:

```bash
poetry shell
```

2. Run the tests:

```bash
pytest
```

## Code Coverage

We use coverage.py to measure code coverage. To generate a coverage report:

1. Run the tests with coverage:

```bash
coverage run -m pytest
```

2. Generate a coverage report:

```bash
coverage report
```

3. Generate an HTML coverage report:

```bash
coverage html
```

4. Open htmlcov/index.html in your browser to view the detailed coverage report.

## Continuous Integration

We've set up GitHub Actions for Continuous Integration (CI) to automatically run tests and generate coverage reports on every commit. The configuration is located in `.github/workflows/python-app.yml`.

### To set up GitHub Actions

1. Push your changes to your fork.
2. Create a pull request to the main repository.
3. The CI will automatically run and display results on the pull request page.

## Submitting Changes

1. Ensure all tests pass.
2. Ensure code coverage is adequate.
3. Create a pull request with a clear description of your changes.

### How to submit a Pull Request

1. Search our repository for open or closed
   [Pull Requests](https://github.com/mauvehed/yourip/pulls)
   that relate to your submission. You don't want to duplicate effort.
2. Fork the project
3. Create your feature branch (`git checkout -b feat/amazing_feature`)
4. Commit your changes (`git commit -m 'feat: add amazing_feature'`) yourIP uses [conventional commits](https://www.conventionalcommits.org), so please follow the specification in your commit messages.
5. Push to the branch (`git push origin feat/amazing_feature`)
6. [Open a Pull Request](https://github.com/mauvehed/yourip/compare?expand=1)

Thank you for contributing! Your help is much appreciated. If you have any questions, feel free to open an issue.
