'''
'''
def equation13(Y,Z,S,r,v,model):
	Zi=0
	for i in range(0,v):
		Zi=Zi+Z[(i)]
	for i in range(0,v):
		temp=0
		for j in range(0,r):
			temp+=Y[(j,i)]- S[(j,i)]
		model.eq.add(Zi+temp==v)