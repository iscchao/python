# 函数四个参数 位置参数 默认参数 动态参数 *args可变参数 **kwargs关键字参数
def fuc1():  # 返回多个值会打包成为元组
    return 1, 2


print(fuc1())


def fuc2(*args):  # *args 也可以任意的标识符代表形参 例如*a 建议使用*args
    return args


alist = [1, 2, 3, 4, 5]
sum1 = fuc2(*alist)
print(sum1)


def fuc3(**kwargs):  # **kwargs 必须是键值对形式的形参
    print(kwargs)


fuc3(age=10, name='chao')
dic = {'name': 'chao', 'height': 180}
fuc3(**dic)

total = 0  # 全局变量


def fuc4(a, b):
    total = a + b  # 局部变量
    print(total)  # 现在局部作用中找变量，如没有再向上一级寻找


def fuc5(a, b):
    global total  # 引用外部的全局变量total
    total = a + b
    print(total)


fuc4(10, 20)  # 30
print(total)  # 0
fuc5(20, 30)  # 50

# 匿名函数 lambda 参数:返回值
# 通常匿名函数 是作为有名函数的参数或者返回值使用
someone = lambda n: 1 if n > 0 else 0
print(someone(10))

scores = [50, 60, 70, 20, 100, 80]


def isPass(num):
    if num >= 60:
        return '合格'
    else:
        return '不及格'


retPass = map(isPass, scores)  # 列表的map方法可以对所有元素进行isPass的操作
print(list(retPass))  # 返回值为map对象 通过list方法转换成列表
# lambda 只能进行2选一的判断 如想要多个条件只能二分判断下去
retPass2 = map(lambda num: '优秀' if num >= 80 else ('及格' if num >= 60 else '不及格'), scores)
print(list(retPass2))
