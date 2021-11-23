from os.path import basename
from zipfile import ZipFile
import os

with ZipFile("G:\\BlueJ_Projects\\archive.zip", "w") as f:
    # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk("G:\\BlueJ_Projects"):
        for filename in filenames:
            # create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            # Add file to zip
            f.write(filePath, basename(filePath))