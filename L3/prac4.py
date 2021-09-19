#WAPP to check wheather two string are anagram
s1=input("enter first string ")
s2=input("enter second string ")
st1=sorted(s1)
st2=sorted(s2)
print(st1)
print(st2)
if(st1 == st2):
	print("yes they are anagram")
else:
	print("they are not")