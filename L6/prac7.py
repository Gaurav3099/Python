from tkinter import *
root = Tk()
root.geometry("300x300+300+300")
root.title("Colors ")
def c(num):
	if num == 1:
		root.configure(background="RED")
	elif num == 2:
		root.configure(background="GREEN")
	else:
		root.configure(background="BLUE")
btnRed=Button(root,text="Red",width=10, command=lambda:c(1))
btnGreen=Button(root,text="Green",width=10, command=lambda:c(2))
btnBlue=Button(root,text="Blue",width=10, command=lambda:c(3))
btnRed.pack(pady=10)
btnGreen.pack(pady=10)
btnBlue.pack(pady=10)
root.mainloop()