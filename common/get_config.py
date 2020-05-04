import os
from configparser import ConfigParser


current=os.path.dirname(__file__)
filepath=os.path.join(current,'../config/conf.ini')
print(filepath)

class GetConfig():
    def __init__(self):
        self.__conf=ConfigParser()
        self.__conf.read(filepath,encoding='utf-8')

    #自定义传值获取配置信息
    def getindependent(self,configuration,name):
        return self.__conf.get(configuration,name)

    @property  #将方法变为属性
    def geturl(self):
        return self.__conf.get('defaule','url')

getconfig=GetConfig()


if __name__=="__main__":
    print(getconfig.getindependent('defaule','url'))
