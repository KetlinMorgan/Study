P, X, Y = int(input()), int(input()), int(input())
summa = X * 100 + Y
res = summa + (summa * P) / 100
print(int(res // 100), int(res % 100))