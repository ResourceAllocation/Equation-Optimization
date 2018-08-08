'''
Equation 10

	Zi + ∑ Yri= 1 +∑ Sri ; ∀i
		r∈R		   r∈R
'''
def equation10(y,z,s,r,v,model):
	for i in range(0,v):
		temp=0
		for j in range(0,r):
			temp+=Y[(j,i)]-S[(j,i)]
		temp+=Z[(i)]-1
		model.eq.add(temp==0)