# coding = utf-8

import json
import os


class OperJson:
    def __init__(self, file_path=None):
        if not file_path:
            _path = os.path.dirname(os.path.dirname(__file__)) + '/config/cookie.json'
            self.file_path =_path
        else:
            self.file_path = file_path

    # 读取json内容
    def read_json(self):
        if os.path.getsize(self.file_path):
            with open(self.file_path,'r',encoding='utf-8') as f:
                res = json.load(f)
        else:
            res = None
        return res
    # 写入json到文件
    def wirte_json(self,value):
        with open(self.file_path,'w',encoding='utf-8') as f:
            json.dump(value, f)

if __name__ == '__main__':
    op = OperJson()
    print(op.read_json())

