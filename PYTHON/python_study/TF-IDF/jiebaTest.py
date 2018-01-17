#! -*- coding:utf-8 -*-
# python 3.6

import jieba

seg_list = jieba.cut("德国贺本清herbacin 洋甘菊护手霜", cut_all = True)
print ("Full Mode:", '/'.join(seg_list)) #全模式
seg_list = jieba.cut("德国贺本清herbacin 洋甘菊护手霜")
print ("Default Mode:", '/'.join(seg_list)) # 精确模式
seg_list = jieba.cut("德国贺本清herbacin 洋甘菊护手霜")
print (",".join(seg_list)) #默认精确模式
seg_list = jieba.cut_for_search("德国贺本清herbacin 洋甘菊护手霜")
print (",".join(seg_list)) #搜索引擎模式
seg_list = jieba.cut("德国爱他美Aptamil Profutura白金版奶粉 Pre段")
print ("Default Mode:", '/'.join(seg_list)) # 精确模式
seg_list = jieba.cut("贝德玛舒研多效洁肤液")
print ("Default Mode:", '/'.join(seg_list)) # 精确模式
seg_list = jieba.cut("德国芭乐雅Balea 玻尿酸浓缩精华安瓶提拉紧致")
print ("Default Mode:", '/'.join(seg_list)) # 精确模式

