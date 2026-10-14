import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	a=data
	p=degree
	res=[[0]*(p+1) for _ in range(len(a))]
	for i in range(len(a)):
		for j in range(p+1):
			res[i][j]=a[i]**j
	return res
	pass