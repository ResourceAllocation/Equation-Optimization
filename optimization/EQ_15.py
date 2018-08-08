'''
EQ 15
	Ui − Uj +Xij ∑ Yri ≤ ∑ Yri − 1; i != j∈V
				i∈V		i∈V
'''


from sys import *
r=int(argv[1])
v=int(argv[2])
for i in range(1,v+1):
	for j in range(1,v+1):
		if(i == j):
			continue
		pre="U["+str(i)+"] - U["+str(j)+"] + 1 +"
		multi="X["+str(i)+","+str(j)+"] * "
		print (pre,end="")
		for k in range(1,r+1):
			print (multi+"Y["+str(k)+","+str(i)+"] - "+"Y["+str(k)+","+str(i)+"]",end="")
			if(k < r ):
				print (" + ",end="")
		print (" <= 0 ") 
		print  

