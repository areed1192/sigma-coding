# Installation Notes: Version Control

## Overview

Link to [resource](https://pip.pypa.io/en/stable/reference/pip_install/#id32)

`pip` supports installing from Git, Mercurial, Subversion and Bazaar, and detects the type of VCS
using URL prefixes: git+, hg+, svn+, and bzr+. `pip` requires a working VCS command on your
path: git, hg, svn, or bzr.

VCS projects can be installed in editable mode (using the --editable option) or not.

For editable installs, the clone location by default is `venv path/src/SomeProject` in virtual environments
, and `cwd/src/SomeProject` for global installs. The --src option can be used to modify this location.

For non-editable installs, the project is built locally in a temp dir and then installed normally. Note that
if a satisfactory version of the package is already installed, the VCS source will not overwrite it without
an --upgrade flag. VCS requirements pin the package version (specified in the setup.py file) of the target commit,
not necessarily the commit itself.

The pip freeze subcommand will record the VCS requirement specifier (referencing a specific commit) if and only
if the install is done using the editable option.

The "project name" component of the URL suffix `egg=project name` is used by pip in its dependency logic to
identify the project prior to pip downloading and analyzing the metadata. For projects where setup.py is not
in the root of project, the "subdirectory" component is used. The value of the "subdirectory" component should
be a path starting from the root of the project to where setup.py is located.

If your repository layout is:

```console
pkg_dir
├── setup.py # setup.py for package "pkg"
└── some_module.py
other_dir
└── some_file
some_other_file
```

Then, to install from this repository, the syntax would be:

```console
pip install -e "vcs+protocol://repo_url/#egg=pkg&subdirectory=pkg_dir"
```

## Using Git

Link to [resource](https://pip.pypa.io/en/stable/reference/pip_install/#id33)

pip currently supports cloning over `git`, `git+http`, `git+https`, `git+ssh`, `git+git`
and `git+file`.

Warning Note that the use of `git`, `git+git`, and `git+http` is discouraged. The former two use the Git
Protocol, which lacks authentication, and HTTP is insecure due to lack of TLS based encryption.

Here are the supported forms:

```console
[-e] git+http://git.example.com/MyProject#egg=MyProject
[-e] git+https://git.example.com/MyProject#egg=MyProject
[-e] git+ssh://git.example.com/MyProject#egg=MyProject
[-e] git+file:///home/user/projects/MyProject#egg=MyProject
```

Passing a branch name, a commit hash, a tag name or a git ref is possible like so:

```console
[-e] git+https://git.example.com/MyProject.git@master#egg=MyProject
[-e] git+https://git.example.com/MyProject.git@v1.0#egg=MyProject
[-e] git+https://git.example.com/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject
[-e] git+https://git.example.com/MyProject.git@refs/pull/123/head#egg=MyProject
```

When passing a commit hash, specifying a full hash is preferable to a partial hash because a full
hash allows pip to operate more efficiently (e.g. by making fewer network calls).
