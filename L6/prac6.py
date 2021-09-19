from tkinter import *
root = Tk()
root.geometry("300x300+300+300")
root.title("Colors ")
def red():
	root.configure(background="RED")
def green():
	root.configure(background="GREEN")
def blue():
	root.configure(background="BLUE")
btnRed=Button(root,text="Red",width=10, command=red)
btnGreen=Button(root,text="Green",width=10, command=green)
btnBlue=Button(root,text="Blue",width=10, command=blue)
btnRed.pack(pady=10)
btnGreen.pack(pady=10)
btnBlue.pack(pady=10)
root.mainloop()