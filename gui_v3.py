

# from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from Tkinter import *
from ttk import Frame, Label, Entry


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

        
    def initUI(self):
      
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill=X)

        MyButton1 = Button(frame1, text="INICIAR", width=10)
        MyButton1.pack(padx=200,pady=350)         
              

def main():
  
    root = Tk()
    root.configure(background="white")
    root.geometry("300x300+300+300")
    root.attributes("-fullscreen", True)
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  