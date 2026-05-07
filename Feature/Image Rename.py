import os

# Path to your folder
folder_path = r"D:\\Basharul\\Cow Muzzle\\Dataset"

# Get list of files in the folder
files = os.listdir(folder_path)

# Filter only image files (optional)
image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
images = [f for f in files if f.lower().endswith(image_extensions)]

# Sort files if needed
images.sort()

# Get starting number from user input
start_number = int(input("Enter the starting number for renaming: "))

# Rename files sequentially
for idx, filename in enumerate(images, start=start_number):
    ext = os.path.splitext(filename)[1]  # keep original extension
    new_name = f"{idx}{ext}"
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("Renaming complete!")