def fun(x):
	ele=[]
	a=""
	for i in x:
		if i!=" ":
			a=a+i
		else:
		    if a!="":
		        ele=ele+[a]
		    a=""
	count=len(ele)	
	return count		
