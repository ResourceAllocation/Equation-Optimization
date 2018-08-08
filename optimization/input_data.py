import sys
from parse_inputs import*

class inputs(object):
	"""docstring for inputs"""
	def __init__(self):
		x={} 	#	1; if a data mule r visits node j immediately after node i
				#	0; otherwise

		y={}	#	1; if a node i is served by a data mule r
				#	0; otherwise

		z={}	#	1; if node i is alloted a communication tower
				#	0; otherwise
		

		s={}	#	1; if a node i is the depot node for a data mule r
				#	0; otherwise


		l={}	# latency of data mule from i to j

		e={}

	def getdata(self,r,v):
		obj=parse_inputs()
		x=obj.parseX(r,v)
		y=obj.parseY(r,v)
		z=obj.parseZ(r,v)
		s=obj.parseS(r,v)
		l=obj.parseL(r,v)
		e=obj.parseE(r,v)
		return(x,y,z,s,l,e)