from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Course feedback")
root.geometry("300x300+400+300")
cf=IntVar()
cf.set(1)
rbExcellent=Radiobutton(root,text="Excellent",variable=cf,value=1)
rbGood=Radiobutton(root,text="Good",variable=cf,value=2)
rbOk=Radiobutton(root,text="Ok",variable=cf,value=3)
rbAverage=Radiobutton(root,text="Average",variable=cf,value=4)
rbExcellent.grid(row=0,column=0,sticky=W)
rbGood.grid(row=1,column=0,sticky=W)
rbOk.grid(row=2,column=0,sticky=W)
rbAverage.grid(row=3,column=0,sticky=W)
def f1():
	f=cf.get()
	msg=""
	if f==1:
		msg="Excellent"
	if f==2:
		msg="Good"
	if f==3:
		msg="Ok"
	else:
		msg="Average"
	messagebox.showinfo("feedback",msg)
btnSubmit=Button(root,text="Submit",command=f1)
btnSubmit.grid(row=4,column=0)
root.mainloop()
