#WAPP to welcome the user
import datetime
import getpass
un=input("enter username ")
pw=getpass.getpass(prompt="enter password ")
if((un=="kk")and(pw=="123")):
	dt=datetime.datetime.now()
	h=dt.hour
	msg=""
	if(h>=6 and h<=12):
		msg="Good morning"
	elif(h>=12 and h<=16):
		msg="Good afternoon"
	elif(h>=16 and h<=20):
		msg="Good evening"
	else:
		msg="Good night"
	print("Welcome " + un + " " + msg)
else:
	print("invalid login")
		