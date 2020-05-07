import os
import xlrd
import json


# {variable_name:{element_name,locator_type,locator_value,timeout},}

current=os.path.dirname(__file__)
datapath=os.path.join(current,'../data/element_info.xlsx')

class GetElementInfo:
    def __init__(self,sheetname,filepath=datapath):
        self.work=xlrd.open_workbook(filepath)
        self.sheet=self.work.sheet_by_name(sheetname)


    def getelementinfo(self,pagename):
        pagedict={}
        for i in range(1,self.sheet.nrows):
            if self.sheet.cell_value(i,0)==pagename:
                seconddict={}
                for j in range(2,self.sheet.ncols):
                    title=self.sheet.cell_value(0,j)
                    value=self.sheet.cell_value(i,j)
                    seconddict.update({title:value})
                    headtitle = self.sheet.cell_value(i, 1)
                    pagedict.update({headtitle: seconddict})
        return pagedict
if __name__=='__main__':
    dictread=GetElementInfo('main').getelementinfo('main_page')
    # print(dictread['caotao_button'])
    print(json.dumps(dictread,indent=1,ensure_ascii=False))



