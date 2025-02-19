# pyWrkspPackage
## Installation

This command should work on my local network.
```
pip install pyWrkspPackage --index-url http://192.168.86.4:8929/api/v4/projects/4/packages/pypi/simple
```

However, you can also add the project to your pip index urls, and then you don't need the --index-url flag. The following commands do that:
```
pip config set global.index-url http://192.168.86.4:8929/api/v4/projects/4/packages/pypi/simple
pip config set global.trusted-host 192.168.86.4
pip config set global.extra-index-url https://pypi.org/simple # Still use regular pypi
```

After that you can install the package by simply running
```
pip install pyWrkspPackage
```
