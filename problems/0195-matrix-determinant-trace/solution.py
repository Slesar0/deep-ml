def determinant(m):
	n=len(m)
	det=0
	if n==1:
		det=m[0][0]
	if n==2:
		det=m[0][0]*m[1][1]-m[1][0]*m[0][1]
	else:
		for col in range(n):
			minor=[row[:col]+row[col+1:] for row in m[1:]]
			sign=(-1)**col
			det+=sign*m[0][col]*determinant(minor)
	return det
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	m=matrix
	n=len(m)
	sm=0
	for i in range(n):
		sm+=m[i][i]
	return(determinant(m),sm)
	pass