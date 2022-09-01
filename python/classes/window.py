from tkinter import Tk

class WindowClass:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("CCF Manager")
        self.tk.mainloop()
    
    def setTitle(self,title):
        self.tk.title(title)