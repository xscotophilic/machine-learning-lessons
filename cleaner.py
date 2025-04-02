import os

def delete_empty_dirs(path):
    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            if not os.listdir(dir_full_path):  # Check if directory is empty
                os.rmdir(dir_full_path)
                print(f"Deleted empty directory: {dir_full_path}")

if __name__ == "__main__":
    root_dir = input("Enter the directory to clean up: ")
    if os.path.exists(root_dir) and os.path.isdir(root_dir):
        delete_empty_dirs(root_dir)
        print("Cleanup completed.")
    else:
        print("Invalid directory path.")
