# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#求均值
def meanX(dataX):
	return np.mean(dataX,axis=0)
	
#计算方差
def variance(X):
	m,n = np.shape(X)  #获取矩阵的行数m，列数n
	mu = meanX(X)  #求出矩阵X的均值mu
	#将每个特征值都减去均值
	muAll = np.tile(mu , (m,1))  
	X1 = X - muAll
	
	variance = 1./m * np.diag(dot(X1.T,X1))
	return variance
	
#标准化
def normalize(X):
	m,n = np.shape(X)
	mu = meanX(X)
	muAll = np.tile(mu,(m,1))
	X1 = X-muAll
	X2 = np.tile(np.diag(X.T*X),(m,1))
	XNorm = X1/X2
	return normalize
	
def pca(XMat,k):
	#将XMat的每一行（代表一个属性字段）进行零均值化，即减去这一行的均值
	average = meanX(XMat)
	m,n = np.shape(XMat)
	data_adjust = []  #申明一个空矩阵
	avgs = np.tile(average,(m,1))
	data_adjust = XMat - avgs
	
	#求出协方差矩阵
	covX = np.cov(data_adjust.T)
	#求解协方差矩阵的特征值和特征向量
	featValue,featVec = np.linalg.eig(covX)
	print u'协方差特征值：',featValue
	print u'协方差特征向量：'
	print featVec
	
	#将特征向量按照对应特征值得大小，从大到小排序
	index = np.argsort(-featValue)
	finalData = []
	
	if k > n:
		print 'k must lower than feature number'
		return 
	else:
		#注意特征向量为列向量
		selectVec = np.matrix(featVec.T[index[:k]])
		finalData = data_adjust * selectVec.T
		print u'保留前%d个特征向量：' % k
		print finalData
		#重构数据空间
		reconData = (finalData * selectVec)+average
		
	return finalData,reconData
		
def loadData(fileName,delim = ','):
	fr = open(fileName)
	stringArr = []
	for line in fr:
		if  line.find(u'Iris-setosa') != -1:
			stringArr.append(line.strip(u',Iris-setosa\n').split(delim))
		elif line.find(u'Iris-versicolor') != -1:
			stringArr.append(line.strip(u',Iris-versicolor\n').split(delim))
		else :
			stringArr.append(line.strip(u',Iris-virginica\n').split(delim))
	datArr1 = [map(float,line) for line in stringArr]
	return  np.mat(datArr1)
	
def plot_1D(d1):
	dataArr1 = np.array(d1[:50])
	dataArr2 = np.array(d1[50:100])
	dataArr3 = np.array(d1[100:150])
	n = np.shape(dataArr1)[0]
	x1 = []
	y1 = []
	x2 = []
	y2 = []
	x3 = []
	y3 = []
	
	for i in range(n):
		x1.append(dataArr1[i])
		y1.append(dataArr1[i])
		x2.append(dataArr2[i])
		y2.append(dataArr2[i])
		x3.append(dataArr3[i])
		y3.append(dataArr3[i])

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(x1,y1,s=30,c=u'magenta')
	ax.scatter(x2,y2,s=30,c=u'yellow',marker = 's')
	ax.scatter(x3,y3,s=30,c=u'blue',marker = '^')
	
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig("plot_1D.png")
	plt.show()
	
def plot_2D(d1):
	dataArr1 = np.array(d1[:50])
	dataArr2 = np.array(d1[50:100])
	dataArr3 = np.array(d1[100:150])
	n = np.shape(dataArr1)[0]
	x1 = []
	y1 = []
	x2 = []
	y2 = []
	x3 = []
	y3 = []

	for i in range(n):
		x1.append(dataArr1[i, 0])
		y1.append(dataArr1[i, 1])
		x2.append(dataArr2[i, 0])
		y2.append(dataArr2[i, 1])
		x3.append(dataArr3[i, 0])
		y3.append(dataArr3[i, 1])

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(x1, y1, s=30, c='magenta')
	ax.scatter(x2, y2, s=30, c='yellow', marker='s')
	ax.scatter(x3, y3, s=30, c='blue', marker='^')

	plt.xlabel('X')
	plt.ylabel('Y')
	plt.savefig("plot_2D.png")
	plt.show()


def plot_3D(d1):
	dataArr1 = np.array(d1[:50])
	dataArr2 = np.array(d1[50:100])
	dataArr3 = np.array(d1[100:150])
	n = np.shape(dataArr1)[0]
	x1 = []
	y1 = []
	z1 = []
	x2 = []
	y2 = []
	z2 = []
	x3 = []
	y3 = []
	z3 = []

	for i in range(n):
		x1.append(dataArr1[i, 0])
		y1.append(dataArr1[i, 1])
		z1.append(dataArr1[i, 2])
		x2.append(dataArr2[i, 0])
		y2.append(dataArr2[i, 1])
		z2.append(dataArr1[i, 2])
		x3.append(dataArr3[i, 0])
		y3.append(dataArr3[i, 1])
		z3.append(dataArr1[i, 2])

	fig = plt.figure()
	ax = Axes3D(fig)
	ax.scatter(x1, y1, z1, s=30, c='magenta', marker='o')
	ax.scatter(x2, y2, z2, s=30, c='yellow', marker='s')
	ax.scatter(x3, y3, z3, s=30, c='blue', marker='^')

	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Z")
	plt.savefig("plot_3D.png")
	plt.show()
	
if __name__ == '__main__':
	data = loadData('iris.data.txt')
	print u'k = 1:'
	a1,b1 = pca(data,1)
	plot_1D(a1)
	print u'k = 2:'
	a2,b2 = pca(data,2)
	plot_2D(a2)
	print u'k = 3:'
	a3,b3 = pca(data,3)
	plot_3D(a3)
