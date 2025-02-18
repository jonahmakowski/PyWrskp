# Documentation for src/helpfulPackage/setup.py

**pyWrkspPackage Documentation**
=====================================

**Summary**
------------

The pyWrkspPackage script is a Python package that provides a set of helpful functions for various tasks. It serves as a foundation for further development and customization.

**Functions and Classes**
-------------------------

### setup()

```python
def setup(
    name: str,  # Package name
    version: str,  # Package version
    description: str,  # Package description
    package_dir: dict = {},  # Package directory
    packages: list = [],  # List of packages to include
    long_description: str,  # Long description of the package
    long_description_content_type: str = "text/markdown",  # Content type of the long description
    url: str = "",  # URL of the package
    author: str = "",  # Author name
    author_email: str = "",  # Author email address
    license: str = "",  # License of the package
    classifiers: list = [],  # List of classifiers for the package
    install_requires: list = [],  # List of dependencies to install
    extras_require: dict = {},  # Dictionary of extra dependencies
    python_requires: str = "",  # Minimum Python version required
):
```

*   `name`: Package name (string)
*   `version`: Package version (string)
*   `description`: Package description (string)
*   `package_dir`: Directory to find the packages in (dictionary)
*   `packages`: List of packages to include (list)
*   `long_description`: Long description of the package (string)
*   `long_description_content_type`: Content type of the long description (string)
*   `url`: URL of the package (string)
*   `author`: Author name (string)
*   `author_email`: Author email address (string)
*   `license`: License of the package (string)
*   `classifiers`: List of classifiers for the package (list)
*   `install_requires`: List of dependencies to install (list)
*   `extras_require`: Dictionary of extra dependencies (dictionary)
*   `python_requires`: Minimum Python version required (string)

Returns:

*   None

**Dependencies**
-----------------

The script depends on the following external packages:

*   `setuptools` for package installation and management
*   `python-dotenv` for environment variable loading
*   `twine>=4.0.2` for development dependencies

Note: The `twine` dependency is only included in the `dev` extras.

**Code**
-------

```python
# Import necessary modules from setuptools
from setuptools import find_packages, setup

# Read the long description from the README.md file
with open("app/README.md", "r") as f:
    long_description = f.read()

# Set up the package using the setup function
setup(
    # Package metadata
    name="pyWrkspPackage",
    version="0.3.0",
    description="A group of helpful functions for Python",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonahmakowski/pyWrskp",
    author="Jonah Makowski",
    author_email="jonah@makowski.ca",
    license="MIT",
    # Classifiers for the package
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    # Dependencies to install
    install_requires=['python-dotenv'],
    # Extra dependencies
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    # Minimum Python version required
    python_requires=">=3.10",
)
```

This documentation provides a clear overview of the `pyWrkspPackage` script, including its functions and classes, dependencies, and code structure.