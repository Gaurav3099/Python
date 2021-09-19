from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("pizza")
root.geometry("300x300+400+300")

p=IntVar()
p.set(1)
rbSmall=Radiobutton(root,text="Small",variable=p,value=1)
rbMedium=Radiobutton(root,text="Medium",variable=p,value=2)
rblarge=Radiobutton(root,text="Large",variable=p,value=3)
ch=IntVar()
cbCheese=Checkbutton(root,text="Cheese",variable=ch)
o=IntVar()
cbOnion=Checkbutton(root,text="Onion",variable=o)
c=IntVar()
cbCorn=Checkbutton(root,text="Corn",variable=c)
ca=IntVar()
cbCapsicum=Checkbutton(root,text="Capsicum",variable=ca)
cbCheese.grid(row=1,column=1)
cbOnion.grid(row=1,column=2)
cbCorn.grid(row=2,column=1)
cbCapsicum.grid(row=2,column=2)

rbSmall.grid(row=0,column=1)
rbMedium.grid(row=0,column=2)
rblarge.grid(row=0,column=3)
def f1():
	f=p.get()
	msg=""
	if f==1:
		msg="small "
	if f==2:
		msg="medium "
	if f==3:
		msg="large "
	if ch.get()==1:
		msg+="Cheese " + "\n"
	if o.get() == 1:
		msg+="onion " + "\n"
	if c.get() ==1:
		msg+="corn " + "\n"
	if ca.get() ==1:
		msg+="capsicum " + "\n"
	
	messagebox.showinfo("order",msg)

btnOrder=Button(root,text="Order",command=f1)
btnOrder.grid(row=4,column=0)
root.mainloop()
