# see-docker
A CLI Python program to help you understand your Docker infrastructure a little better


## Installation
```shell
python3 -m venv ~/my/path/to/venv
. ~/my/path/to/venv/bin/activate
python3 -m pip install git+git://github.com/retrodaredevil/see-docker.git
```


## Quick installation (Not Recommended)
```shell
sudo python3 -m pip install git+git://github.com/retrodaredevil/see-docker.git
# or
python3 -m pip install git+git://github.com/retrodaredevil/see-docker.git
```

## Common Errors

### `error: invalid command 'bdist_wheel'`

Run this before installing:

```shell
python3 -m pip install setuptools --upgrade
python3 -m pip install wheel
```
