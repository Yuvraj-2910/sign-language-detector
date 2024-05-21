import os
import string
import shutil
import random

def rename_directories(base_path):
    # Check if the base path exists
    if not os.path.exists(base_path):
        print(f"Error: The directory {base_path} does not exist.")
        return
    
    # Generate a dictionary mapping numbers to letters (0 -> A, 1 -> B, ...)
    num_to_alpha = {str(i): letter for i, letter in enumerate(string.ascii_uppercase)}

    # List directories in the base path
    directories = os.listdir(base_path)
    for dir_name in directories:
        full_dir_path = os.path.join(base_path, dir_name)
        if os.path.isdir(full_dir_path) and dir_name.isdigit():  # Check if it's a directory and named with digits
            new_name = num_to_alpha.get(dir_name)
            if new_name is not None:
                new_dir_path = os.path.join(base_path, new_name)
                # Rename the directory
                os.rename(full_dir_path, new_dir_path)
                print(f"Renamed {full_dir_path} to {new_dir_path}")
            else:
                print(f"No letter mapping for directory named {dir_name}")
        else:
            print(f"Skipping {full_dir_path}: not a digit-named directory or is not a directory")


def split_train_val(source_dir, train_dir, val_dir, split_ratio=0.8):
    # Create train and val directories if they don't exist
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    # Iterate through each directory in the source directory
    for class_dir in os.listdir(source_dir):
        if os.path.isdir(os.path.join(source_dir, class_dir)):
            class_files = os.listdir(os.path.join(source_dir, class_dir))
            random.shuffle(class_files)  # Shuffle the files for randomness in split
            split_index = int(len(class_files) * split_ratio)

            # Split files into train and val sets
            train_files = class_files[:split_index]
            val_files = class_files[split_index:]

            # Copy train files to train directory
            for file_name in train_files:
                src_file = os.path.join(source_dir, class_dir, file_name)
                dest_file = os.path.join(train_dir, class_dir, file_name)
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copyfile(src_file, dest_file)

            # Copy va l files to val directory
            for file_name in val_files:
                src_file = os.path.join(source_dir, class_dir, file_name)
                dest_file = os.path.join(val_dir, class_dir, file_name)
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copyfile(src_file, dest_file)

    print("Splitting completed.")

# Example usage
# base_path = 'data'
# rename_directories(base_path)

source_directory = 'data'
train_directory = 'data/train'
val_directory = 'data/val'

split_train_val(source_directory, train_directory, val_directory)
