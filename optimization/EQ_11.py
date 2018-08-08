'''
Equation 11
		
		 ∑ (Xrij+Xrji)-Yri>=0,∀r,i
		 j∈V
'''
def equation11(x,y,r,v,model):
	for i in range(0,r):
		for j in range(0,v):
			temp=0
			for k in range(0,v):
				temp+=x[(i,j,k)] + x[(i,k,j)]
			temp+=(- y[i,j])
			model.ineq.add(temp>=0)