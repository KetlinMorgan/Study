from sys import stdin
d = {}
for i in stdin.readlines():
    men, item, num = list(i.split())
    d.setdefault(men, {}).setdefault(item, 0)
    d[men][item] = d[men][item] + int(num)

for x in sorted(d):
    print(x, ':', sep='')
    for y in sorted(d[x]):
        print(y, d[x][y])