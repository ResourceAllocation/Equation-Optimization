'''
EQ 14 :-
	Xrij ≤ Eij ; ∀i,j,r

'''

def equation14(X,E,r,v,model):
	for i in range(0,v):
		for j in range(0,v):
			for k in range(0,r):
				m.ineq.add(X[(k,i,j)]- E[(i,j)]<=0)
				