from log import filter
import json


def register():
    user_name = input('请输入用户名')
    user_name = filter.fil(user_name)
    password = input('请输入密码')
    repeat_password = input('请重新输入密码')
    if password == repeat_password:
        # 用r模式打开，反序列化文件句柄f1
        with open('database.json', 'r') as f1:
            lists = json.load(f1)
        # 反序列化后的是列表里面包含字典 新增列表
        lists.append({'username': user_name, 'password': password})
        # 用w模式打开，把新增好的列表重新写入覆盖进去
        with open('database.json', 'w') as f2:
            json.dump(lists, f2)
    else:
        print('俩次密码不正确，注册失败')


register()
