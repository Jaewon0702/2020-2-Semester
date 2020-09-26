from scipy.optimize import linprog
obj = [-4, -1] # 목적함수의 계수

lhs_ineq = [[4, 3], [1, 2]]  # subject >=, <= 좌변의 계수

rhs_ineq = [6, 4]  # subject >=, <= 우변의 계수

lhs_eq = [[3, 1]]  # subject = 좌변의 계수
rhs_eq = [3] #subject = 우변의 계수

bnd = [(0, float("inf")),  # Bounds of x
(0, float("inf"))]  # Bounds of y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
method="revised simplex")

print(opt)
'''opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
method="revised simplex")''' # 없으면 뺀다.
# https://realpython.com/linear-programming-python/
