import os
import tkinter as tk
from tkinter import font

from binaries.ObjectWindow import ObjectWindow

def launchApp():
    root = tk.Tk()
    app = ObjectWindow().init_window(root, 500, 250, False)
    text_import = app.create_text("Select a PDF file", 15)
    button_import = app.create_button("Import", 10)
    text_export = app.create_text("File location", 15)
    button_export = app.create_button("Export", 10)

    app.mainloop()

if __name__ == "__main__":
    launchApp()