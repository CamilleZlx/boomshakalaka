# 使用 TensorFlow, 你必须明白 TensorFlow:

#   使用图 (graph) 来表示计算任务.
#   在被称之为 会话 (Session) 的上下文 (context) 中执行图.
#   使用 tensor 表示数据.
#   通过 变量 (Variable) 维护状态.
#   使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据.


import tensorflow as tf
import numpy as np

'''
基本用法：构建图
'''
# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中.
#
# 构造器的返回值代表该常量 op 的返回值.
matrix1 = tf.Constant([[3.,3.]])
# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.Constant([[2.], [2.]])
# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)

# 默认图现在有三个节点, 两个 constant() op, 和一个matmul() op. 
# 为了真正进行矩阵相乘运算, 并得到矩阵乘法的 结果, 你必须在会话里启动这个图.
#
# 启动默认图.
sess = tf.Session()
# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数. 
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
# 矩阵乘法 op 的输出.
#
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
# 
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
#
# 返回值 'result' 是一个 numpy `ndarray` 对象.
result = sess.run(product)
print(result)
# ==> 
# 任务完成, 关闭会话.
sess.close()

# Session 对象在使用完后需要关闭以释放资源. 
# 除了显式调用 close 外, 也可以使用 "with" 代码块 来自动完成关闭动作.
with tf.Session() as sess:
    result = sess.run([product])
    print(result)


'''
基本用法：交互式使用
'''
# 文档中的 Python 示例使用一个会话 Session 来 启动图, 并调用 Session.run() 方法执行操作.

# 为了便于使用诸如 IPython 之类的 Python 交互环境, 
# 可以使用 InteractiveSession 代替 Session 类,
# 使用 Tensor.eval() 和 Operation.run() 方法代替 Session.run(). 
# 这样可以避免使用一个变量来持有会话.

'''
Tensor
'''
# TensorFlow 程序使用 tensor 数据结构来代表所有的数据, 计算图中, 操作间传递的数据都是 tensor. 
# 你可以把 TensorFlow tensor 看作是一个 n 维的数组或列表. 
# 一个 tensor 包含一个静态类型 rank, 和 一个 shape. 

'''
变量:Variables
'''

'''
Fetch
'''

'''
Feed
'''


'''
test start
----------------------------------------------------------------------------------------------
'''
# # 使用 NumPy 生成假数据(phony data), 总共 100 个点.
# x_data = np.float32(np.random.rand(2,100)) #随机输入
# y_data = np.dot([0.100 , 0.200], x_data) + 0.300 #dot()返回的是两个数字的点积
# # print(x_data)
# # print(y_data)

# # 构造一个线性模拟
# b = tf.Variable(tf.zeros([1]))
# W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
# y = tf.matmul(W, x_data) + b

# # 最小化方差
# loss = tf.reduce_mean(tf.square(y - y_data))
# optimizer = tf.train.GradientDescentOptimizer(0.5)
# train = optimizer.minimize(loss)

# # 初始化变量
# # init = tf.initialize_all_variables() # 已经弃用
# init = tf.global_variables_initializer()

# # 启动图 (graph)
# sess = tf.Session()
# sess.run(init)

# # 拟合平面
# for step in range(0, 201):
#     sess.run(train)
#     if step % 20 == 0:
#         print (step, sess.run(W), sess.run(b))
'''
test end
----------------------------------------------------------------------------------------------
'''