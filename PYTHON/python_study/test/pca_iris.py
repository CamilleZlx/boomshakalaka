#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def loadDataSet(fileName, delim=','):
    fr = open(fileName)
    stringArr1 = []
    # stringArr2 = []
    # stringArr3 = []
    for line in fr:
        if line.find(u'Iris-setosa') != -1:
            stringArr1.append(line.strip(u',Iris-setosa\n').split(delim))
        elif line.find(u'Iris-versicolor') != -1:
            stringArr1.append(line.strip(u',Iris-versicolor\n').split(delim))
        else:
            stringArr1.append(line.strip(u',Iris-virginica\n').split(delim))
    datArr1 = [map(float, line) for line in stringArr1]
    return np.mat(datArr1)


def pca(dataMat, topNfeat):
    # 去除平均值
    meanVals = np.mean(dataMat, axis=0)
    # print meanVals
    meanRemoved = dataMat - meanVals
    # print meanRemoved
    covMat = np.cov(meanRemoved, rowvar=False)
    # print covMat
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))  # 返回特征值和特征向量
    print u'协方差特征值：', eigVals
    print u'协方差特征向量：'
    print eigVects
    eigValInd = np.argsort(eigVals)  # 返回数组值(特征值)从小到大的索引值
    # print eigValInd
    eigValInd = eigValInd[:-(topNfeat + 1):-1]  # 选择维度
    # print eigValInd
    redEigVects = eigVects[:, eigValInd]
    # print redEigVects
    lowDDataMat = meanRemoved * redEigVects
    print u'保留的前%d个特征向量:' % topNfeat
    print lowDDataMat
    reconMat = (lowDDataMat * redEigVects.T) + meanVals  # 重构数据空间
    # print reconMat

    return lowDDataMat, reconMat


def plot_1D(d1):
    dataArr1 = np.array(d1[:50])
    dataArr2 = np.array(d1[50:100])
    dataArr3 = np.array(d1[100:150])
    n = np.shape(dataArr1)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    xcord3 = []
    ycord3 = []

    for i in range(n):
        xcord1.append(dataArr1[i])
        ycord1.append(dataArr1[i])
        xcord2.append(dataArr2[i])
        ycord2.append(dataArr2[i])
        xcord3.append(dataArr3[i])
        ycord3.append(dataArr3[i])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c=u'red')
    ax.scatter(xcord2, ycord2, s=30, c=u'green', marker='s')
    ax.scatter(xcord3, ycord3, s=30, c=u'blue', marker='^')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def plot_2D(d1):
    dataArr1 = np.array(d1[:50])
    dataArr2 = np.array(d1[50:100])
    dataArr3 = np.array(d1[100:150])
    n = np.shape(dataArr1)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    xcord3 = []
    ycord3 = []

    for i in range(n):
        xcord1.append(dataArr1[i, 0])
        ycord1.append(dataArr1[i, 1])
        xcord2.append(dataArr2[i, 0])
        ycord2.append(dataArr2[i, 1])
        xcord3.append(dataArr3[i, 0])
        ycord3.append(dataArr3[i, 1])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red')
    ax.scatter(xcord2, ycord2, s=30, c='green', marker='s')
    ax.scatter(xcord3, ycord3, s=30, c='blue', marker='^')

    plt.xlabel('X')
    plt.ylabel('Y')
    # plt.ylabel('Z')
    plt.show()


def plot_3D(d1):
    dataArr1 = np.array(d1[:50])
    dataArr2 = np.array(d1[50:100])
    dataArr3 = np.array(d1[100:150])
    n = np.shape(dataArr1)[0]
    xcord1 = []
    ycord1 = []
    zcord1 = []
    xcord2 = []
    ycord2 = []
    zcord2 = []
    xcord3 = []
    ycord3 = []
    zcord3 = []

    for i in range(n):
        xcord1.append(dataArr1[i, 0])
        ycord1.append(dataArr1[i, 1])
        zcord1.append(dataArr1[i, 2])
        xcord2.append(dataArr2[i, 0])
        ycord2.append(dataArr2[i, 1])
        zcord2.append(dataArr1[i, 2])
        xcord3.append(dataArr3[i, 0])
        ycord3.append(dataArr3[i, 1])
        zcord3.append(dataArr1[i, 2])

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(xcord1, ycord1, zcord1)
    ax = Axes3D(fig)
    ax.scatter(xcord1, ycord1, zcord1, s=30, c='red', marker='o')
    ax.scatter(xcord2, ycord2, zcord2, s=30, c='green', marker='s')
    ax.scatter(xcord3, ycord3, zcord3, s=30, c='blue', marker='^')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

if __name__ == '__main__':
    data1 = loadDataSet('iris.data.txt')
    # print data1
    print u'显示一维：'
    a1, b1 = pca(data1, 1)  # 选择一维
    # print a1, b1
    plot_1D(a1)
    print u'显示二维：'
    a2, b2 = pca(data1, 2)  # 选择二维
    plot_2D(a2)
    print u'显示三维：'
    a3, b3 = pca(data1, 3)
    plot_3D(a3)
