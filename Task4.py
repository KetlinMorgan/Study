n = int(input())
k, s = 0, 0
for i in range(n - 1):
    m = int(input())
    k = k + m
for j in range(1, n+1):
    s = s + j

print(s - k)