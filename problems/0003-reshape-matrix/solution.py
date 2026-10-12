
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	
	new_rows, new_cols = new_shape

	reshaped_matrix =[] 

	if new_cols*new_rows!=len(a)*len(a[0]):
		return []

	m=[]
	cnt=0
	for row in a:
		for i in range(len(a[0])):
			cnt+=1
			m.append(row[i])
			if cnt==new_cols:
				reshaped_matrix.append(m)
				m=[]
				cnt=0

	return reshaped_matrix