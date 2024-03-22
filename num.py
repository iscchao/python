import random

# random.random(a, b) 生成为a~b的浮点数(左闭右开) 默认为0~1   randint(a, b) 生成a~b区间的整数
# random.randrange(a, b, step) 生成a~b区间的整数 step为步长

# 猜0~10随机的整数数字，直到猜对为止，输出输入的次数
num = random.randint(0, 11)
userNum = None
userScore = 100
cont = 0
while userNum != num:
    userNum = int(input('请输入数字'))
    cont += 1
    if userNum == num:
        print("输入正确输入次数为", end='\r\r')
        print(f"输入次数为:{cont}")
        break
    print("输入错误，请重新输入")
