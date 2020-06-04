# coding = utf-8
from tools.database_connect import create_pool
from tools.filed import Filed
from tools.model_metaclass import ModelMetaclass


# 定义数据库的操作方法
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)
    # def __getattr__(self, key):
    #     return self[key]
    # def __setattr__(self, key, value):
    #     self[key] = value

    def select(self, column_list, where_list):
        args = []
        fileds = []
        for k, v in self.__mappings__.items():
            fileds.append(k)
        for k in where_list:
            args.append(k)
        for k in column_list:
            if k not in fileds:
                raise RuntimeError("field not found")
        sql = 'select %s from %s where %s' % (','.join(column_list),self.__table__,'and '.join(args))
        print(sql)
        res = self.__do_excute(sql)
        return res
    def __do_excute(self,sql):
        db = create_pool()
        cursor = db.cursor()
        if 'select'in sql:
            cursor.execute(sql)
            rs = cursor.fetchall()
        else:
            rs = cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return rs

    def insert_many(self, column_list, value_list):
        args=[]
        files=[]
        for k,v in self.__mappings__.items():
            files.append(k)
        for k in value_list:
            args.append(k)
        for k in column_list:
            if k not in files:
                raise RuntimeError("field not found")
        sql1 ="INSERT INTO %s(%s)" %(self.__table__,','.join(column_list))
        num = len(value_list[0])
        forma = []
        for i in range(num):
            forma.append('%s')
        format_data = ','.join(forma)
        sql2 = "VALUES" + '(' + format_data + ')'
        # sql2 = "VALUES (%s,%s,%s,%s)"
        sql = sql1 + sql2
        data = value_list
        print(sql)
        res = self.__do_excutemany(sql,data)
        return res
    def __do_excutemany(self,sql,data):
        db = create_pool()
        cursor = db.cursor()
        rs = cursor.executemany(sql, data)
        db.commit()
        cursor.close()
        db.close()
        return rs

    # def insert(self,column_list, value_list):
    def update(self,column_list,where_list):
        args = []
        fileds = []
        for k in where_list:
            args.append(k)
        sql = "UPDATE %s SET %s WHERE %s" %(self.__table__,','.join(column_list),'and '.join(args))
        print(sql)
        res = self.__do_excute(sql)
        return res
    def delete(self,where_list):
        args = []
        for k in where_list:
            args.append(k)
        sql = 'DELETE FROM %s WHERE %s' %(self.__table__, 'and '.join(args))
        print(sql)
        res = self.__do_excute(sql)
        return res













