#coding = utf-8

import xlwt
import glob
import os

def row_name(filename):
    # print filename
    # print os.path.dirname(filename)
    row_name  = os.path.basename(filename).replace(".xls","")
    # print row_name
    return row_name

def write_to_excel(name):
    excel = xlwt.Workbook(encoding= 'utf-8')
    sheet = excel.add_sheet('sheet1')
    rowname = []
    for i in range(0,len(rowname)):
        print (rowname[i])
    for filename in filenames:
        time = row_name(filename)
        rowname.append(time)
    for i in range(0,len(rowname)):
        sheet.write(i,0,rowname[i])
    excel.save(name)

def rename(path):
    filelist = os.listdir(path)
    for files in filelist:
        olddir = os.path.join(path,files)
        filename = os.path.splitext(files)[0]
        # print (filename)
        # print(filename.replace("爱他美","2017"))
        filetype = os.path.splitext(files)[1]
        newdir = os.path.join(path ,filename.replace("榨汁机","2017")+filetype)
        os.rename(olddir,newdir)

if __name__ == '__main__':
    # row_name('C:/Users/Camille/Desktop/data_output/facelle_output/facelle0511.xls')
    rename(r'C:\Users\Camille\Desktop\data_output\wmf_output')
    filenames = glob.glob(r'C:\Users\Camille\Desktop\data_output\wmf_output\*.xls')
    write_to_excel("C:/Users/Camille/Desktop/"+"wmf_.xls")


