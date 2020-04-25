import os
import yaml

current=os.path.dirname(__file__)
filepath=os.path.join(current,'../data/element_info.yaml')
class GetElementInfoYaml:
    def __init__(self):
        fopen=open(filepath,'r',encoding='utf-8')
        self.getyaml=yaml.load(fopen,yaml.FullLoader)
    def getelementinfo(self):
        return self.getyaml

if __name__=="__main__":
    a=GetElementInfoYaml().getelementinfo()
    print(a['login_page']['caotao_button'])