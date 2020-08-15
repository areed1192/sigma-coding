import json
import pathlib
from pprint import pprint

# Save it to a JSON file.
with open(file='configs/packages.jsonc', mode='r') as pack_json:
    file_paths = json.load(fp=pack_json)

all_directories = []
all_folders = []
for file_path in file_paths:

    folder_path = pathlib.WindowsPath(file_path)
    all_directories = all_directories + list(folder_path.iterdir())

for directory in all_directories:
    folder_path = pathlib.WindowsPath(directory)

    if folder_path.is_dir():

        for folder in list(folder_path.iterdir()):

            filter_list = [
                'resources and note', 'config', 'configs',
                'docs', 'data', 'indicators', 'sample-responses',
                'dist', 'build', '.vscode', 'LICENSE', '.gitignore',
                '.pypirc', '.git', '.github', 'tests', 'README.md',
                'resources', 'samples', 'setup.py'
            ]

            if folder.parts[-1] not in filter_list and not folder.is_file() and '.egg-info' not in folder.parts[-1]:
                print(folder.parts)
                all_folders.append(folder)


class WindowsPathEncoder(json.JSONEncoder):

    def default(self, obj):

        # If we have a Windows Path Object, convert it to a string.
        if isinstance(obj, pathlib.WindowsPath):
            return obj.as_posix()

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


all_folders = list(set(all_folders))

# Save it to a JSON file.
with open(file='configs/packages_files.jsonc', mode='w+') as pack_json:
    json.dump(
        obj=all_folders,
        fp=pack_json,
        indent=2,
        cls=WindowsPathEncoder
    )
