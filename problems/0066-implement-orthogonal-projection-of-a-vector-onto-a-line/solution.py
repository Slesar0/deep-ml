
def orthogonal_projection(v, L):
	vl=[]
	ll=[]
	res=[]
	for i in range(len(v)):
		vl.append(v[i]*L[i])
		ll.append(L[i]*L[i])
		if L[i]!=0:
			res.append((vl[i]/ll[i])*L[i])
		else:
			res.append(0)
	return res
	pass
