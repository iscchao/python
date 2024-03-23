import json


def fil(use_name):
    fp = open('./log/database.json', mode='r')
    # 根据调用此模块方法的地方来写open的路径
    json_data = json.load(fp)
    fp.close()
    if any(use_name in item for item in json_data):
        # 存储的为列表，列表里面是字典，用in判断是否有对应的键
        repeat = input('用户名存在请重新输入')
        return fil(repeat)
    else:
        return use_name
