def solution1(arr1, arr2):
    return [
        [arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))
    ]


import numpy as np


def addition(arr1, arr2):
    return (np.array(arr1) + np.array(arr2)).tolist()


def solve(arr1, arr2):  # Ax=b면 solve(A,b) --> x를 구함.
    return np.linalg.solve(np.array(arr1), np.array(arr2))


def inverse(arr1):
    return np.linalg.inv(np.array(arr1))


def dot(arr1, arr2):
    return np.dot(np.array(arr1), np.array(arr2))


def det(arr):
    return np.linalg.det(np.array(arr))


def cross(arr1, arr2):
    return np.cross(np.array(arr1), np.array(arr2))


print("행렬의 덧셈\n", addition([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print("Ax=b에서 x\n", solve([[1, 2, 3], [2, 5, 3], [1, 0, 8]], [5, 3, 17]))
print("역행렬\n", inverse([[1, 2, 3], [2, 5, 3], [1, 0, 8]]))
print(
    "행렬의 곱 또는 내적\n",
    dot([[1, 2, 4], [2, 6, 0]], [[4, 1, 4, 3], [0, -1, 3, 1], [2, 7, 5, 2]]),
)
print("Determinant\n", round(det([[2, 1, -1], [0, 4, -3], [1, -2, 1]])))
print("Cross Product\n", cross([0, 2, 3], [-2, 2, -1]))
