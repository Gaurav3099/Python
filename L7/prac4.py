import cx_Oracle
con=None
try:
	con=cx_Oracle.connect("system/abc123")
	print("u r connected")
	while True:
		choice=int(input("1 add student, 2 view student and 3 exit"))
		if (choice==1):
			rno=int(input("Enter rno "))
			name=input("enter name ")
			cursor=con.cursor()
			sql="insert into student values('%d','%s')"
			args=(rno,name)
			cursor.execute(sql % args)
			con.commit()
			print(cursor.rowcount,"rows inserted")
		elif(choice==2):
			cursor=con.cursor()
			sql="select*from student"
			cursor.execute(sql)
			rec=cursor.fetchall()
			for r in rec:
					rno=r[0]
					name=r[1]
					print("Rno: ",rno, "Name: ",name)
		elif(choice == 3):
			break
		else:
			print("invalid choice")
except cx_Oracle.DatabaseError as e:
	con.rollback()
	print('issue',e)
finally:
	cursor.close()
	if con is not None:
		con.close()
		print("u r no longer connected")