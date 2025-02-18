# Documentation for src/helpfulPackage/setup.py

**pyWrkspPackage Documentation**
=====================================

**Summary**
------------

The pyWrkspPackage script is a Python package that provides a set of helpful functions for various tasks. The package can be easily installed using pip and provides documentation for the user.

**Functions and Classes**
-------------------------

### setup

*   **Description:** This function initializes the package.
*   **Inputs:**
    *   `name`: The name of the package.
    *   `version`: The version number of the package.
    *   `description`: A short description of the package.
    *   `package_dir`: A dictionary containing the directory path for the package.
    *   `packages`: A list of packages to include in the installation.
    *   `long_description`: A long description of the package.
    *   `long_description_content_type`: The content type of the long description.
    *   `url`: The URL of the package repository.
    *   `author`: The author's name.
    *   `author_email`: The author's email address.
    *   `license`: The license under which the package is released.
    *   `classifiers`: A list of classifiers for the package.
*   **Output:** Returns None.

```python
# setup function to initialize the package
from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyWrkspPackage",
    version="0.3.1",
    description="A group of helpful functions for Python",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonahmakowski/pyWrskp",
    author="Jonah Makowski",
    author_email="jonah@makowski.ca",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=['python-dotenv'],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
```

**Dependencies**
----------------

The following external packages/modules are required for the script to function:

*   `setuptools`
*   `python-dotenv` (install requirement)
*   `twine` (development extra requirement)

Note: The dependencies can be installed using pip: `pip install setuptools python-dotenv twine`