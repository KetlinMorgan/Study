N, M, x, y = int(input()), int(input()), int(input()), int(input())
N, M = max(N, M), min(N, M)
if (N - y) >= y and (M - x) >= x:
    print(min(y, x))
elif (N - y) < y and (M - x) >= x:
    print(min(N - y, x))
elif (N - y) >= y and (M - x) < x:
    print(min(y, M - x))
else:
    print(min(N - y, M - x))
