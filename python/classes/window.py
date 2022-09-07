from tkinter import Button, OptionMenu, StringVar, Text, Tk, Label
from PIL import Image, ImageTk
from classes.firebase import FirebaseClass
import sys

class WindowClass:
    def __init__(self):
        self.firebase = FirebaseClass()
        self.remember = []
        self.startup()
        self.tk.mainloop()
    
    def startup(self):
        self.tk = Tk()
        self.type = StringVar(value="College")
        self.tk.title("CCF Manager")
        self.tk.resizable(False,False)
        #https://stackoverflow.com/questions/14900510/changing-the-application-and-taskbar-icon-python-tkinter
        try:
            self.tk.iconbitmap(default="./../images/logo.ico")
        except:
            self.tk.iconbitmap(default=f"{sys._MEIPASS}/logo.ico")

        #widgets
        #don't blame me: https://stackoverflow.com/questions/13148975/tkinter-label-does-not-show-image
        try:
            self.img = Image.open("./../images/logo.png").convert("RGBA")
        except:
            self.img = Image.open(f"{sys._MEIPASS}/logo.png").convert("RGBA")
        self.img = ImageTk.PhotoImage(self.img.resize([self.img.size[0]//15,self.img.size[1]//15]))
        self.addToGrid(Label(self.tk,image=self.img,bg="black"),0,0,3)
        self.addToGrid(Label(self.tk,text="College Career Fair Manager",bg="black",fg="white",font=("ArialBold",15)),1,0,3)
        self.addToGrid(Label(self.tk,text="Name"),2,0)
        self.addToGridRemember("name",Text(self.tk,height=3),2,1)
        self.addToGrid(Label(self.tk,text="Logo URL"),3,0)
        self.addToGridRemember("logo",Text(self.tk,height=3),3,1)
        self.addToGrid(Label(self.tk,text="Website URL"),4,0)
        self.addToGridRemember("web",Text(self.tk,height=3),4,1)
        self.addToGrid(Label(self.tk,text="Description"),5,0)
        self.addToGridRemember("desc",Text(self.tk,height=3),5,1)
        self.addToGrid(Label(self.tk,text="Interest Areas"),6,0,3)
        for i in range(5):
            self.addToGrid(Label(self.tk,text=i+1),7+i,0)
            self.addToGridRemember(f"ia{i+1}",Text(self.tk,height=3),7+i,1)
        self.addToGrid(Label(self.tk,text="Type"),998,0)
        self.addToGrid(OptionMenu(self.tk,self.type,*["College","Company","Military"]),998,1,2)
        self.addToGrid(Button(self.tk,text="Submit",bg="darkgreen",fg="lime",command=self.submit),999,0,3) #Not counting this out.

    def addToGridRemember(self,name,widget,row,column,columnspan=1,sticky="news"):
        self.remember.append([name,widget])
        widget.grid(row=row,column=column,columnspan=columnspan,sticky=sticky)

    def addToGrid(self,widget,row,column,columnspan=1,sticky="news"):
        widget.grid(row=row,column=column,columnspan=columnspan,sticky=sticky)

    def submit(self):
        data = {}
        for i in self.remember:
            data[i[0]] = i[1].get("1.0",'end-1c')
            i[1].delete("1.0","end")
        data["type"] = self.type.get()
        self.firebase.new(data)

    def exit(self):
        self.tk.destroy()

    def setTitle(self,title):
        self.tk.title(title)