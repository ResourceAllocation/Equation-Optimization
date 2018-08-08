from pyomo.environ import *
from input_data import *
from Equations import *
import sys
#Defined object of pyomo package
model=ConcreteModel()
model.eq=ConstraintList()
model.ineq=ConstraintList()

def print_inputs(x,y,z,s,l,e):
	print("X = ",end=" ")
	print(x,end="\n\n")
	print("Y = ",end=" ")
	print(y,end="\n\n")
	print("Z = ",end=" ")
	print(z,end="\n\n")
	print("S = ",end=" ")
	print(s,end="\n\n")
	print("L = ",end=" ")
	print(l,end="\n\n")
	print("E= ",end=" ")
	print(e,end="\n\n")

def set_constraints():
	equation7(z,c,model)
	equation8(s,z,r,v,model)
	equation9(s,r,v,model)
	print("done 9")
	equation10(y,z,s,r,v,model)
	equation11(x,y,r,v,model)
	equation12(x,r,v,model)
	equation13(y,z,s,r,v,model)
	equation14(x,e,r,v,model)
	equation15(x,y,s,r,v,model)
def objective_function():
	temp=0
	mai=-1000000000
	for k in range(1,r+1):
		temp=0
		for i in range(1,v+1):
			for j in range(1,v+1):
				temp+=l[(k,i,j)]*x[(k,i,j)]
		mai=max(mai,temp)	
	return mai
r=3
v=8
c=2

# Taking the inputs 
input_obj=inputs()
(x,y,z,s,l,e)=input_obj.getdata(r,v)

model.IDX = range(10)
model.U = Var(model.IDX,bounds = (-100000,10000))
#print_inputs(x,y,z,s,l,e)
set_constraints()
model.TotalLatency = Objective(expr = objective_function(), sense=minimize)
opt = SolverFactory("glpk")
results = opt.solve(model, tee=True)
print(results)
