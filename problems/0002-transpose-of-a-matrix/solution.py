def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    dl=len(a)
    dl2=len(a[0])
    res=[]
    m=[]
    for i in range(dl2):
        for j in range(dl):
            m.append(a[j][i])
        res.append(m)
        m=[]
    return res

    # Your code here
    pass