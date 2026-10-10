import os
import shutil

base_dir = os.path.dirname(__file__)
source_folder = os.path.join(base_dir, "source_files")
destination_folder = os.path.join(base_dir, "JPG_Images")

if not os.path.isdir(source_folder):
    print("Source folder not found!")
    raise SystemExit

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)
    
    if os.path.isfile(source_path) and filename.lower().endswith(".jpg"):
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("JPG file organization completed!")
