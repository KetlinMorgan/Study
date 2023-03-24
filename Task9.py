n, m = map(int, input().split())
mp = [[0]*m for _ in range(n)]
for i in range(n):
    mp[i] = input().split()
a, b = map(int, input().split())

for i in range(n):
    for j in range(m):
        if j == a:
            print(mp[i][b], end=' ')
        elif j == b:
            print(mp[i][a], end=' ')
        else:
            print(mp[i][j], end=' ')
    print()
