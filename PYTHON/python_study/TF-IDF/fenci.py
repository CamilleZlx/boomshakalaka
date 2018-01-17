# -*- coding: utf-8 -*-
# python 3.6

import jieba
jieba.load_userdict("E:/Python.workspace/TF-IDF/userdict.txt")

f1 = open("C:/Users/Camille/Desktop/List/fenci.txt")
f2 = open("C:/Users/Camille/Desktop/List/fenci_result.txt", 'a')
lines = f1.readlines()  # 读取全部内容
for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ', '')
    seg_list = jieba.cut(line, cut_all=False)
    f2.write(" ".join(seg_list))

f1.close()
f2.close()