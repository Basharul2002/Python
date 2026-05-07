import os
import shutil

def delete_dot_underscore_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        # Delete files starting with "._"
        for file in files:
            if file.startswith("._"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

        # Delete folders starting with "._"
        for dir_name in dirs:
            if dir_name.startswith("._"):
                dir_path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Deleted folder: {dir_path}")
                except Exception as e:
                    print(f"Error deleting folder {dir_path}: {e}")

# 🔹 Change this to your target directory
target_directory = r"D:\cow-image-dataset\images"

delete_dot_underscore_files(target_directory)