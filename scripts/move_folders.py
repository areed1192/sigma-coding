import json
import pathlib

from pprint import pprint
from distutils.dir_util import copy_tree

# Save it to a JSON file.
with open(file='configs/packages_files.jsonc', mode='r') as pack_json:
    repos = json.load(fp=pack_json)

# Define the folder to copy to.
sigma_folder = pathlib.Path().cwd().joinpath('sigma')

# Define a set to house all the unique folders.
folders_to_create = set()

# Loop through each repo.
for repo in repos:

    # Create a path.
    repo_path = pathlib.Path(repo)

    # Grab all the files in it.
    files = repo_path.glob("*")

    # Loop through each file.
    for file in files:

        # Define the library folder name.
        library_folder = file.parents[0].parts[-1]

        # Define the Destination path.
        library_destination_folder_path: pathlib.WindowsPath = sigma_folder.joinpath(
            library_folder
        ).absolute()

        # Define the source path.
        library_source_folder_path = file.parents[0]

        # Add the folders to create.
        folders_to_create.add(
            (library_source_folder_path, library_destination_folder_path)
        )

# Loop through the folders to create.
for folder_to_create in folders_to_create:

    # Define the source and destination folder.
    source_folder_str = folder_to_create[0].as_posix()
    destination_folder_str = folder_to_create[1].as_posix()

    # If it doesn't exist.
    if folder_to_create[1].is_dir() and not folder_to_create[1].exists():

        # Create it.
        folder_to_create[1].mkdir(exist_ok=True)

    else:
        pass

        # # Copy the tree.
        # copy_tree(src=source_folder, dst=destination_folder)

    print('SIGMA FOLDER: {dest_folder}'.format(
        dest_folder=destination_folder_str
    ))
    print('SOURCE FOLDER: {src_folder}'.format(
        src_folder=source_folder_str
    ))
    print('')
