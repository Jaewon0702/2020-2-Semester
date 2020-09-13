import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def analysis(data):
    var = np.var(data) * len(data) / (len(data) - 1)
    std = var ** (1 / 2)
    stdzation = [round((v - np.mean(data)) / std, 2) for v in data]

    return (
        "mean : %.2f, var : %.2f, std : %.2f" % (np.mean(data), var, std),
        stdzation,
    )


def cov(data1, data2):
    return np.cov(data1, data2)[0][0], np.corrcoef(data1, data2)[0][1]


print(analysis([60, 45, 155, 130, 80, 210, 200, 185, 135, 55]))
print(analysis([170, 166, 175, 158, 174, 180, 176, 170, 178, 169]))
print("")
print(
    "data1의 분산, 공분산 \n",
    cov(
        [170, 166, 175, 158, 174, 180, 176, 170, 178, 169],
        [63, 65, 61, 59, 63, 77, 66, 56, 71, 63],
    ),
)
print("")
X = [5.5, 4.5, 4.1, 3.5, 2.5, 2.3, 2.7, 2.8]
y = [73, 59, 56, 31, 28, 31, 30, 25]


def Regression(X, y):
    p = 0
    c = 1
    k = 0
    for v in X:
        p += pow(v, 2)
    for v in list(map(list, zip(X, y))):
        c = 1
        for i in v:
            c *= i
        k += c
    zero = ((k / p * sum(X)) - sum(y)) / ((sum(X) / p * sum(X)) - len(X))
    one = (k - (sum(X) * zero)) / p
    return (
        "%.1fb1 + %.1fb0 = %.1f " % (p, sum(X), k),
        "%.1fb1 + %db0 = %.1f" % (sum(X), len(X), sum(y)),
        "b1 = %.2f, b0 = %.2f" % (one, zero),
    )


print("회귀 방정식 구하기 : Y = b1x + b0")
print(
    Regression(
        [5.5, 4.5, 4.1, 3.5, 2.5, 2.3, 2.7, 2.8], [73, 59, 56, 31, 28, 31, 30, 25]
    )
)

plt.plot(X, y, "o")
plt.show()
