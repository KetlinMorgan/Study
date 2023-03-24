from math import sqrt
x_n = int(input())
n, summa, Q, num_sp = 0, 0, 0, []
while x_n != 0:
    summa = summa + x_n
    num_sp.append(x_n)
    x_n = int(input())
    n = n + 1
s = summa / n

for i in range(n):
    Q = Q + (num_sp[i] - s) ** 2

print(sqrt(Q / (n - 1)))