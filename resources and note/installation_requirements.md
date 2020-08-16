# Building the `requirements.txt` File

## Overview

A `requirements.txt` file is used for specifying what python packages are required to
run the project you are looking at. Now there are many ways to generate this file, and some
provide a better framework than others, depending on the goal at hand.

However, before we start jumping into the different ways to build a `requirement.txt` file, I want
to share a link with you that goes over the difference between the `requirement.txt` file and the
`setup.py` file. While these two frameworks can do similar things, they are used for very different
purposes.

Link to [Setup Vs. Requirement](https://caremad.io/posts/2013/07/setup-vs-requirement/).

## Option 1: `pip freeze`

Output installed packages in requirements format. Packages are listed in a case-insensitive sorted order.

### Running `pip freeze`

To generate a `requirement.txt` file using the `pip freeze` command, from the terminal, run the following
code:

```console
pip freeze > requirements.txt
```

That command will generate a new file in your directory named `requirement.txt` and it will have the following
format:

```console
azure-keyvault-secrets==4.2.0
azure-mgmt-resource==10.2.0
azure-mgmt-sql==0.20.0
-e git+https://github.com/areed1192/azure-sql-data-project.git@107ad6c3cc3cf82e44b4b9bb0eaa5eca9d7fd7d4#egg=azure_sql_project
backcall==0.2.0
```

Here are some additional arguments that you can apply with the `freeze` command.

-`r`, `--requirement <file>`

- Use the order in the given requirements file and its comments when generating output. This option can be used multiple times.

-`f`, `--find-links <url>`

- URL for finding packages, which will be added to the output.

-`l`, `--local`

- If in a virtualenv that has global access, do not output globally-installed packages.

`--user`

- Only output packages installed in user-site.

`--path <path>`

- Restrict to the specified installation path for listing packages (can be used multiple times).

`--all`

- Do not skip these packages in the output: setuptools, wheel, pip, distribute

`--exclude-editable`

- Exclude editable package from output.

### More Examples of `pip freeze`

```bash
pip freeze -l > requirements.txt
pip freeze --path "C:\Users\Alex\OneDrive\Desktop\Sigma\Repo - Upload PyPi\uploading-python-packages" > requirements_path.txt
pip freeze -q -r requirements.txt | grep -B100 "pip freeze" | grep -v "pip freeze" > requirements-froze.txt
pip freeze –r > requirements-top-level.txt
```

## Option 2: `pipreqs`

### What is and Why Use `pipreqs`

Generate pip requirements.txt file based on imports of any project. Looking for maintainers to move this project forward.

- `pip freeze` only saves the packages that are installed with `pip install` in your environment.
- `pip freeze` saves all packages in the environment including those that you don't use in your current project. (if you don't have virtualenv)
- and sometimes you just need to create `requirements.txt` for a new project without installing modules.

Link to this [overview](https://github.com/bndr/pipreqs).

### Installing `pipreqs`

To install `pipreqs` run the following command:

```bash
pip install pipreqs
```

### Using `pipreqs`

Run `pipreqs`

```bash
pipreqs "<PATH/TO/FOLDER>"
```

Another feature of `pipreqs` is cleaning an existing `requirements.txt` file of dependencies that aren't being imported. To
utilize this feature you would run the following command:

```bash
pipreqs --clean "<PATH/TO/FOLDER>"
```

### Additional Options of `pipreqs`

```console
Usage:
    pipreqs [options] <path>

Options:
    --use-local           Use ONLY local package info instead of querying PyPI
    --pypi-server <url>   Use custom PyPi server
    --proxy <url>         Use Proxy, parameter will be passed to requests library. You can also just set the
                          environments parameter in your terminal:
                          $ export HTTP_PROXY="http://10.10.1.10:3128"
                          $ export HTTPS_PROXY="https://10.10.1.10:1080"
    --debug               Print debug information
    --ignore <dirs>...    Ignore extra directories
    --encoding <charset>  Use encoding parameter for file open
    --savepath <file>     Save the list of requirements in the given file
    --print               Output the list of requirements in the standard output
    --force               Overwrite existing requirements.txt
    --diff <file>         Compare modules in requirements.txt to project imports.
    --clean <file>        Clean up requirements.txt by removing modules that are not imported in project.
    --no-pin              Omit version of output packages.
```

## Bugs with `pipreqs`

Keep in mind you may experience a bug when it comes to the encoding of the file. If that pops up simply use
the following command:

```bash
pipreqs --encoding utf-8
```

## Option 3: `pipdeptree`

### What is `pipdeptree`

pipdeptree is a command line utility for displaying the installed python packages in form of a dependency
tree. It works for packages installed globally on a machine as well as in a virtualenv. Since pip freeze
shows all dependencies as a flat list, finding out which are the top level packages and which packages do
they depend on requires some effort. It can also be tedious to resolve conflicting dependencies because pip
doesn’t yet have true dependency resolution (more on this later). This utility tries to solve this problem.

Link to this [overview](https://pypi.org/project/pipdeptree/).

### Using `pipdeptree`

To use `pipdeptree` to generate a `requirments.txt` file, you can run the following command on a Windows
terminal.

```bash
pipdeptree > requirements_examples/pipdeptree_find.txt
pipdeptree | findstr -P '^\w+' > requirements_examples/pipdeptree_find.txt
```

The Linux equivalent is the following:

```bash
pipdeptree | grep -P '^\w+' > requirements_examples/pipdeptree_find.txt
```

I can also use `pipdeptree` to generate a JSON output.

```bash
pipdeptree --json
pipdeptree --json > requirements_examples/pipdeptree_find.jsonc
```

The output will look something like the following:

```json
[
  {
    "package": {
      "key": "wrapt",
      "package_name": "wrapt",
      "installed_version": "1.12.1"
    },
    "dependencies": []
  },
  {
    "package": {
      "key": "wcwidth",
      "package_name": "wcwidth",
      "installed_version": "0.2.5"
    },
    "dependencies": []
  }
]
```

You can also, output the JSON content to a file, using the following command:

```bash
pipdeptree --json > requirements.json
```
