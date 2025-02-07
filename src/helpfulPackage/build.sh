cat >.pypirc <<EOL
[distutils]
index-servers =
    first-repository

[first-repository]
repository = https://test.pypi.org/legacy/
username = WhiteSwine
password = $TEST_PYPI_PASSWORD
... 
EOL
echo "Created .pypirc file"

python setup.py bdist_wheel sdist
echo "Built wheel and source distribution"

pip install .[dev]
echo "Installed Dependancies"

twine check dist/*
echo "Checked distribution"

twine upload — repository testpypi dist/*
echo "Uploaded to testpypi"