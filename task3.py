import os
import shutil

source_folder = "images"
destination_folder = "moved_images"

os.makedirs(destination_folder, exist_ok=True)

if os.path.exists(source_folder):
    count = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                print("Moved:", filename)
                count += 1

    print("Task automation completed!")
    print("Total files moved:", count)

else:
    print("Please create the images folder first.")