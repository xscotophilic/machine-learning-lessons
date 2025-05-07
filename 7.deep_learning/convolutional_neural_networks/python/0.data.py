import os
import shutil
import subprocess

REPO_URL = "https://github.com/laxmimerit/dog-cat-full-dataset.git"
CLONE_DIR = "dog-cat-full-dataset"
TARGET_DIR = "data"

# Skip if data directory already exists
if os.path.exists(TARGET_DIR):
    print(f"'{TARGET_DIR}' directory already exists. Skipping download.")
else:
    # Step 1: Clone the repo
    print("Cloning repository...")
    subprocess.run(["git", "clone", REPO_URL], check=True)

    # Step 2: Move the 'data' directory
    data_path = os.path.join(CLONE_DIR, TARGET_DIR)
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"'data' directory not found in repo: {data_path}")

    print("Moving 'data' directory to current directory...")
    shutil.move(data_path, TARGET_DIR)

    # Step 3: Remove the rest of the repo
    print("Cleaning up...")
    shutil.rmtree(CLONE_DIR)

    print("Done. Only 'data' directory is kept.")
