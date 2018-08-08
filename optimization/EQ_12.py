'''
Equation 12
	
	∑ Xrip − ∑ Xrpj = 0 ; ∀ r,p
	i∈V		j∈V
'''

def equation12(X,r,v,model):
	for i in range(0,r):
		for j in range(0,p):
			temp=0
			for k in range(0,v):
				temp+=X[(i,k,j)]- X[(i,j,k)]
			model.eq.add(temp==0)