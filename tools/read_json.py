'''
这个文件主要是对JSON文件进行读取。
'''
import json
import os.path

# 读取json文件的函数
def read_json(filename):
    '''
    :param filename: JSON文件的位置
    :return: 测试用例组成的字典
    '''
    filepath = os.path.join("../data/",filename)
    with open(filepath,"r",encoding="utf-8") as f:
        return json.load(f)

if __name__ == '__main__':


    datas = read_json("login.json")
    # print(datas)
    arrs = []
    for data in datas.values():
       arrs.append((data['a'],data['b'],data['expect']))
    print(arrs)

