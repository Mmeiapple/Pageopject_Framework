import os
import unittest
from common import HTMLTestReportCN
from common.get_config import getconfig


current=os.path.dirname(__file__)
test_case_path=os.path.join(current,getconfig.get_casepath)
report_path=os.path.join(current,getconfig.get_reportpath)


class  RunAllCases:
    def __init__(self):
        self.test_case_path=test_case_path
        self.report_path =report_path
        self.title='禅道自动化测试报告'
        self.description='hemei—test'
    def run(self):
        discover=unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                     pattern='*_test.py',
                                                     top_level_dir=self.test_case_path)
        all_sutie=unittest.TestSuite()
        all_sutie.addTest(discover)

        report_dir=HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path=HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path=HTMLTestReportCN.GlobalMsg.get_value('report_path')
        with open(report_path,'wb') as file:
            runner=HTMLTestReportCN.HTMLTestRunner(stream=file,
                                                        title=self.title,
                                                        description=self.description,
                                                        tester='hemie')
            runner.run(all_sutie)

        return dir_path


if __name__=="__main__":
    a=RunAllCases().run()