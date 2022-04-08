file1=open(r’myfile.txt’,’r’)
v,c,u,l=0
str1=file1.read()
for I in str1:
	if(i>=’a’ and i<=’z’):
		l+=i
	elif (i>=’A andi<=’Z’):
		u+=i
for j in str1:
	j=j.lower()
	if(j==’a’ or j==’e’ or j==’i’ or j==’o’ or j==’u’):
		v+=1
	else:
		if j.isalpha():
			c+=1
print(“ lower case count”,l)
print(“ upper case count”,u)
print(“ vowels count”,v)
print(“ consonants count”,u)
