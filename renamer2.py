import os
import random
import shutil

def split_train_val(source_dir, train_dir, val_dir, split_ratio=0.8, selected_dirs=None):
    # Create train and val directories if they don't exist
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    # Iterate through specified directories only
    for class_dir in selected_dirs:
        full_dir_path = os.path.join(source_dir, class_dir)
        if os.path.isdir(full_dir_path):
            class_files = os.listdir(full_dir_path)
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

            # Copy val files to val directory
            for file_name in val_files:
                src_file = os.path.join(source_dir, class_dir, file_name)
                dest_file = os.path.join(val_dir, class_dir, file_name)
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copyfile(src_file, dest_file)

    print("Splitting completed for selected directories.")

# Example usage
source_directory = 'data'
train_directory = 'data/train'
val_directory = 'data/val'
selected_directories = ['W', 'X', 'Y', 'Z']  # Directories to split

split_train_val(source_directory, train_directory, val_directory, selected_dirs=selected_directories)
