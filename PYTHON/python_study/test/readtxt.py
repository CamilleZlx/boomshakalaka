# -*- coding:utf-8 -*-
# python3.6


import glob

txt_filenames = glob.glob('C:\\Users\\Camille\\Desktop\\Python3\\*.txt')
urlData = []
for filename in txt_filenames:
      txt_file = open(filename, 'r',encoding = 'utf-8')
      print(txt_file)
      lines = txt_file.readlines()
      for line in lines :
          print(line)
          temp = line.replace('\n','')
          print('temp:'+ temp)
          urlData.append(temp.replace('\ufeff',''))
          print(urlData)
print(urlData)
