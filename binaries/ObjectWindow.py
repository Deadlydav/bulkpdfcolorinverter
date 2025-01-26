import tkinter as tk

class ObjectWindow:
    def window(self, master):
        self.master = master
        self.master.title("PDF Inverter")

        return self

    def editWindowSize(self, width, height):
        self.master.configure(width=width, height=height)

        return self

    def mainloop(self):
        self.master.mainloop()

        return self

