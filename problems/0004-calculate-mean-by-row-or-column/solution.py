def calculate_matrix_mean(a: list[list[float]], mode: str) -> list[float]:
	rows=len(a)
	cols=len(a[0])
	if mode == 'row':
		means=[]
		for i in a:
			means.append(sum(i)/cols)
	else:
		means=[0]*cols
		for row in a:
			for i in range(len(row)):
				means[i]+=row[i]
		for j in range(cols):
			means[j]/=rows

	return means