folder="./inputs/"
class parse_inputs(object):
	"""docstring for parse_inputs"""
	def ThreeD_Array(self,a,b,c): # Initializing 3D Array with 0
		temp={}
		for i in range(1,a+1):
			for j in range(1,b+1):
				for k in range(1,c+1):
					temp[(i,j,k)]=0
		return temp
	def TwoD_Array(self,a,b): # Initializing 2D Array with 0
		temp={}
		for i in range(1,a+1):
			for j in range(1,b+1):
				temp[(i,j)]=0
		return temp
	def parseX(self,r,v):
		temp={}
		temp=self.ThreeD_Array(r,v,v)
		fil=open(folder+"x.txt","r")
		data=fil.read()
		data=data.split("\n")
		n=len(data)
		for i in range(1,n-1):
			data[i]=data[i].split(",")
			temp[(int(data[i][0]),int(data[i][1]),int(data[i][2]))]=1
		fil.close()
		print("X= ")
		print(temp)
		return temp
	def parseY(self,r,v):
		temp={}
		temp=self.TwoD_Array(r,v)
		fil=open(folder+"y.txt","r")
		data=fil.read()
		data=data.split("\n")
		n=len(data)
		for i in range(1,n-1):
			data[i]=data[i].split(",")
			#print(data[i])
			temp[(int(data[i][1]),int(data[i][0]))]=1
		print("Y= ")
		print(temp)
		fil.close()
		return temp
	def parseZ(self,r,v):
		temp={}
		for i in range(1,v+1):
			temp[(i)]=0
		fil=open(folder+"z.txt","r")
		data=fil.read()
		data=data.split("\n")
		n=len(data)
		for i in range(1,n-1):
			data[i]=data[i].split(",")
			#print(data[i])
			temp[(int(data[i][0]))]=int(data[i][1])
		print("Z= ")
		print(temp)
		fil.close()
		return temp
	
	def parseS(self,r,v):
		temp={}
		temp=self.TwoD_Array(r,v)
		fil=open(folder+"s.txt","r")
		data=fil.read()
		data=data.split("\n")
		n=len(data)
		for i in range(1,n-1):
			data[i]=data[i].split(",")
			#print(data[i])
			temp[(int(data[i][0]),int(data[i][1]))]=1
		print("S= ")
		print(temp)
		fil.close()
		return temp
	def parseL(self,r,v):
		temp={}
		temp=self.ThreeD_Array(r,v,v)
		fil=open(folder+"l.txt","r")
		data=fil.read()
		data=data.split("\n")
		n=len(data)
		for i in range(1,n-1):
			data[i]=data[i].split(",")
			#print(data[i])
			temp[(int(data[i][0]),int(data[i][1]),int(data[i][2]))]=float(data[i][3])
		print("L = ")
		print(temp)
		fil.close()
		return temp
	def parseE(self,r,v):
		temp={}
		temp=self.TwoD_Array(v,v)
		fil=open(folder+"e.txt","r")
		data=fil.read()
		data=data.split("\n")
		n=len(data)
		for i in range(1,n-1):
			data[i]=data[i].split(",")
			for j in range(0,v+1):
				temp[(i,j)]=float(data[i][j-1])
		print("E = ")
		print(temp)
		fil.close()
		return temp
'''
obj=parse_inputs()
obj.parseX(r,v)
obj.parseY(r,v)
obj.parseZ(r,v)
obj.parseS(r,v)
obj.parseL(r,v)
obj.parseE(r,v)
'''