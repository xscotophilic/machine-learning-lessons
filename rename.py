import os
import re
import sys
from tabulate import tabulate

def is_valid_snake_case(name):
    """Checks if a name is in valid snake_case format."""
    return re.match(r'^[a-z0-9]+(_[a-z0-9]+)*(\.[a-z]+)?$', name) is not None

def to_snake_case(name):
    """Converts a name to snake_case format."""
    name, ext = os.path.splitext(name)  # Separate name and extension

    if is_valid_snake_case(name):
        return name + ext  # Skip if already in correct format

    name = re.sub(r'[^a-zA-Z0-9. ]', '', name)  # Remove special characters
    name = name.strip()

    if re.match(r'^[0-9]+ ', name):
        name = re.sub(r'^([0-9]+) ', r'\1.', name)  # Replace leading number & space with number.

    name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)  # Convert CamelCase to snake_case
    name = re.sub(r' ', '_', name)  # Replace spaces with underscores
    name = re.sub(r'__+', '_', name)  # Replace multiple underscores with a single underscore
    name = name.lower()
    return name + ext  # Add extension back

def rename_dirs_and_files(root_dir):
    changes = []

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Rename files
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            if ext.lower() not in {".py", ".r", ".ipynb", ".csv"}:  # Ignore .png and .md extensions
                continue
            new_name = to_snake_case(name + ext)
            if filename == new_name:  # Skip if already in correct format
                continue
            old_path = os.path.join(dirpath, filename)
            new_path = os.path.join(dirpath, new_name)
            if old_path != new_path:
                os.rename(old_path, new_path)
                changes.append([filename, new_name])

        # Rename directories
        for dirname in dirnames:
            new_dirname = to_snake_case(dirname)
            if dirname == new_dirname:  # Skip if already in correct format
                continue
            old_dirpath = os.path.join(dirpath, dirname)
            new_dirpath = os.path.join(dirpath, new_dirname)
            if old_dirpath != new_dirpath:
                os.rename(old_dirpath, new_dirpath)
                changes.append([dirname, new_dirname])

    if changes:
        print(tabulate(changes, headers=["Old Name", "New Name"], tablefmt="grid"))
    else:
        print("No changes were made.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    root_directory = sys.argv[1]
    if not os.path.isdir(root_directory):
        print("Error: Provided path is not a directory")
        sys.exit(1)

    rename_dirs_and_files(root_directory)
