# Installation Notes: Twine

## Overview

Twine is the primary tool developers use to upload packages to the Python Package Index or other Python
package indexes. It is a command-line program that passes program files and metadata to a web API. Developers
use it because it’s the official PyPI upload tool, it’s fast and secure, it’s maintained, and it reliably works.

Link to [documentation](https://twine.readthedocs.io/en/latest/)

## Why Use Twine

The goal of Twine is to improve PyPI interaction by improving security and testability. The biggest reason to
use Twine is that it **securely authenticates you to PyPI** over HTTPS using a verified connection, regardless
of the underlying Python version. Meanwhile, python `setup.py` upload will only work correctly and securely
if your build system, Python version, and underlying operating system are configured properly.

Secondly, Twine encourages you to build your distribution files. Python `setup.py` upload only allows you to upload
a package as a final step after building with distutils or setuptools, within the same command invocation. This
means that you cannot test the exact file you’re going to upload to PyPI to ensure that it works before uploading it.

Finally, Twine allows you to pre-sign your files and pass the `.asc` files into the command line invocation
(twine upload myproject-1.0.1.tar.gz myproject-1.0.1.tar.gz.asc). This enables you to be assured that you’re typing
your `gpg passphrase` into gpg itself and not anything else, since you will be the one directly
executing `gpg --detach-sign -a <filename>`.

## Installing Twine

To install `twine`, run the following command:

```console
pip install twine
```

If you already have it you'll want to make sure you're on the latest version, so make sure to update it
using the following command:

```console
pip install --upgrade twine
```

## Using Twine

- Step 1: Create some distributions in the normal way.

  ```bash
  python setup.py sdist bdist_wheel
  ```

- Step 2: Upload with twine to Test PyPI and verify things look right.
  Twine will automatically prompt for your username and password.

  ```bash
  twine upload -r testpypi dist/*
  username: ...
  password: ...
  ```

- Step 3: Upload to PyPI

  ```bash
  twine upload dist/*
  ```

## Note on the `.pypirc` File

Part of the benefit to using `twine` is that it can leverage a file `.pypirc` now I've never been able to find a definitive name
for this file, but I always called it the PyPi Runtime Configuration file.

A `.pypirc` file allows you to define the configuration for package indexes (referred to here as "repositories"), so that you
don’t have to enter the URL, username, or password whenever you upload a package with twine.

Now the location of this file is very important because if you don't put it in the right location then `twine` can't use it becuase
it won't be able to find it. Now, I had a hard time figuring out where to put this file initially because I would see commands like
`%HOME%` and when I used them on my Windows machine it would say it couldn't find them.

When I explored the issue in more detail I found that for some Windows users that command doesn't work and that `twine` will then try
to use other commands. `twine` will use the `os` library to find the User's HOMEPATH, in full it runs the following code:

```python
os.path.expanduser('~/')
```

Now that line will try to look for following environment variables on your system in the following order:

1. `%HOME%`, this will be checked first.
2. `%USERPROFILE%`, this will be checked if `%HOME%` fails.
3. `%HOMEDRIVE%\%HOMEPATH%`, this will be checked if `%USERPROFILE%` fails.

On my system I had to place my `.pypirc` file in the following location:

```console
C:\Users\Alex\.pypirc
```
