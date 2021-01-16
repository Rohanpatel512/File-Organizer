from tkinter import *
from tkinter import ttk
import window
import os
import shutil

# Create an instance of the window class
app = window.Window("File Organizer", 400, 100, False)

# Method to sort files into specific folders
def sortFiles(files, path):

    # Local variables
    fileType = ""
    index = 0

    # Loop through all the files
    for file in files:
        # Try
        try:
            # Get the index of the '.' and store in variable
            index = file.index('.')
        except:
            # Continue to the next file
            continue

        # Get the file type and store in variable
        fileType = file[index + 1:len(file)]

        # Move the file to its corresponding folder
        shutil.move(path + "\\" + file, path + "\\" + fileType)

# Method to create folders for each of the specific files
def createFolders(files, path):

    # Local variables
    fileType = ""
    index = 0

    # Loop through all the file types
    for file in files:
        # Get the index of the '.' and store in variable
        index = file.index('.')

        # Get the file type and store in variable
        fileType = file[index + 1:len(file)]

        # Try
        try:
            # Create the folder for the file
            os.mkdir(path + "//" + fileType)
        except:
            # Do nothing
            pass

    # Call method to sort the files
    sortFiles(files, path)

# Method to get all files within folder
def getFiles(event):

    # Get path to the folder and store in variable
    path = app.pathInput.get()

    # Get all the files within the path directory
    files = os.listdir(path)

    # Call method to create folders for each of the files
    createFolders(files, path)

# Bind the button to hear for clicks
app.sortButton.bind("<Button-1>", getFiles)

# Call all methods within window.py file
app.displayWindow()
app.addComponents()
