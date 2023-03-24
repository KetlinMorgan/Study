n, k = map(int, input().split())
s = 'I' * n
for i in range(k):
    l, r = map(int, input().split())
    s = s[0:l-1] + '.' * (r - l + 1) + s[r:]

print(s)