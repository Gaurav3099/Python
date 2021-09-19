#average of three float numbers from CL
import sys
n1=float(sys.argv[1])
n2=float(sys.argv[2])
n3=float(sys.argv[3])
res = n1+n2+n3/3
print('Average = ',res)
print('Average=%7.2f'%res)