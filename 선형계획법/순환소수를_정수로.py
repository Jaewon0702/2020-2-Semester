def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


x = float(input("순환소수 입력: "))
y = int(input("순환마디 입력: "))

i = int(10 ** len(str(x).split(".")[1]) * x) - int(
    10 ** (len(str(x).split(".")[1]) - len(str(y))) * x
)
j = 10 ** len(str(x).split(".")[1]) - 10 ** (len(str(x).split(".")[1]) - len(str(y)))

print("출력: {}/{}".format(int(i / gcd(i, j)), int(j / gcd(i, j))))
