# Installation Notes: Development Mode

## Overview

Setuptools allows you to deploy your projects for use in a common directory or staging area, but
without copying any files. Thus, you can edit each project’s code in its checkout directory, and
only need to run build commands when you change a project’s C extensions or similarly compiled files.
You can even deploy a project into another project’s checkout directory, if that’s your preferred way
of working (as opposed to using a common independent staging area or the site-packages directory).

- **Link to this [overview](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode)**

## Running `setup.py` in Editable Mode

`Editable` installs are fundamentally `setuptools develop mode` installs. You can install local projects or
VCS projects in `editable` mode:

```bash
pip install -e path/to/SomeProject
pip install -e git+http://repo/my_project.git#egg=SomeProject
```

(See the VCS Support section above for more information on VCS-related syntax.)

For local projects, the `SomeProject.egg-info` directory is created relative to the project path. This is
one advantage over just using setup.py develop, which creates the `egg-info` directly relative the current
working directory.

### Examples

If I want to do an editable install, for a package on my system that I'm not currently in, I can provide the
full path to the project. For example, imagine I currently have this project open in Visual Studio Code, but
I want to do an editable install for my `td-ameritrade-python-api` library on my system. Well what I could do
is run the following command in the terminal.

```bash
pip install -e "C:\Users\Alex\OneDrive\Desktop\Sigma\Repo - TD API Client\td-ameritrade-python-api"
```

If I want to do an install in editable mode for the the current project I'm in. I would run the following command.

```bash
pip install -e .
```

Now the `.` (period) means, is the current directory I'm in.

- **Link to this [overview](https://pip.pypa.io/en/stable/reference/pip_install/#id45)**
