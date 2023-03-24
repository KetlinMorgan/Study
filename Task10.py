n, k = map(int, input().split())
r, mn = 0, set()
for i in range(k):
    a_i, b_i = map(int, input().split())
    while a_i <= n:
        if a_i % 7 != 0 and (a_i % 7) % 6 !=0 :
            mn.add(a_i)
        a_i = a_i + b_i

print(len(mn))