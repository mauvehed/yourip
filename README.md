<h1 align="center">
  <a href="https://github.com/mauvehed/yourip">
    <img src="docs/images/yourIP_logo.png" alt="yourIP Logo" width="100" height="100">
  </a>
</h1>

<div align="center">
  <a href="https://github.com/mauvehed/yourip/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  -
  <a href="https://github.com/mauvehed/yourip/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  -
  <a href="https://github.com/mauvehed/yourIP/issues/new?assignees=&labels=enhancement&template=03_CODEBASE_IMPROVEMENT.md&title=dev%3A+">Suggest Improvement</a>
  -

</div>

<div align="center">
<br />

[![Deployment](https://github.com/mauvehed/yourip/actions/workflows/deploy-flyio-app.yml/badge.svg)](https://github.com/mauvehed/yourip/actions/workflows/deploy-flyio-app.yml)
[![CodeQL](https://github.com/mauvehed/yourIP/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/mauvehed/yourIP/actions/workflows/codeql-analysis.yml)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4ec1fc69d8a14048a80124167f6f7664)](https://www.codacy.com/gh/mauvehed/yourIP/dashboard)
[![Project license](https://img.shields.io/github/license/mauvehed/yourip.svg?style=flat-square)](LICENSE)
[![Website](https://img.shields.io/website?url=https%3A%2F%2FyourIP.app)](https://yourip.app)

</div>

## About

**yourIP** started as a simple web app to fulfill a common need I have of identifying my public IP without having
to use other methods to relay it back to me. This is half a purposeful tool and the other half a nice excuse to
learn some new things and deployment technologies.

### Built With

- <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
- <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
- <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />

## Usage

### Development

Please see [Contributing](#contributing) for how to setup a dev environment

### Using the website

The current deployment of this tool is hosted and available to all online. You will have a couple choices for how you access
the website and what format your ask for the IP address to be returned in.

1. Point your browser to the official app URL at [https://yourip.app](https://yourip.app)
2. Use your favorite command line web tool (e.g. curl, wget) to access one of the two endpoints (raw or json)

   ```sh
   $ curl -L yourIP.app/json
   {
     "ip": "123.45.6.78"
   }
   ```

   ```sh
   $ curl -L yourIP.app/raw
   123.45.6.78
   ```

### Issues and feature requests

You've found a bug in the source code, a mistake in the documentation or maybe you'd like a new feature? You can help us by [submitting an issue on GitHub](https://github.com/mauvehed/yourip/issues). Before you create an issue, make sure to search the issue archive -- your issue may have already been addressed!

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

**Even better: Submit a pull request with a fix or new feature!**

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Security

- **yourIP** follows good practices of security, but 100% security cannot be assured.
- **yourIP** is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.

## Acknowledgements

> Long desired to build, but for sure inspired by Zate's [https://urip.fyi](https://urip.fyi) web [project](https://github.com/Zate/urip.fyi) in Go
