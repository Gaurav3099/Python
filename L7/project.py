from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle
root =Tk()
root.title("Student Management System ")
root.geometry("300x300+300+300")


visit =Toplevel(root)
visit.title("View Student ")
visit.geometry("300x300+300+300")
visit.withdraw()
stDataView=scrolledtext.ScrolledText(visit, width=30, height=10)

def f4():
	root.deiconify()
	visit.withdraw()
	stDataView.delete('1.0',END)
btnBackView=Button(visit, text="Back", command=f4)
stDataView.pack()
btnBackView.pack()

adst=Toplevel(root)
adst.title("Add student")
adst.geometry("300x300+300+300")
lblRnoAdd=Label(adst, text="Rno")
entRnoAdd=Entry(adst, bd=5)
lblNameAdd=Label(adst, text="Name")
entNameAdd=Entry(adst, bd=5)

upd=Toplevel(root)
upd.title("Update Student")
upd.geometry("300x300+300+300")

delete = Toplevel(root)
delete.title("Delete")
delete.geometry("300x300+300+300")
lblRnodel=Label(delete, text="Rno")
entRnodel=Entry(delete, bd=5)
def f11():
	root.deiconify()
	delete.withdraw()
btnBackdel=Button(delete, text="Back", command=f11)
def f10():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		r=entRnodel.get()
		if len(r) == 0:
			messagebox.showerror("issue", 'rno is empty')
			entRnoupd.focus()
			return
		
		rno=int(r)
		
		
		cursor=con.cursor()
		sql="delete from student  where rno='%d'"
		args=(rno)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+ " row deleted"
		messagebox.showinfo("Success", msg)
	except cx_Oracle.DatabaseError as e:
			if con is not None:
				con.rollback()
			messagebox.showerror("Failure",e)
			
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
	
btnDeleteS=Button(delete, text="Delete Student", command=f10)
lblRnodel.pack(pady=10)
entRnodel.pack(pady=10)
btnDeleteS.pack(pady=10)
btnBackdel.pack(pady=10)
delete.withdraw()


def f8():
	root.deiconify()
	upd.withdraw()
btnBackupd=Button(upd, text="Back", command = f8)
lblRnoupd=Label(upd, text="Rno")
entRnoupd=Entry(upd, bd=5)
lblNameupd=Label(upd, text="Name")
entNameupd=Entry(upd, bd=5)
def f9():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		r=entRnoupd.get()
		if len(r) == 0:
			messagebox.showerror("issue", 'rno is empty')
			entRnoupd.focus()
			return
		n=entNameupd.get()
		if len(n) == 0:
			messagebox.showerror("issue", 'Name is empty')
			entNameAdd.focus()
			return
		rno=int(r)
		name=n
		cursor=con.cursor()
		cursor=con.cursor()
		sql="update student set name='%s' where rno='%d'"
		args=(name,rno)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+ " row updated"
		messagebox.showinfo("Success", msg)
	except cx_Oracle.DatabaseError as e:
			if con is not None:
				con.rollback()
			messagebox.showerror("Failure",e)
			
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		
btnUpdateupd=Button(upd, text="Update Student", command=f9)

lblRnoupd.pack(pady=10)
entRnoupd.pack(pady=10)
lblNameupd.pack(pady=10)
entNameupd.pack(pady=10)
btnUpdateupd.pack(pady=10)
btnBackupd.pack(pady=10)
upd.withdraw()


def f7():
	delete.deiconify()
	root.withdraw()
	
	


def f5():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		r=entRnoAdd.get()
		if len(r) == 0:
			messagebox.showerror("issue", 'rno is empty')
			entRnoAdd.focus()
			return
		n=entNameAdd.get()
		if len(n) == 0:
			messagebox.showerror("issue", 'Name is empty')
			entNameAdd.focus()
			return
		rno=int(r)
		name=n
		cursor=con.cursor()
		sql="insert into student values('%d','%s')"
		args=(rno,name)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+ " row inserted"
		messagebox.showinfo("Success", msg)



	except cx_Oracle.DatabaseError as e:
			if con is not None:
				con.rollback()
			messagebox.showerror("Failure",e)
			
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		entRnoAdd.delete(0,END)
		entNameAdd.delete(0,END)
		entRnoAdd.focus()
btnSaveAdd=Button(adst, text="Save", command=f5)
def f2():
	root.deiconify()
	adst.withdraw()
btnBackAdd=Button(adst, text="Back", command = f2)
lblRnoAdd.pack(pady=10)
entRnoAdd.pack(pady=10)
lblNameAdd.pack(pady=10)
entNameAdd.pack(pady=10)
btnSaveAdd.pack(pady=10)
btnBackAdd.pack(pady=10)
adst.withdraw()
def f1():
	adst.deiconify()
	root.withdraw()
btnAdd=Button(root,text="Add",width=10,command=f1)
def f3():
	visit.deiconify()
	root.withdraw()
	import cx_Oracle
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="select*from student"
		cursor.execute(sql)
		rec=cursor.fetchall()
		data=""
		for r in rec:
			rno=r[0]
			name=r[1]
			data=data + "Rno: " + str(rno) + "Name :" + name + "\n"
		stDataView.insert(INSERT, data)
	except cx_Oracle.DatabaseError as e:
		print("issue",e)
	finally:
		cursor.close()
		if con is not None:
			con.close()
def f6():
	upd.deiconify()
	root.withdraw()
	


btnView=Button(root, text="View", width=10,command=f3)
btnUpdate=Button(root,text="Update", width=10, command=f6)
btnDelete=Button(root,text="Delete", width=10, command=f7)
btnAdd.pack(pady=20)
btnView.pack(pady=20)
btnUpdate.pack(pady=20)
btnDelete.pack(pady=20)
root.mainloop()