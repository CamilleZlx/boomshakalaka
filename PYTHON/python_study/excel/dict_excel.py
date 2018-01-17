# -*- coding: UTF-8 -*-

import time
import xlrd
import xlwt

start = time.clock()
def read_excel(file):
    # """
    # 读入excel文件
    # :rtype : object
    # :param file:
    # :return: 数据对象
    # """
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as err:
        print(err)

def write_excel(file):
    # """
    # 读入excel文件
    # :rtype : object
    # :param file:
    # :return: 数据对象
    # """
    try:
        data = XlsxWrite.Workbook(file)
        return data
    except Exception as err:
        print(err)


def excel_to_dict(read_excel_file,excel_title):
    # """
    # :rtype : object
    # :return dict
    # """
    dict2 = {}
    data = read_excel(read_excel_file)
    table = data.sheet_by_name(u'bas_info')
    for i in range(1,table.nrows):
        row_content = table.row_values(i, 0, table.ncols)
        dict1 = dict(zip(excel_title, row_content))
        dict2[i] = dict1
    return dict2


def dict_to_excel(dict_content,excel_title):
    # """
    # 将字典写入excel中
    # :type dict_content: object dict
    # excel_title 列标题
    # """
    dict_ing = dict_content
    excel_init_file = xlsxwriter.Workbook(out_excel_file)
    table = excel_init_file.add_worksheet('bas_info')
    title_bold = excel_init_file.add_format({'bold': True, 'border': 2, 'bg_color':'blue'})
    border = excel_init_file.add_format({ 'border': 1})
    for i,j in enumerate(excel_title):
        table.set_column(i,i,len(j)+1)
        table.write_string(0,i,j,title_bold)
    for k,v in dict_content.items():
        for i in range(len(v)):
            j = v.get(excel_title[i])
            table.write_string(k,i,j,border)
    table.set_column(1,1,16)
    table.set_column(0,0,16)
　　excel_init_file.close()

if __name__ == '__main__':
　　read_excel_file = r'D:\baspools_read.xlsx'
　　out_excel_file = r'D:\baspools_out.xlsx'
　　excel_title = ['basname', 'basip', 'location', 'baslocation', 'port', 'basprovider', 'portal_version', 'timeout', 'retry','auth_type']
　　dict_content = excel_to_dict(read_excel_file,excel_title)  #excel to dict
　　dict_to_excel(dict_content,excel_title)                    #dict to excel  write to out_excel_file
　　end = time.clock()
　　print("read: %f s" % (end - start))