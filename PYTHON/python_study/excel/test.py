#coding=utf-8

# import os
# def file_name(file_dir):
#     list = []
#     temp = []
#     for root , dirs , files in os.walk(file_dir):
#         for file in files:
#             if os.path.splitext(file)[1] == '.xls':
#                 temp.append(os.path.basename(file))
#     for i in range(len(temp)):
#         print temp[i].replace(".xls","")
#     print temp
# file_name("C:\\Users\\Camille\\Desktop\\facelle")


# import os
# filename = ('C:/Users/Camille/Desktop/Data_Analysis/ALL_commodity/facelle/facelle0621.xls')
# path = os.path.dirname(filename)
# print path
# # path = ('C:/Users/Camille/Desktop/Data_Analysis/ALL_commodity/facelle')
# ls = os.listdir(path)
# count = 0
# for i in ls:
#     if os.path.isfile(os.path.join(path,i)):
#         count += 1
# print count

