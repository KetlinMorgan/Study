r, k = 1, 1
n, m = int(input()), int(input())
while m != 0:
    if m == n:
        r = r + 1
        k = max(k, r)
    else:
        r = 1
    n = m
    m = int(input())
print(k)