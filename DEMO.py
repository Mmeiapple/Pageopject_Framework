import os
from common.excel_utils import ExcelUtils

curren = os.path.dirname(__file__)
excel_path = os.path.join(curren, '../data/test_data.xlsx')
print(21212)

class TestDataUtils():
    def __init__(self, test_suite_name, test_calss_name):
        self.test_calss_name = test_calss_name
        self.excel_data = ExcelUtils(excel_path, test_suite_name).get_sheet_data_by_list()
        self.testsuitcounts = len(self.excel_data) - 1  # 祛除行首的值

    """

    {‘test_login_sucsess’:{'test_name':'验证是否能成功进行登录',‘isnot’:'是','excepted_result':'测试人员1','test_parameter':{'参数1'：‘参数值1’,'参数2'：‘参数值2’}}}

    """

    def convert_exceldata_to_testdata(self):
        test_data_infos = {}
        for i in range(1, self.testsuitcounts):
            test_data_info = {}
            if self.excel_data[i][2].__eq__(self.test_calss_name):
                test_data_info['test_name'] = self.excel_data[i][1]
                test_data_info['isnot'] = self.excel_data[i][3]
                test_data_info['excepted_result'] = self.excel_data[i][4]
                test_parameter = {}
                for j in range(5, len(self.excel_data[i])):
                    if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j]) > 2:
                        parameter_info = self.excel_data[i][j].split('=')
                        test_parameter[parameter_info[0]] = parameter_info[1]
                    test_data_info['test_parameter'] = test_parameter
                test_data_infos[self.excel_data[i][0]] = test_data_info
        return test_data_infos


if __name__ =='__mian__':
    read_excel_data = TestDataUtils('login_suite', 'LoginTest').convert_exceldata_to_testdata()
    for i in read_excel_data.values():
        print(i)

