
def orthogonal_projection(v, L):
	res=[]
	for i in range(len(v)):
		vl=v[i]*L[i]
		ll=L[i]*L[i]
		if L[i]!=0:
			res.append((vl/ll)*L[i])
		else:
			res.append(0)
	return res
	pass
