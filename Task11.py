'''
Задача «Продажи»

Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида Покупатель товар количество,
где Покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов),
количество — количество приобретенных единиц товара.
Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.
Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.
'''

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
