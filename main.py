import os
import tkinter as tk

from binaries.ObjectWindow import ObjectWindow

def launchApp():
    root = tk.Tk()
    app = ObjectWindow.window(ObjectWindow, root)
    app.editWindowSize(app, 500, 250)
    app.mainloop(app)

if __name__ == "__main__":
    launchApp()