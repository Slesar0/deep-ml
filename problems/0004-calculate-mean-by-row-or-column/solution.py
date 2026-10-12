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
		means=[x / rows for x in means]

	return means