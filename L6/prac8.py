from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("Even or odd")
win.geometry("300x300+400+200")
lblEnterNumber=Label(win,text="enter number ")
entNumber=Entry(win,bd=4)
def eo():
	try:
		s=entNumber.get()
		n=int(s)
		msg=" "
		if n%2 == 0:
			msg="Even"
		else:
			msg="odd"
		messagebox.showinfo("Jawab",msg)
	except ValueError:
		messagebox.showerror("issue","enter integers only")
		entNumber.delete(0,END)
		ent.Number.focus()
def eo1(event):
	try:
		s=entNumber.get()
		n=int(s)
		msg=" "
		if n%2 == 0:
			msg="Even"
		else:
			msg="odd"
		messagebox.showinfo("Jawab",msg)
	except ValueError:
		messagebox.showerror("issue","enter integers only")
		entNumber.delete(0,END)
		ent.Number.focus()
btnFind=Button(win,text="Find",command=eo)
btnFind.bind("<Return>",eo1)
lblEnterNumber.pack(pady=10)
entNumber.pack(pady=10)
btnFind.pack(pady=10)
entNumber.focus()
def ex():
	ans=messagebox.askyesno("Exit" , "are u leaving")
	if ans:
		ans1=messagebox.askyesno("Exit","r u sure")
		if ans1:
			import sys
			sys.exit()
win.protocol("WM_DELETE_WINDOW",ex)
win.mainloop()
