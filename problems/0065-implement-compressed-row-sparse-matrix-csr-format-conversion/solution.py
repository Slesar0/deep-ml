import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	r1=[]
	r2=[]
	r3=[0]
	a=dense_matrix
	rows=len(a)
	cols=len(a[0])
	for i in range(rows):
		for j in range(cols):
			x=a[i][j]
			if x!=0:
				r1.append(x)
				r2.append(j)
		r3.append(len(r1))		
	return r1,r2,r3
	pass
