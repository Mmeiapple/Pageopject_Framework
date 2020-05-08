import os
from configparser import ConfigParser


current=os.path.dirname(__file__)
filepath=os.path.join(current,'../config/conf.ini')

class GetConfig():
    def __init__(self):
        self.__conf=ConfigParser()
        self.__conf.read(filepath,encoding='utf-8')

    #自定义传值获取配置信息
    def getindependent(self,configuration,name):
        return self.__conf.get(configuration,name)
    """
    
    默认测试地址
    
    """
    @property  #将方法变为属性
    def geturl(self):
        return self.__conf.get('defaule','url')
    """

    默认等待时间

    """
    @property
    def gettimeout(self):
        return float(self.__conf.get('defaule','time_out'))

    """

    默认截图地址

    """

    @property  #将方法变为属性
    def getscreenpath(self):
        return self.__conf.get('defaule','screenshot_path')



    """

    默认用户名称

    """

    @property  #将方法变为属性
    def getusername(self):
        return self.__conf.get('defaule','username')




    """

    默认用户密码

    """

    @property  #将方法变为属性
    def getpassword(self):
        return self.__conf.get('defaule','password')




getconfig=GetConfig()


if __name__=="__main__":
    print(type(getconfig.gettimeout))
    print(type(getconfig.getusername))
    print(type(getconfig.getpassword))
