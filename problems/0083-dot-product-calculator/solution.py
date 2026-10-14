import numpy as np

def calculate_dot_product(vec1, vec2):
	v1=vec1.tolist()
	v2=vec2.tolist()
	r=0
	for i in range(len(v1)):
		r+=v1[i]*v2[i]
	return r
	pass