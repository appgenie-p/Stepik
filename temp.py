class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix):
        if not all(
            (
                len(i) == len(matrix[0]) and type(j) in (int, float)
                for i in matrix
                for j in i
            )
        ):
            raise ValueError("Неверный формат для первого параметра matrix.")

        sr, sc = self.size  # size_row, size_column
        str, stc = self.step  # step_row, step_column
        new_mtrx_row = (len(matrix) - sr) // str + 1
        new_mtrx_col = (len(matrix[0]) - sc) // stc + 1

        new_matrix = [[0] * new_mtrx_col for _ in range(new_mtrx_row)]

        for x in range(new_mtrx_row):
            for y in range(new_mtrx_col):
                res = (
                    i[y * str : y * sr + sr]
                    for i in matrix[x * stc : x * sc + sc]
                )
                new_matrix[x][y] = max(max(i) for i in res)

        return new_matrix



mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [
    [12]
], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert (
        False
    ), "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert (
        False
    ), "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"