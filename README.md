<!--
## README Template Overview

This document is the standardized README template for the Octopy company.
It defines the required structure and sections to ensure consistency, clarity, and maintainability across all Octopy repositories.
Use this template as a starting point and remove any comments, placeholder text, or sections that are not applicable to your project.
-->

# Repository Name

<!-- Project Shields/Badges
Badges show required programming langue, framework, module in your project repository.
Syntaxis: [![Shield Name](Image URL)](Link URL).
Use the following link https://shields.io/badges, you can generate your shields.
-->


[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=plastic&logo=github)](https://github.com/)
[![WebSocket](https://img.shields.io/badge/WebSocket-Enabled-C93CD7.svg?style=plastic&logo=socket)](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
[![Python](https://img.shields.io/badge/Python-v3.12+-3776AB.svg?style=plastic&logo=python)](https://www.python.org/)
[![ROS2](https://img.shields.io/badge/ROS2-Humble-22314E.svg?style=plastic&logo=ros)](https://docs.ros.org/en/humble/index.html)
[![FASTAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg?style=plastic&logo=fastapi)](https://fastapi.tiangolo.com/)
![SQALCHEMY](https://img.shields.io/badge/SQLAlchemy-306998?logo=python&logoColor=white)
[![UBUNTU](https://img.shields.io/badge/Ubuntu-v22.04-E95420.svg?style=plastic&logo=ubuntu)](https://releases.ubuntu.com/jammy/)
[![C++](https://img.shields.io/badge/C++-00599C.svg?style=plastic&logo=c)](link)
[![LICENSE](https://img.shields.io/badge/License-MIT-FF0000.svg?style=plastic&logo=github)](link)


High-level description of the project and its purpose.
<span style="color:green">Add an image related to the repository or a representative result.</span>

![Demo_result](docs/result.png)

  
## Features

<span style="color:blue">List of main functionalities.</span>

- ***Feature 1*** – Description
- ***Feature 2*** – Description
- ***Feature 3*** – Description


## Information sources

Add links to official documentation of the frameworks used in the repo.

- Navigation 2: https://navigation.ros.org/index.html


---
## Table of Contents

- [Requirements](#requirements)
   - [Hardware](#hardware)
   - [Software](#software)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage or Quick start](#usage-or-quick-start)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

---
## Requirements

Prerequisites needed to run or develop the project.

### Hardware
- Minimum hardware specifications.


### Software
- Required operating systems, runtimes, and tools.


---
## Installation

**Clone the repository**

```bash
git clone <repository-url>
```

**Install dependencies**

```bash
sudo apt install libmpv1 python3-venv
```

**Configure environment variables**

- Create the required environment/configuration files.
- Set the necessary values as described in the Configuration section.
- Debug or logging options

**Virtual environment setup**

```bash
cd name_folder
python3 -m venv .venv               #create virtual environment
source .venv/bin/activate           #activate venv
pip install -r requirements.txt     #install requirements
```

To generate the `requirements.txt` file with all current dependencies, use:
```bash
pip freeze > requirements.txt
```

> [!IMPORTANT]
> **Specify Versions:** It is highly recommended to specify package versions (e.g., `pandas==1.3.3`) in your `requirements.txt` to ensure reproducibility and avoid compatibility issues.


To deactivate virtual env:

```bash
deactivate
```

**Verify the installation:**
```bash
<command-to-verify>
```

**Building the project:**
```bash
<command-to-build-or-run>
```

---
## Project Structure

Explanation of the folder and file organization.
To automatic generate folder structure, use `tree` command. If not installed `sudo apt-get install tree`.

```bash
folder_name
├── docs
│   └── result.png
├── backend
│   ├── app.py
│   ├── install.sh         #bash installation script
│   ├── instance
│   │   └── database.db
│   └── requirements.txt
└── README.md              #Project documentation
```

---
## Usage or Quick start

Descriptive procedure to run application either as a whole or as module.

Once your virtual environment is activated, run Python script
```bash
python3 main.py
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

1. Fork the repository (if you do not have write access).
2. Clone the repository to your local environment.
3. Create a new branch for your changes:
```bash
git checkout -b feature/short_description
```
4. Make your changes following the project standards.
5. Commit your changes with a clear and descriptive message:
```bash
git commit -m "Add: short description of the change"
```
6. Push your branch to the remote repository:
```bash
git push -u origin feature/short_description
```
7. Open a pull Request against the main branch.
8. Address review comments if required.
9. Once approved, the changes will be merged.

---
## License

This section describes the license of this repository. If a license is set, add the corresponding `License` file.

---
## Credits

<!--
This section acknowledges individuals, teams, or resources that contributed to this project.
-->

+ **Author:** <span style="color:green">Yanahi Castillo</span>

+ **Contact:** [Email](email@example.com)

+ **Project Link:** [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


---
Return to [Table of Contents](#table-of-contents)
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
