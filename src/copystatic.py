import os
import shutil

source_dir_path = "./static"
dest_dir_path = "./public"

def clear_directory(dest_dir_path):
    if os.path.exists(dest_dir_path):
        for filename in os.listdir(dest_dir_path):
            file_path = os.path.join(dest_dir_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)  # Delete the file
            else:  # It's a directory
                clear_directory(file_path)  # Recursively clear it
                os.rmdir(file_path)

def copy_files_recursive(source_dir_path, dest_dir_path):
    # Clear the destination only if it's the top-level call
    if os.path.abspath(source_dir_path) == "./static":
        clear_directory(dest_dir_path)

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)