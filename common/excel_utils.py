import os
import xlrd
<<<<<<< HEAD
import json


class ExcelUtils(object):
    def __init__(self,excel_path,sheet_name=None):
        self.excel_path=excel_path
        self.sheet_name=sheet_name
        self.sheet_date=self.get_sheet_date()

    """
    sheet表值传递    
        
    """
    def get_sheet_date(self):
        workopen=xlrd.open_workbook(self.excel_path)
        if self.sheet_name:
            sheet=workopen.sheet_by_name(self.sheet_name)
        else:
            sheet=workopen.sheet_by_index(0)
        return sheet

    """
    sheet表最大行    

    """
    @property
    def get_nrows(self):
        return self.sheet_date.nrows

    """
    sheet表最大列    

    """
    @property
    def get_ncols(self):
        return self.sheet_date.ncols


    """
    
    将Excel表以列表形式返回   

    """
    def get_sheet_data_by_list(self):
        all_data=[]
        for rows in range(self.get_nrows):
            row_data=[]
            for ncols in range(self.get_ncols):
                value=self.sheet_date.cell_value(rows,ncols)
                row_data.append(value)
            all_data.append(row_data)
        return all_data

if __name__=="__main__":
    curren=os.path.dirname(__file__)
    excel_path=os.path.join(curren,'../data/test_data.xlsx')
    sheet_info=ExcelUtils(excel_path,'login_suite').get_sheet_data_by_list()
    print(json.dumps(sheet_info,indent=1,ensure_ascii=False))
=======


class ExcelUtils(object):
    """
    判断是否是excel文件再进行处理 xls  xlsx  并且 文件存在
    """

    def __init__(self,excel_path,sheet_name=None):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):
        workbook = xlrd.open_workbook(self.excel_path)
        if self.sheet_name:     # 当sheet_name没带参数时，默认取第一个表格
            sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            sheet = workbook.sheet_by_index(0)
        return sheet

    @property
    def get_row_count(self):
        row_count = self.sheet_data.nrows
        return row_count

    @property
    def get_col_count(self):
        col_count = self.sheet_data.ncols
        return col_count

    def get_sheet_data_by_list(self): #把excel的数据通过列表返回 [ [] , [] , [] ]
        all_excel_data = []
        for rownum in range(self.get_row_count):
            row_excel_data = []
            for colnum in range(self.get_col_count):
                cell_value = self.sheet_data.cell_value(rownum,colnum)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data

if __name__ == '__main__':
    current_path = os.path.abspath(os.path.dirname(__file__))
    test_data_path = os.path.join(current_path,'../data/element_info.xlsx')
    sheet_infos = ExcelUtils(test_data_path,'login').get_sheet_data_by_list()
    print( sheet_infos )
>>>>>>> origin/master
