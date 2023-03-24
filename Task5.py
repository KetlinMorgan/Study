s, q = input(), ''
for i in range(len(s)):
    if i % 3 != 0:
        q = q + s[i]
print(q)