#!/usr/bin/env python
#_*_ coding: utf-8 _*_
#python = 3.6

import xlrd
import xlwt
import glob
import os

filenames = glob.glob(r'\Users\zhanglanxia\Desktop\*.xls')

def read_excel(filename):
    print(filename)
    file_name = os.path.basename(filename)
    print(file_name)
    data = xlrd.open_workbook(filename)  #打开工作表
    sheet = data.sheet_by_index(0)  #根据sheet索引或者名称获取sheet内容
    nrows = sheet.nrows  #获取行数
    ncols = sheet.ncols  #获取列数
    print(nrows)
    print(ncols)
    # id = sheet.col_values(1)   #获取第二列的内容
    # idDict = {}
    # for i in range(1,nrows):
    #     cell_value1 = sheet.cell_value(i, 0)  #获取单元格的内容 第i行第一列
    #     if id[i] not in idDict:
    #         idDict[id[i]] = cell_value1
    #     else:
    #         idDict[id[i]] = idDict[id[i]] + cell_value1
    # final = sorted(idDict.items(), key=lambda item: item[1], reverse=True)
    # return final

# def write(final,finalname):
#     workbook = xlwt.Workbook(encoding='utf-8')
#     data_sheet = workbook.add_sheet('sheet1')
#     row0 = ['comments', 'price']
#     data_sheet.write(0, 0, row0[0])
#     data_sheet.write(0, 1, row0[1])
#     for i in range(1,len(final)+1):
#         data_sheet.write(i, 0, final[i-1][0])
#         data_sheet.write(i, 1, final[i-1][1][0])
#     workbook.save(finalname)


if __name__ == '__main__':
    for filename in filenames:
        read_excel(filename)
        # final = read_excel(filename)
    #     write(final,"/Users/zhanglanxia/Desktop/"+"new"+os.path.basename(filename) )



