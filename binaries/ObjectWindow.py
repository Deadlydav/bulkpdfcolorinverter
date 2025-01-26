import tkinter as tk

class ObjectWindow:
    def init_window(self, master, width, height, isresizable):
        self.master = master
        self.master.iconbitmap("binaries/icon.ico")
        self.master.title("PDF Inverter")
        self.master.geometry(f"{width}x{height}")
        self.master.resizable(isresizable, isresizable)
        return self
    

    def create_text(self, text, fontsize):
        self.text = tk.Label(self.master, text=text, font=("Open Sans", fontsize))
        self.text.pack()
        return self.text

    def create_button(self, text, fontsize):
        self.button = tk.Button(self.master, text=text, font=("Open Sans", fontsize))
        self.button.pack()
        return self.button

    def create_folder_selector(self):
        self.folder_selector = tk.filedialog.askdirectory()
        return self.folder_selector

    def mainloop(self):
        self.master.mainloop()
        return self


