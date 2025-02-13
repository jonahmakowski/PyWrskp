# Documentation for src/helpfulPackage/setup.py

**pyWrkspPackage Documentation**

**Summary**
-----------

The pyWrkspPackage is a Python package that provides a group of helpful functions for various tasks. It includes functions and classes designed to simplify programming tasks, making it easier for developers to write efficient and effective code.

**Functions and Classes**
------------------------

### Functions

*   `setup()`: This function is used to configure the package and its dependencies.
    *   Parameters:
        +   `name` (str): The name of the package.
        +   `version` (str): The version number of the package.
        +   `description` (str): A brief description of the package.
        +   `package_dir` (dict): The directory where the packages are located.
        +   `packages` (list): A list of packages to include in the distribution.
        +   `long_description` (str): The long description of the package.
        +   `long_description_content_type` (str): The format of the long description.
        +   `url` (str): The URL of the package's repository.
        +   `author` (str): The author of the package.
        +   `author_email` (str): The email address of the author.
        +   `license` (str): The license under which the package is released.
        +   `classifiers` (list): A list of classifiers for the package.
        +   `install_requires` (list): A list of packages required to install the package.
        +   `extras_require` (dict): A dictionary of additional dependencies, where keys are strings like 'dev' and values are lists of packages.
        +   `python_requires` (str): The minimum version of Python required to run the package.

*   `find_packages(where="app")`: This function finds all packages in the given directory.

### Classes

None. The script only defines a setup function from setuptools without any custom classes.

**Dependencies**
---------------

The pyWrkspPackage depends on:

*   `python-dotenv`
*   `twine>=4.0.2` (only required for development)

**Code**

```python
# Import the necessary module from setuptools
from setuptools import find_packages, setup

# Open and read the README.md file to generate a long description
with open("app/README.md", "r") as f:
    # Read the contents of the README.md file
    long_description = f.read()

# Use the setup function to configure the package and its dependencies
setup(
    # Specify the name of the package
    name="pyWrkspPackage",
    
    # Specify the version number of the package
    version="0.2.1",
    
    # Provide a brief description of the package
    description="A group of helpful functions for Python",
    
    # Specify the directory where the packages are located
    package_dir={"": "app"},
    
    # Find all packages in the 'app' directory
    packages=find_packages(where="app"),
    
    # Use the long description read from the README.md file
    long_description=long_description,
    
    # Specify the format of the long description
    long_description_content_type="text/markdown",
    
    # Provide information about the package's author and repository URL
    url="https://github.com/jonahmakowski/pyWrskp",
    author="Jonah Makowski",
    author_email="jonah@makowski.ca",
    
    # Specify the license under which the package is released
    license="MIT",
    
    # Provide classifiers for the package
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    
    # Specify the packages required to install the package
    install_requires=['python-dotenv'],
    
    # Specify additional dependencies for development
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    
    # Specify the minimum version of Python required to run the package
    python_requires=">=3.10",
)
```