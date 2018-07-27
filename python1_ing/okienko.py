from tkinter import *

class Application(Frame):
    def pokaz_zawartosc(self):
        tekst = self.ITEXT.get(1.0, END)
        print( "zawartosc_okienka!\n%s"%tekst)
        self.OTEXT.delete(1.0, END)
        self.OTEXT.insert(1.0,"\n".join(sorted(set(tekst.splitlines()))).strip())        

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] =  self.quit
        
        self.pokaz = Button(self)
        self.pokaz["text"] = "pokaz...",
        self.pokaz["command"] = self.pokaz_zawartosc
        
        self.ITEXT = Text(self)        
        self.OTEXT = Text(self)       
        self.ISB = Scrollbar(self, command=self.ITEXT.yview) 
        self.ITEXT['yscrollcommand'] = self.ISB.set
        self.QUIT.grid(row=0,column=0)
        self.pokaz.grid(row=0,column=1)
        self.ITEXT.grid(row=1,column=0, columnspan=2,sticky="nsew")
        self.ISB.grid(row=1, column=3, sticky='nsew')
        
        self.OTEXT.grid(row=1,column=4, columnspan=2,sticky="nsew")
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=0, column=0, columnspan=6, sticky=N+S+E+W)
       
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
