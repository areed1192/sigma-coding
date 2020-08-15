import json
import pathlib

from setuptools import find_namespace_packages
from setuptools import find_packages


class WindowsPathEncoder(json.JSONEncoder):

    def default(self, obj):

        # If we have a Windows Path Object, convert it to a string.
        if isinstance(obj, pathlib.WindowsPath):
            return obj.as_posix()

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


# Grab the Current Working Directory.
current_working_directory: pathlib.WindowsPath = pathlib.Path(
).cwd().parents[1].absolute()

# Grab all the directories in that folder.
all_directories = list(current_working_directory.iterdir())

# Save it to a JSON file.
with open(file='configs/packages.jsonc', mode='w+') as pack_json:
    json.dump(
        obj=all_directories,
        fp=pack_json,
        indent=2,
        cls=WindowsPathEncoder
    )
