import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



def analysis(data):
    var = np.var(data) * len(data) / (len(data) - 1)
    std = var ** (1 / 2)
    stdzation = [round((v - np.mean(data)) / std, 2) for v in data]

    return (
        "mean : %.2f, var : %.2f, std : %.2f, 표준화:" % (np.mean(data), var, std),
        stdzation,
    )


def cov(data1, data2):
    return np.cov(data1, data2)[0][1], np.corrcoef(data1, data2)[0][1]


def Regression1(X, y): # Least Square Method
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

def Regression2(data1, data2,x): # x, y, 데이터 입력
    data1 = np.array(data1)
    data2 = np.array(data2)
    b0 = (np.mean(data2) - ((np.cov(data1, data2)[0][1]) / (np.var(data1)* len(data1) / (len(data1)-1)) * (np.mean(data1))))
    b1 = (np.cov(data1, data2)[0][1]) / (np.var(data1) * len(data1) / (len(data1)-1))
    return ("Y = %.2fx + %.2f" % (b1, b0)), b0 + b1 * x

def Regression3(data1, data2, data3 ,x, u): # x, u, y, 데이터 입력 1, 데이터 입력 2
    data1 = np.array(data1)
    data2 = np.array(data2)
    A = [[np.var(data1) * len(data1) / (len(data1)-1), (np.cov(data1, data2)[0][1])], [(np.cov(data1, data2)[0][1]), np.var(data2) * len(data2) / (len(data2)-1)]]
    b = [np.cov(data1, data3)[0][1], np.cov(data2, data3)[0][1]]
    b1 = np.linalg.solve(A,b)[0]
    b2 = np.linalg.solve(A,b)[1]
    b0 = np.mean(data3) - b1 * np.mean(data1) - b2 * np.mean(data2)
    return ("Y = %.2f + %.2fx + %.2fu" % (b0, b1, b2)), b0 + b1 * x + b2 * u




print(analysis([60, 45, 155, 130, 80, 210, 200, 185, 135, 55]))
print(analysis([170, 166, 175, 158, 174, 180, 176, 170, 178, 169]))
print("")
print(
    "data1, data2의 공분산,상관계수 \n",
    cov(
        [170, 166, 175, 158, 174, 180, 176, 170, 178, 169],
        [63, 65, 61, 59, 63, 77, 66, 56, 71, 63],
    ),
)
print("")
print("단순회귀 방정식 구하기 : Y = b1x + b0, (b1에 대한 편미분, b0에 대한 편미분, 두 방정식을 연립한 해)")
print(
    Regression1(
        [5.5, 4.5, 4.1, 3.5, 2.5, 2.3, 2.7, 2.8], [73, 59, 56, 31, 28, 31, 30, 25]
    )
)
print("분산, 공분산을 이용한 회귀방정식, 예측값 --> ",Regression2([5.5, 4.5, 4.1, 3.5, 2.5, 2.3, 2.7, 2.8], [73, 59, 56, 31, 28, 31, 30, 25], 5.5))
X = [5.5, 4.5, 4.1, 3.5, 2.5, 2.3, 2.7, 2.8]
y = [73, 59, 56, 31, 28, 31, 30, 25]

print("중회귀방정식, 예측값",Regression3([5.5, 4.5, 4.1, 3.5, 2.5, 2.3, 2.7, 2.8], [12, 9, 8, 6, 5, 6, 5, 4], [73, 59, 56, 31, 28, 31, 30, 25], 5.5, 12))
plt.plot(X, y, "o")
plt.title("Scatter Plot")
plt.show()
