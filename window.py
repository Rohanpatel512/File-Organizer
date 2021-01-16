from tkinter import *
from tkinter import ttk

class Window():

    # Global variables
    title = ""
    width = 0
    height = 0
    resize = False

    # Constructs the main window
    def __init__(self, title, width, height, resize):
        # Initialize all window frame variables and GUI components
        self.title = title
        self.width = width
        self.height = height
        self.resize = resize
        self.window = Tk()
        self.text = Label(text="Please enter the path to folder:")
        self.pathInput = Entry(width=50)
        self.sortButton = Button(text="OK", width=20)

    # Creates and displays window
    def displayWindow(self):

        # Create the window frame
        self.window.title(self.title)
        self.window.geometry("{}x{}".format(self.width, self.height))
        self.window.resizable(width=self.resize, height=self.resize)

    # Method to create and display components
    def addComponents(self):

        # Display the components
        self.text.grid(row=0, column=1, pady=5, sticky=W)
        self.pathInput.grid(row=1, column=1, pady=5, sticky=W)
        self.sortButton.grid(row=2, column=1, pady=5, sticky=W)

        # Display the window
        self.window.mainloop()