sp1, sp2 = [], []
k = 0
for i in range(8):
    x, y = list(map(int, input().split()))
    sp1.append(x)
    sp2.append(y)

for i in range(8):
    for j in range(i + 1, 8):
        if len(set(sp1)) != 8 or len(set(sp2)) != 8 or abs(sp1[i] - sp1[j]) == abs(sp2[i] - sp2[j]):
            k = k + 1
print('YES' if k > 0 else 'NO')


