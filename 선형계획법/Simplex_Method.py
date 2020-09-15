c = [-3, -2]  # 목적함수의 계수
A = [[1, 2], [2, 1], [-1, 1], [0, 1]]  # subject to.의 좌변
b = [6, 8, 1, 2]  # subject to.의 우변
x0_bounds = (0, None)
x1_bounds = (0, None)

from scipy.optimize import linprog

# Solve the problem by Simplex method in Optimization
res = linprog(
    c,
    A_ub=A,
    b_ub=b,
    bounds=(x0_bounds, x1_bounds),
    method="simplex",
    options={"disp": True},
)
print(res)
