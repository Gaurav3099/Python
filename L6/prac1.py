import threading 
class Even(threading.Thread):
	def run(self):
		print("Even thread started")
		f1=open("even.txt","w")
		f2=open("data.txt")
		data=f2.readline()
		while(data):
			if int(data)%2 == 0:
				f1.write(data)
			data=f2.readline()
		f1.close()
		f2.close()
		print("even thread completed")
class Odd(threading.Thread):
	def run(self):
		print("odd thread started")
		f1=open("odd.txt","w")
		f2=open("data.txt")
		data=f2.readline()
		while(data):
			if int(data)%2 != 0:
				f1.write(data)
			data=f2.readline()
		f1.close()
		f2.close()
		print("odd thread completed")
t1=Even()
t1.start()
t1.join()
t2=Odd()
t2.start()

