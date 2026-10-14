def compressed_col_sparse_matrix(dense_matrix):
	a=dense_matrix
	r1=[]
	r2=[]
	r3=[0]
	rows=len(a)
	cols=len(a[0])
	for col in range(cols):
		for row in range(rows):
			x=a[row][col]
			if x!=0:
				r1.append(x)
				r2.append(row)
		r3.append(len(r1))
	return r1,r2,r3
	pass
