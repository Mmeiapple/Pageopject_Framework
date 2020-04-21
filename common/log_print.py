import os
import logging

current=os.path.dirname(__file__)
loginfopath=os.path.join(current,'../log/info_logs.txt')

class LogPrint:
    def __init__(self):
        # 创建一个日志对象,定义一个名称和日志全局级别
        self.looger=logging.getLogger(__name__)
        #给日志设置级别
        self.looger.setLevel(level=logging.INFO)
        #给日志设置样式
        self.formater=logging.Formatter('Info:%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #创建一个存入文件日志的对象
        console=logging.FileHandler(loginfopath)
        #设置格式
        console.setFormatter(self.formater)
        # 将日志对象文件中输出
        self.looger.addHandler(console)
    def logsinfo(self,message):

        self.looger.info(message)
Log=LogPrint()
if __name__=="__main__":
    Log.logsinfo('dudu')
