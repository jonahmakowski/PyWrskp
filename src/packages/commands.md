# Commands to upload package

## Cd
```cd ~/Desktop/Github/pyWrskp/src/packages```

Then move to the correct directory for the package

## Build
```python3 -m build```

## Upload
```python3 -m twine upload --repository testpypi dist/*```

## Download
```pip install -i https://test.pypi.org/simple/ pyWrskp==VERSION``` replace VERSION with the version you wish to install.