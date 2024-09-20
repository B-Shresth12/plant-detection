import os
import shutil
import logging

def move_file(source_path, vegetable, folder_name):
    destination_folder = os.path.join('data/predicted_data', vegetable, folder_name)
    os.makedirs(destination_folder, exist_ok=True)

    destination_path = os.path.join(destination_folder, os.path.basename(source_path))
    shutil.move(source_path, destination_path)

    logging.info(f"image moved to {destination_folder}")
