from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Course material")
root.geometry("300x300+400+300")
n=IntVar()
cbNotes=Checkbutton(root,text="Notes",variable=n)
d=IntVar()
cbDvd=Checkbutton(root,text="dvd",variable=d)
c=IntVar()
cbCertificates=Checkbutton(root,text="Certifiactes",variable=c)
cbNotes.grid(sticky=W)
cbDvd.grid(sticky=W)
cbCertificates.grid(sticky=W)
def f1():
	msg=""
	if n.get()==1:
		msg+="Notes " + "\n"
	if d.get() == 1:
		msg+="DVD" + "\n"
	if c.get() ==1:
		msg+="Certificats" +"\n"
	if ((n.get()==0) and (d.get()== 0) and (c.get()==0)):
		messagebox.showinfo("Materials",nothing)
	else:
		messagebox.showinfo("Materials",msg)
		import zerosms
		un="9892836730"
		pw="zxcvbnm"
		sendto="8850377397"
		zerosms.sms(phno=un,passwd=pw,message=msg,receivernum=sendto)
btnSubmit=Button(root,text="Submit",command=f1)
btnSubmit.grid()
root.mainloop()
