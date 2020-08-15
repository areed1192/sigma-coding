# Python Package Installation

## Step 1: Install `setuptools`

We will be using the `setuptools` module to package our modules. If you don't have have `setuptools`
installed you'll need to install it. To install it, run the following command in your console.

```console
pip install setuptools wheel
```

If you already have you'll want to make sure you're on the latest version, so make sure to update it
using the following commands:

```console
pip install --upgrade setuptools wheel
```

## Step 2: Install `twine`

Twine is the primary tool developers use to upload packages to the Python Package Index or other Python
package indexes. It is a command-line program that passes program files and metadata to a web API. Developers
use it because it’s the official PyPI upload tool, it’s fast and secure, it’s maintained, and it reliably works.
To install `twine`, run the following command:

```console
pip install twine
```

if you already have ir you'll want to make sure you're on the latest version, so make sure to update it
using the following commands:

```console
pip install --upgrade twine
```

## Step 3: Build our Distribution Package

Now that we have everything installed, we can build or distribution package. To build our distribution pacakge run
the following command:

```console
python setup.py sdist bdist_wheel
```

## Step 4: Upload our Distribution Pacakge to PyPi test Index

To upload the distribution run the following command:

```console
twine upload --repository testpypi --config-file pypirc dist/*
```

```console
twine upload --repository pypi --config-file pypirc dist/*
```
