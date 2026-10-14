import numpy as np

def make_diagonal(x):
	x=x.tolist()
	cnt=0
	res=[[0]*len(x) for _ in range(len(x))]
	for i in res:
		i[cnt]=x[cnt]
		cnt+=1
	return res
	pass