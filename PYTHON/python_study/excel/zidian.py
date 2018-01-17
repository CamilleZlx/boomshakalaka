# -*- coding : utf-8 -*-
# python 2.7

import xlrd
import xlwt
import glob
import os

filenames = glob.glob(r'C:\Users\Camille\Desktop\test\*.xls')

def sort(filename):
    print filename
    file_name = os.path.basename(filename)
    print file_name
    data = xlrd.open_workbook(filename)
    sheet = data.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    id = sheet.col_values(0)
    idDict = {}
    for i in range(1,nrows):
        cell_value1 = sheet.cell_value(i, 1)
        cell_value2 = sheet.cell_value(i, 2)
        cell_value3 = sheet.cell_value(i, 3)
        if id[i] not in idDict and cell_value2 != "-" and cell_value3 != "-":
            idDict[id[i]] = (cell_value1,cell_value2,cell_value3)
        elif cell_value2 != "-" and cell_value3 != "-":
            idDict[id[i]] = (cell_value1,cell_value2,cell_value3)
    final = sorted(idDict.items(),key = lambda item:item[1],reverse = True)
    return final

def write(final,finalname):
    workbook = xlwt.Workbook(encoding='utf-8')
    data_sheet = workbook.add_sheet('sheet1')
    row0 = ['item_id', 'item_name', 'trade', 'comments']
    data_sheet.write(0, 0, row0[0])
    data_sheet.write(0, 1, row0[1])
    data_sheet.write(0, 2, row0[2])
    data_sheet.write(0, 3, row0[3])
    for i in range(1,len(final)+1):
        data_sheet.write(i, 0, final[i-1][0])
        data_sheet.write(i, 1, final[i-1][1][0])
        data_sheet.write(i, 2, final[i-1][1][1])
        data_sheet.write(i, 3, final[i-1][1][2])
    workbook.save(finalname)

# def file_name(file_dir):
#     list = []
#     for root , dirs , files in os.walk(file_dir):
#         for file in files:
#             if os.path.splitext(file)[1] == '.xls':
#                 list.append(os.path.basename(file))
#     for i in range(len(list)):
#         print list[i].replace(".xls","")
#
#     return list

if __name__ == '__main__':
    for filename in filenames:
        final = sort(filename)
        write(final,"C:/Users/Camille/Desktop/test/"+"new"+os.path.basename(filename) )
