import os
import shutil

# Specify the path
path = "C://Users//pauli//Downloads"
destination = "c:\Program Files (x86)\Steam\steamapps\common\Rocksmith2014\dlc\cldc"

# Get the list of all files and directories
dir_list = os.listdir(path)
cdlc_list = os.listdir(destination)

# Filter the list to find files ending with .psarc
psarc_files = [file for file in dir_list if file.endswith('.psarc')]

print("Files and directories in '", path, "' :")

# Print all files
print(dir_list)

to_move = []

# Check if .psarc files are in the destination directory, and if not, add them to the move list
for file in psarc_files:
    if file not in cdlc_list:
        to_move.append(file)

# Move files to the destination directory
if to_move:
    print("Moving files to destination:")
    for file in to_move:
        src_path = os.path.join(path, file)
        dst_path = os.path.join(destination, file)
        shutil.move(src_path, dst_path)
        print(f"Moved {file} to {destination}")
else:
    print("No files to move.")