# Installation Notes: pip

## `pip` Overview

[pip overview](https://pip.pypa.io/en/stable/)

## `pip` Upgrade

```console
python -m pip install -U pip
```

## `pip` [List](https://pip.pypa.io/en/stable/reference/pip_list/)

Shows installed packages in the tabular format.

### List Usage

```bash
pip list
```

### List Options

```bash
pip list -l # shows packages installed in local virtual environment
pip list -o # lists outdated packages
pip list -u # lists up-to-date packages

pip list --format=json

pip list -l > requirements_examples/requirements_table_output.txt
pip list -o > requirements_examples/requirements_out_of_date_output.txt
pip list -u > requirements_examples/requirements_up_to_date_output.txt

pip list -l --format=json > requirements_examples/requirements_json_output.jsonc
pip list -o --format=json > requirements_examples/requirements_out_of_date_json_output.jsonc
pip list -u --format=json > requirements_examples/requirements_up_to_date_json_output.jsonc
```

## `pip` [Show](https://pip.pypa.io/en/stable/reference/pip_show/)

This command shows information about a specified package.

### Show Usage

```bash
pip show sphinx
pip show --verbose sphinx
```

### Show Options

```bash
-f, --files
```

## `pip` [Search](https://pip.pypa.io/en/stable/reference/pip_search/)

This command shows information about a specified package. Search command could be
handy if we don't know the exact package name we are looking to install. All packages
and packages summaries containing search term are included in the result.

### Search Usage

```bash
pip search peppercorn
```

### Search Options

```bash
-i, --index <url>
```

Base URL of Python Package Index (default <https://pypi.org/pypi>)

## `pip` [Check](https://pip.pypa.io/en/stable/reference/pip_check/)

This command is used verify whether installed packages have compatible dependencies.

### Check Usage

```bash
pip check peppercorn
```

## `pip` [Uninstall](https://pip.pypa.io/en/stable/reference/pip_check/)

Unnecessary packages could be cleaned up from the target machine using this command.

### Install Usage

```bash
pip uninstall simplejson
```

### Install Options

```bash
-r, --requirement <file>
-y, --yes

# confirm before uninstall
pip uninstall flask-bootstrap

# uninstall without confirmation
pip uninstall -y flask-bootstrap

# uninstall all packages mentioned
pip uninstall -r requirements.txt
```
