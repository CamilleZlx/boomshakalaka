# -*- coding: utf-8 -*-

import xlrd
import xlwt
import glob
import os

filenames = glob.glob(r'C:\Users\Camille\Desktop\data_output\wmf_output\*.xls')
# path = ('C:/Users/Camille/Desktop/Data_Analysis/ALL_commodity/facelle')
# ls = os.listdir(path)
# count = 0
# for i in ls:
#     if os.path.isfile(os.path.join(path, i)):
#         count += 1
# print count

def row(filename):
    # print filename
    # print os.path.dirname(filename)
    data = xlrd.open_workbook(filename)
    sheet = data.sheet_by_index(0)
    file_row = sheet.nrows-1
    print file_row
    return file_row

def write_to_excel(name):
    excel = xlwt.Workbook(encoding= 'utf-8')
    sheet = excel.add_sheet('sheet1')
    rows = []
    for filename in filenames:
        file_row = row(filename)
        rows.append(file_row)
    for i in range(0,len(rows)):
        sheet.write(i,1,rows[i]) # row col value
    excel.save(name)


if __name__ == '__main__':
    # for filename in filenames:
    #     file_row = row(filename)
    write_to_excel("C:/Users/Camille/Desktop/count/"+"wmf.xls")
    # file_row = row('C:/Users/Camille/Desktop/data_output/facelle_output/facelle0511.xls')
    # write_to_excel(file_row,"C:/Users/Camille/Desktop/"+"facelle.xls")

