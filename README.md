<!--
## README Template Overview

This document is the standardized README template for the Octopy company.

It defines the required structure and sections to ensure consistency, clarity, and maintainability across all Octopy repositories.

Use this template as a starting point and remove any comments, placeholder text, or sections that are not applicable to your project.

-->

# Repository Name

<!--The repository name defines how the project is identified and referenced within the organization and on GitHub.

***A clear and consistent naming convention improves:
***Discoverability
***Organization

Long-term maintainability
-->


<!--Project Shields-->

<!--
See the bottom of this document for the declaration of the reference variables.
Syntaxis: [![Shield Name](Image URL)](Link URL).
Use the following link https://shields.io/badges, you can generate your shields.
Review these examples and implement the required shields in your project repository.
-->


[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=plastic&logo=github)](https://github.com/)
[![HTML5](https://img.shields.io/badge/HTML5-Ready-E34F26.svg?style=plastic&logo=html5)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![SVG](https://img.shields.io/badge/SVG-Animated-FFB13B.svg?style=plastic&logo=svg)](https://developer.mozilla.org/en-US/docs/Web/SVG)
[![WebSocket](https://img.shields.io/badge/WebSocket-Enabled-C93CD7.svg?style=plastic&logo=socket)](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
[![Python](https://img.shields.io/badge/Python-v3.7+-3776AB.svg?style=plastic&logo=python)](https://www.python.org/)
[![SROS2](https://img.shields.io/badge/SROS2-Humble-22314E.svg?style=plastic&logo=ros)](https://docs.ros.org/en/humble/index.html)
[![FASTAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg?style=plastic&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PYDANTIC](https://img.shields.io/badge/Pydantic-v2.12-E92063.svg?style=plastic&logo=pydantic)](https://docs.pydantic.dev/latest/)
[![UBUNTU](https://img.shields.io/badge/Ubuntu-v22.04-E95420.svg?style=plastic&logo=ubuntu)](https://releases.ubuntu.com/jammy/)
[![C++](https://img.shields.io/badge/C++-00599C.svg?style=plastic&logo=c)](link)
[![LICENSE](https://img.shields.io/badge/License-MIT-FF0000.svg?style=plastic&logo=github)](link)
[![JSON](https://img.shields.io/badge/JSON-000000.svg?style=plastic&logo=JSON)](https://fastapi.tiangolo.com/tutorial/encoder/#using-the-jsonable-encoder)



---
## Abstract
<!-- 
High-level description of the project and its purpose.
Add an image related to the repository
-->

![Image description - Put the link in parentheses, as shown in the example](https://gist.githubusercontent.com/abhirampai/ce94b0b8345cd969d3cf997578487cdd/raw/b2dc51d4421db9d4a5a17be817e07dc8ad1e3375/hello.gif)

---   
## Features
<!--
Add a list of the features included in the repository – Description of each specification.
List of main functionalities.
Descriptions of features from the end-user perspective.
Specific scenarios showing how the system is used.
-->

- ***Feature 1*** – Description
- ***Feature 2*** – Description
- ***Feature 3*** – Description

---
## Table of Contents
<!--
Add to the table of contents the sections you consider necessary.
-->

- [Requirements](#requirements)
    - [Hardware](#hardware)
    - [Software](#software)
- [Quick Start](#quick-start)
- [Installation](#installation)
    - [Configuration](#configuration)
- [Quick Reference](#quick-reference)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

---
## Requirements

<!--
Prerequisites needed to run or develop the project.
-->

### Python 
#### **Virtual Environment**

- **Navigate** into the folder
```bash
   $ cd name_folder
```
- **Activate Virtual Environment.** To use the virtual environment, you have to activate it with this command.

```bash
   $ source .venv/bin/activate
```
- **Run** the script: 
```bash
   $ python name.py
```
- **Deactivate the virtual environment**

```bash
   $ deactivate
```

### Hardware
- Minimum hardware specifications.


### Software
- Required operating systems, runtimes, and tools.

---

## Quick Start
<!--
The Quick Start section provides the minimum steps required to get the project running quickly.
This section focuses only on the essential commands and actions, keeping instructions short and simple.
-->

STEP 1. Install required software

STEP 2. Configure environment variables

STEP 3. Install dependencies

STEP 4. Verify installation

> [!NOTE]
> _For detailed setup, configuration, and advanced options, please refer to the [Installation](#-installation) section._


---

## Installation
<!-- 
Steps to install the project.
Configuration of development or runtime environments.
Environment variables and configuration files.
-->

**Step 1. Clone the repository**

```bash
   git clone <repository-url>
```

**STEP 2. Install dependencies:**

```bash
<package-manager-install-command>
```
**STEP 3. Configure environment variables:**

    - Create the required environment/configuration files.
    - Set the necessary values as described in the Configuration section.

**STEP 4. Verify the installation:**
```bash
<command-to-verify-or-run>
```


---

## Configuration
<!--
The Configuration section explains how to adjust the project’s settings so it works correctly in different environments (development, testing, production).
This section describes how to configure the project before running it.
-->

### Configuration Files
- `.env` – Environment-specific variables
- `config.*` – Project configuration files (if applicable)

### Required Settings
- Environment variables required for the project to run
- Paths, URLs, or ports used by the application

### Optional Settings
- Feature flags
- Debug or logging options

> [!IMPORTANT]
> _**Update** the configuration values according to your environment before starting the application._

---

## Quick Reference
<!--
The Quick Reference section provides a concise, easy-to-scan summary of the most commonly used commands, paths, and key information for the project.
-->

- Start application: `<run-command>`
- Run tests: `<test-command>`
- Configuration file: `<config-file-path>`


---
## Project Structure
<!--
Explanation of the folder and file organization.
-->
```bash
├── src/        # Application source code
├── config/     # Configuration files
├── tests/      # Test files
├── README.md   # Project documentation
```

---
## Troubleshooting
<!--
This section lists common issues and their possible solutions.
-->

**Problem:** Description of the issue  
**Solution:** Steps to fix it

**Problem:** Another common issue  
**Solution:** How to resolve it

---
## Contributing
<!--
***CONTRIBUTION RULES***
-Follow the defined coding standards.
-Keep commits small and focused.
-Ensure tests pass before submitting a Pull Request.
-Update documentation if your changes affect behavior or usage
-Please follow the contribution guidelines defined in this repository.
-->


<!--
This section defines the standard process for contributing to this project.
-->

### Contributing workflow

1. Fork the repository (if you do not have write access).
2. Clone the repository to your local environment.
3. Create a new branch for your changes:
   ```bash
   git checkout -b feature/short-description
   ```
4. Make your changes following the project standards.
5. Commit your changes with a clear and descriptive message:
    ```bash
    git commit -m "Add: short description of the change"
    ```
6. Push your branch to the remote repository:
    ```bash
    git push origin feature/short-description
    ```
7. Open a pull Request against the main branch.
8. Address review comments if required.
9. Once approved, the changes will be merged.

---
## License
<!--
License information for the repository.
-->

This section describes the license of this repository.


---
## Credits

<!--
This section acknowledges individuals, teams, or resources that contributed to this project.
-->

- Your Name 

- Mail - [Email](email@example.com)

- Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


<!-- Basic writing and formatting syntax-->
<!--
Visit the following link https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax to enhance your README formatting using GitHub’s writing and formatting guidelines.
-->

---
<!-- Alerts -->

<!--
To add an alert, use a special blockquote line specifying the alert type, followed by the alert information in a standard blockquote. Five types of alerts are available:
-->

<!--
> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

-->
