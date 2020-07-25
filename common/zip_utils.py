import os
import zipfile



def zip_dir(dir_path,zip_path):
    '''


    :param dir_path:目标文件夹路径
    :param zip_path: 压缩后的文件夹路径
    :return:
    '''


    zip=zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED)
    for root,dirnames,filenames in os.walk(dir_path):
        file_path=root.replace(dir_path,'')  #去掉根路径，只对目标路径下的文件及文件夹进行压缩
        # 循环出一个个文件名
        for filename in filenames:
            zip.write(os.path.join(root,filename),os.path.join(file_path,filename))
    zip.close()
if __name__=="__main__":
    current_path=os.path.dirname(__file__)
    dri_path=os.path.join(current_path,'reports/禅道自动化测试报告V2.3')
    zip_dir(dri_path,dri_path+'/../禅道自动化测试报告.zip')

