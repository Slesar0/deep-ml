import numpy as np

def cosine_similarity(v1, v2):
	v1=v1.tolist()
	v2=v2.tolist()
	smv=0
	ddv2=0
	dv1=0
	dv2=0
	for i in range(len(v1)):
		dv1+=v1[i]**2
		dv2+=v2[i]**2
		smv+=v1[i]*v2[i]
	return (smv)/((dv1**0.5)*(dv2**0.5))
	pass