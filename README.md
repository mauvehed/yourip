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

![Deployment](https://heroku-badge.herokuapp.com/?app=heroku-badge)
[![CodeQL](https://github.com/mauvehed/yourIP/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/mauvehed/yourIP/actions/workflows/codeql-analysis.yml)
#[![Known Vulnerabilities](https://snyk.io/test/github/mauvehed/yourIP/badge.svg)](https://snyk.io/test/github/mauvehed/yourIP)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4ec1fc69d8a14048a80124167f6f7664)](https://www.codacy.com/gh/mauvehed/yourIP/dashboard)[![Website](https://img.shields.io/website?url=https%3A%2F%2FyourIP.app)](https://yourIP.app)
[![Project license](https://img.shields.io/github/license/mauvehed/yourip.svg?style=flat-square)](LICENSE)

<!--
![GitHub branch checks state](https://img.shields.io/github/checks-status/mauvehed/yourip/main)
[![Open pull requests](https://img.shields.io/github/issues-pr-raw/mauvehed/yourip?style=flat&logo=appveyor&logoColor=turquoise)](https://github.com/mauvehed/yourip/pulls)
[![Open issues](https://img.shields.io/github/issues-raw/mauvehed/yourip?style=flat&logo=appveyor&logoColor=turquoise)](https://github.com/mauvehed/yourip/issues)
[![Last Commit](https://img.shields.io/github/last-commit/mauvehed/yourip?style=flat&logo=appveyor&logoColor=turquoise)](https://github.com/mauvehed/yourip/commits/master)
[![Contributors](https://img.shields.io/github/contributors/mauvehed/yourip?style=flat&logo=appveyor&logoColor=turquoise)](https://github.com/mauvehed/yourip/graphs/contributors)
[![Prod Deploy](https://github.com/mauvehed/yourIP/actions/workflows/main.yml/badge.svg)](https://github.com/mauvehed/yourIP/actions/workflows/main.yml)
![Prod deployments](https://img.shields.io/github/deployments/mauvehed/yourIP/stage?label=prod)
![Staging deployments](https://img.shields.io/github/deployments/mauvehed/yourIP/stage?label=stage)
-->
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Usage](#usage)
  - [Development](#development)
  - [Using the website](#using-the-website)
- [Roadmap](#roadmap)
- [Support](#support)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [License](#license)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

<table><tr><td>

**yourIP** started as a simple web app to fulfill a common need I have of identifying my public IP without having
to use other methods to relay it back to me. This is half a purposeful tool and the other half a nice excuse to
learn some new things and deployment technologies.

<details>
<summary>Screenshots</summary>
<br>

> **[?]**
> Please provide your screenshots here.

|                               Home Page                               |                               Login Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/screenshot.png" title="Home Page" width="100%"> | <img src="docs/images/screenshot.png" title="Login Page" width="100%"> |

</details>

</td></tr></table>

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


## Roadmap

See the [open issues](https://github.com/mauvehed/yourip/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/mauvehed/yourip/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/mauvehed/yourip/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/mauvehed/yourip/issues?q=is%3Aopen+is%3Aissue+label%3Abug) (Squash Em!)

## Support

Reach out to the maintainer at one of the following places:

- Contact options listed on [this GitHub profile](https://github.com/mauvehed)
- @mauvehed just about anywhere else online

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.


Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [mauvehed](https://github.com/mauvehed).

For a full list of all authors and contributors, see [the contributors page](https://github.com/mauvehed/yourip/contributors).

## Security

- **yourIP** follows good practices of security, but 100% security cannot be assured.
- **yourIP** is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.

## Acknowledgements

> Long desired to build, but for sure inspired by Zate's [https://urip.fyi](https://urip.fyi) web [project](https://github.com/Zate/urip.fyi) in Go
