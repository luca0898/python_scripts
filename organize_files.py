import os
import shutil

def organize_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(src_dir):
        source_path = os.path.join(src_dir, filename)


        if os.path.isfile(source_path) and not filename.startswith('.'):
    
            _, file_extension = os.path.splitext(filename)

    
            destination_subdir = os.path.join(dest_dir, file_extension[1:].lower())

    
            if not os.path.exists(destination_subdir):
                os.makedirs(destination_subdir)

    
            destination_path = os.path.join(destination_subdir, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to '{destination_subdir}'")

if __name__ == "__main__":
    source_directory = input("Enter the source directory: ")

    destination_directory = input("Enter the destination directory: ")

    organize_files(source_directory, destination_directory)
