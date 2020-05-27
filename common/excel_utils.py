import os
import xlrd
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
