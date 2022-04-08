file1=open(‘myfile.txt’)
file2=open(‘mynew.txt’,’w’)
for line i9n file1:
	if ‘a’ in line:
		line=line.replace(‘a’, ‘ ‘)
	else:
		file2.write(line)
file1.close()
