from tkinter import PhotoImage, Tk, Label

class WindowClass:
    def __init__(self):
        self.startup()
        self.tk.mainloop()
    
    def startup(self):
        self.tk = Tk()
        self.tk.title("CCF Manager")
        self.tk.resizable(False,False)
        #https://stackoverflow.com/questions/14900510/changing-the-application-and-taskbar-icon-python-tkinter
        self.tk.iconbitmap("./images/logo.png")
        self.tk.eval('tk::PlaceWindow . center')

        #widgets
        self.addToGrid(Label(self.tk,text="College Career Fair Manager",bg="gray",font=("ArialBold",15)),0,0)
        self.addToGrid(Label(self.tk,text="Name"),1,0)
        self.addToGrid(Label(self.tk,text="Logo"),2,0)
        self.addToGrid(Label(self.tk,text="Website"),3,0)
        self.addToGrid(Label(self.tk,text="Description"),4,0)
        self.addToGrid(Label(self.tk,text="Interest Areas"),5,0)
    
    def addToGrid(self,widget,row,column,columnspan=1,sticky="news"):
        widget.grid(row=row,column=column,columnspan=columnspan,sticky=sticky)

    def exit(self):
        self.tk.destroy()

    def setTitle(self,title):
        self.tk.title(title)