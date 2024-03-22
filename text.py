# 2024-3-22 python基础练习
# 计算100以内所有偶数的和，直到大于1000 输出和与循环次数 结束循环
num = 0
cont = 0
for i in range(2, 101, 2):  # range(start, stop, step) start默认为0 左闭右开 step为步长
    cont += 1  # python 没有自增自减 ++ --
    if num <= 1000:
        num += i
    if num > 1000:
        print(num)
        print(cont)
        break

# 已知 a^2+b^2=c^2 且a+b+c=1000(a,b,c都是自然数)，求a,b,c所以组合
lists = []
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if c >= 0 and a ** 2 + b ** 2 == c ** 2:  # c有可能为负数 加上C>=0的条件判断
            lists.append({'a': a, 'b': b, 'c': c})
print(lists)
