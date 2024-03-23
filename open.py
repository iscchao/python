# 读取文件
file = open("text.html", mode="r") # 获得一个文件句柄 读取模式
print(file.read())  # 获取当前文件的所有数据
print(file.read(5))  # 表示从文件中获取5个字节的数据
print(file.readline())  # 从光标处开始获取当行数据，获取完后光标会移动到下一行开始
print(file.readline(3))  # 表示从光标出开始获取当行3个字节的数据,如参数大于当前行数据字节数 只会读取当行整行
print(file.readlines())  # 从光标处读取所有行的数据，以字符串的形式存入列表里，返回一个列表
# # 每行末尾的换行符 (\n) 将会被保留

# 循环高效获取数据
for line in file:  # 基于垃圾回收机制，重复对变量line赋值 节省内存
    print(line, end='')

# 写文件
file = open("text02.json", mode="w", encoding='utf-8')  # a模式为追加
# 在当前目录下找到text02.json文件并覆盖内容并写入，没有则创建
import json

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
alist_json = json.dumps(alist)  # 使用dumps将python数据类型序列化成json格式
# file.write(alist_json)  # 文件是json格式 写入的数据也必须是json格式 虽然字符串也可以写入但不建议
file.close()  # 默认程序结束关闭，如整体程序执行时间长 要写close
