import numpy as np
from fractions import Fraction

def gauss(matrix, result):
    def sort_arrays(matrix, result):
        # сортировка строк по убыванию 1й колонки, потом 2й, потом 3й и т.д.
        order_idx = sorted(enumerate(matrix.tolist()), key=lambda x: x[1], reverse=True)
        order_idx = [i[0] for i in order_idx]
        return matrix[order_idx], result[order_idx]

    def to_diag(matrix, result):
        for i in range(min(matrix.shape)):
            # одна итерация посвящена тому, чтобы выбрать i-ый элемент в i-й строке,
            # привести его к 1 и занулить i-ый элемент в остальных строках
            row_idx, col_idx = i, i
            divider = matrix[row_idx][col_idx]
            if divider not in (0, 1):
                matrix[row_idx] = matrix[row_idx] / divider
                result[row_idx] = result[row_idx] / divider

            for an_row_idx in filter(lambda x: x != row_idx, range(rows_cnt)):
                multiplier = matrix[an_row_idx][col_idx]
                matrix[an_row_idx] = matrix[an_row_idx] - (matrix[row_idx] * multiplier)
                result[an_row_idx] = result[an_row_idx] - (result[row_idx] * multiplier)
            matrix, result = sort_arrays(matrix, result)  # перестановка строк
        return matrix, result
    matrix, result = to_diag(*sort_arrays(matrix, result))
    all_zero_rows = np.all(np.equal(matrix, 0), axis=1)

    if (result[all_zero_rows] != 0).sum() > 0:  # проверка на уравнения вида "0 = b", где "b != 0"
        print('NO')
    elif matrix.shape[1] > matrix[~all_zero_rows].shape[0]:  # ранг матрицы меньше, чем кол-во переменных
        print('INF')
    else:
        print('YES')
        print(' '.join(result[~all_zero_rows].astype(float).astype(str)))