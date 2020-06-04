# coding = utf-8
from tools.filed import Filed


# 定义元类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)
        mappings = {}
        for k,v in attrs.items():
            if isinstance(v,Filed):
                mappings[k] = v
        for k, v in mappings.items():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name.lower()
        return super().__new__(cls, name, bases, attrs)
