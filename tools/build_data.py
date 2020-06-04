# coding:utf-8

import random
from datetime import date
from datetime import timedelta

class BuildData:
    def creat_phone(self):
        third_num = ['130', '131', '132', '133', '134', '135','150', '152','153', '154', '155', '181','188']
        num1 = random.choice(third_num)
        num2 = []
        num3 = '0123456789'
        num4 = ''
        for num in range(0, 8):
            num2.append(random.choice(num3))
            num4 = ''.join(num2)
        phone_number = num1+num4
        return phone_number

    def get_district_code(self):  # 获取区号
        codelist = list()
        path = r'../config/districtcode.txt'
        with open(path) as f:
            dict = f.readlines()
        for line in dict:
            if line.lstrip().rstrip().strip() != '' and (line.lstrip().rstrip().strip())[0:6][-2:]!='00':
                codelist.append(line[0:6])
        code = random.choice(codelist)
        return code

    def get_birth(self):  # 获取出生日期
        year = str(random.randint(1950, 1998))
        month = date.today()+timedelta(days=random.randint(1, 366))
        month = month.strftime('%m%d')
        birth = year + month
        return birth

    def get_card_id(self):  # 生成3位随机数和权重位生成身份证号
        id = self.get_district_code()+self.get_birth()
        id = id + str(random.randint(100, 299))
        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        print(id)
        return id

    def get_name(self):
        first_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈']
        middle_name = ['玉', '明', '龙', '芳', '军', '玲']
        last_name = ['', '立', '玲', '', '国', '']
        name = random.choice(first_name) + random.choice(middle_name) + random.choice(last_name)
        return name











if __name__ == '__main__':
    number = BuildData()
    number.get_card_id()

