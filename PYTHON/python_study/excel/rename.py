#coding=utf-8

import os

def rename(path):
    filelist = os.listdir(path)

    for files in filelist:
        olddir = os.path.join(path,files)
        filename = os.path.splitext(files)[0]
        print (filename)
        print(filename.replace("爱他美","2017"))
        filetype = os.path.splitext(files)[1]
        newdir = os.path.join(path ,filename.replace("爱他美","2017")+filetype)
        os.rename(olddir,newdir)

rename('C:/Users/Camille/Desktop/aptamil_output');

