from pyomo.environ import *

def equation7(z,c,model):
	x=0
	for i in range(1,len(z)+1):
		x+=z[(i)]
	if(x<=c):
		model.eq.add(Constraint.Feasible)
	else:
		model.eq.add(Constraint.Infeasible)
def equation8(s,z,r,v,model):
	for i in range(1,r):
		for j in range(1,v):
			if(s[(i,j)]<=z[j]):
				model.eq.add(Constraint.Feasible)
			else:
				model.eq.add(Constraint.Infeasible)

'''
Equation 9 

 	∑ Sri= 1,∀r
	i∈V
'''
def equation9(s,r,v,model):
	for i in range(1,r+1):
		x=0

		for j in range(1,v+1):
			x+=s[(i,j)]
		if(x==1):
			model.eq.add(Constraint.Feasible)
		else:
			model.eq.add(Constraint.Infeasible)
			

'''
Equation 10

	Zi + ∑ Yri= 1 +∑ Sri ; ∀i
		r∈R		   r∈R
'''
def equation10(Y,Z,S,r,v,model):
	
	for i in range(1,v+1):
		temp=0
		for j in range(1,r+1):
			temp+=Y[(j,i)]-S[(j,i)]
		temp+=(Z[(i)]-1)
		if(temp==0):
			model.eq.add(Constraint.Feasible)
		else:
			model.eq.add(Constraint.Infeasible)

'''
Equation 11
		
		 ∑ (Xrij+Xrji)-Yri>=0,∀r,i
		 j∈V
'''
def equation11(x,y,r,v,model):
	for i in range(1,r+1):
		for j in range(1,v+1):
			temp=0
			for k in range(1,v+1):
				temp+=x[(i,j,k)] + x[(i,k,j)]
			temp+=(- y[i,j])
			if(temp>=0):
				model.ineq.add(Constraint.Feasible)
			else:
				model.ineq.add(Constraint.Infeasible)

'''
Equation 12
	
	∑ Xrip − ∑ Xrpj = 0 ; ∀ r,p
	i∈V		j∈V
'''

def equation12(X,r,v,model):
	for i in range(1,r+1):
		for j in range(1,v+1):
			temp=0
			for k in range(1,v+1):
				temp+=X[(i,k,j)]- X[(i,j,k)]
			if(temp==0):
				model.eq.add(Constraint.Feasible)
			else:
				model.eq.add(Constraint,Infeasible)

'''
'''
def equation13(Y,Z,S,r,v,model):
	Zi=0
	print(Y)
	print(Z)
	print(S)
	for i in range(1,v+1):
		Zi=Zi+Z[(i)]
	temp=0
	for i in range(1,v+1):
		for j in range(1,r+1):
			print(j,i)
			temp+=(Y[(j,i)]- S[(j,i)])
	print(Zi)
	print(temp)
	print(v)
	if(Zi+temp==v):
		model.eq.add(Constraint.Feasible)
	else:
		model.eq.add(Constraint.Infeasible)


'''
EQ 14 :-
	Xrij ≤ Eij ; ∀i,j,r

'''

def equation14(X,E,r,v,model):
	for i in range(1,v+1):
		for j in range(1,v+1):
			for k in range(1,r+1):
				if(X[(k,i,j)]- E[(i,j)]<=0):
					model.ineq.add(Constraint.Feasible)
				else:
					model.ineq.add(Constraint.Infeasible)
				
'''
EQ 15
	Ui − Uj +Xij ∑ Yri ≤ ∑ Yri − 1; i != j∈V
				i∈V		i∈V
'''


def sum1(y,i,v):
	x=0
	for k in range(1,v):
		x+=y[(i,k)]
	return x
def equation15(X,Y,S,r,v,model):
	temp1=0
	temp2=0
	temp3=0
	for k in range(1,r+1):
		temp1=sum1(Y,k,v)
		for i in range(1,v+1):
			for j in range(1,v+1):
				if(i==j or S[(k,j)]==1):
					continue
				temp2+=(model.U[i]-model.U[j]+1+(temp1*X[(k,i,j)]-temp1)) 
				#print(model.U[i])
				model.eq.add(temp2<=0)
				'''if((temp2)<=0):
					model.eq.add(Constraint.Feasible)
				else:
					model.eq.add(Constraint.Infeasible)  
				'''
