# Import Tkinter module
from Tkinter import *
#instantiate Tk library
window = Tk()
#set background color 
window.configure(background="white")
#set window title
window.title("SOFIA")
# set window size
window.geometry("400x400")

window.attributes("-fullscreen", True)


MyButton1 = Button(window, text="INICIAR",width=20)
MyButton1.pack_propagate(0) # don't shrink
MyButton1.pack(padx=200,pady=350)    

# b = Button(window, text="Sure!")
# b.pack(fill=BOTH, expand=1)


window.mainloop()