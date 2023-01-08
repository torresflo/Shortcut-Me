![GitHub license](https://img.shields.io/github/license/torresflo/Shortcut-Me.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
![GitHub contributors](https://img.shields.io/github/contributors/torresflo/Shortcut-Me.svg)
![GitHub issues](https://img.shields.io/github/issues/torresflo/Shortcut-Me.svg)

<p align="center">
  <h1 align="center">Shortcut Me</h3>

  <p align="center">
    A little python script to help you update your readme file with a random code editor shortcut.
    <br />
    <a href="https://github.com/torresflo/Shortcut-Me/issues">Report a bug or request a feature</a>
  </p>
</p>

## Table of Contents

* [Installation](#installation)
   * [Preparation work](#preparation-work)
   * [Project setup](#project-setup)
* [Example](#example)
* [Contributing](#contributing)
* [License](#license)

---

## Installation

### Preparation work

Add comments to the place where you want to update in your readme file.

You can add a shortcut with:
   ```markdown
    <!-- shortcut-box start -->
    <!-- shortcut-box end -->
   ```

### Project setup

For updating your github profile README, you can follow [update-shortcut.yml](https://github.com/torresflo/Shortcut-Me/blob/master/.github/workflows/update-shortcut.yml) to create a GitHub Action in your README repository.

1. Go to the repo **Settings > Secrets**
1. Add the following environment variable:
   - **MARKDOWN_FILE:** The name of your readme file. 

## Example

Here is an example from my own profile that you could obtain:

![Example image](https://raw.githubusercontent.com/torresflo/Shortcut-Me/examples/example1.png)

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the [GNU General Public License v3.0](./LICENSE). See `LICENSE` for more information.
