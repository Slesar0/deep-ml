def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    m=matrix
    a=m[0][0]
    b=m[0][1]
    c=m[1][0]
    d=m[1][1]
    det=a*d-b*c
    if det==0:
        return None
    det1=1/det
    return [[det1*d,det1*-b],[det1*-c,det1*a]]
    pass