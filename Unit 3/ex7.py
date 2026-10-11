
import shutil
import os

# Copy a file
shutil.copy("data.txt", "copy_data.txt")
print("File copied successfully!")

# Move a file
shutil.move("copy_data.txt", "moved_data.txt")
print("File moved successfully!")

# Delete a file
os.remove("moved_data.txt")
print("File deleted successfully!")
