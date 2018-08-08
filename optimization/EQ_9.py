
'''
Equation 9 

 	∑ Sri= 1,∀r
	i∈V
'''
def equation9(s,r,v,model):
	for i in range(0,r):
		x=0
		for j in range(0,v):
			x+=s[(i,j)]
		model.eq.add(x==1)