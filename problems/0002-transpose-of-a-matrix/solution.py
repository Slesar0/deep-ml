def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    """
    Возвращает транспонированную матрицу.
    Для матрицы m x n результатом будет матрица n x m.
    """
    # Если матрица пустая — возвращаем пустой список
    if not a:
        return []

    rows = len(a)        # число строк исходной матрицы (m)
    cols = len(a[0])     # число столбцов исходной матрицы (n)

    # Создаём новую матрицу размера n x m, заполненную нулями
    result = [[0] * rows for _ in range(cols)]

    # Заполняем: элемент result[j][i] = a[i][j]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = a[i][j]

    return result