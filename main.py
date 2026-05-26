import os
import shutil

# 1. Define the directory you want to clean up
# (By default, this targets your computer's Downloads folder)
TRACK_FOLDER = os.path.expanduser("~/Downloads")

# 2. Define your folder mapping based on file extensions
DEST_FOLDERS = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".zip": "Archives"
}

def clean_folder():
    # Loop through every file in the target folder
    for filename in os.listdir(TRACK_FOLDER):
        file_path = os.path.join(TRACK_FOLDER, filename)
        
        # Skip if it's a folder, we only want files
        if os.path.isdir(file_path):
            continue
            
        # Extract the file extension (e.g., '.pdf')
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Check if the extension matches one of our destination folders
        if file_ext in DEST_FOLDERS:
            folder_name = DEST_FOLDERS[file_ext]
            target_dir = os.path.join(TRACK_FOLDER, folder_name)
            
            # Create the subfolder if it doesn't exist yet
            os.makedirs(target_dir, exist_ok=True)
            
            # Move the file
            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f"Moved: {filename} -> {folder_name}/")

if __name__ == "__main__":
    clean_folder()
    print("Folder cleanup complete!")
