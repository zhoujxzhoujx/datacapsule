# coding = utf-8

import configparser


class OperIni:
    def __init__(self, file_name):
        self.file_name = file_name
        self.conf = configparser.ConfigParser()

    def get_section(self, section, key):
        self.conf.read(self.file_name, encoding="utf-8-sig")
        return self.conf.get(section, key)


# opr = OperIni(r'E:\PycharmProjects\airspace\config\locate.ini')
# # print(opr.get_section('login','login_button'))