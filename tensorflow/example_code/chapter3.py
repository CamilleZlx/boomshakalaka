'''
2018.1.31 by camille
这是一个简单的实现神经网络的训练过程（二分类问题）
无论神经网络的结构怎么变化，训练神经网络的过程均可以分为以下3步：
1.定义神经网络的结构和前向传播的输出结果
2.定义损失函数及选择反向传播的优化算法
3.生成会话（tf.Session），并且在训练数据集上反复运行反向传播优化算法
-----------------------------------------------------------------------------------------------------
注：
1.TensorFlow最基本的三个概念：计算图、张量、会话
    计算图：所有的TensorFlow程序都会通过计算图的形式表示。计算图上的每一个节点都是一个运算，而计算图上的边
        则表示了运算之间的数据传递关系。计算图上还保存了每个运算的设备信息(比如是通过CPU还是GPU运行)，以及
        运算之间的依赖关系。计算图提供了管理不同集合的功能，并且TensorFlow会自动维护5个不同的默认集合。
    张量：TensorFlow中所有运算的输入、输出都是张量。张量本身并不存储任何数据，它只是对运算结果的引用。通过
        张量。可以更好的组织TensorFlow程序。
    会话：管理一个TensorFlow程序拥有的系统资源，所有的运算都要通过会话执行。
2.TensorFlow计算模型--计算图
  TensorFlow数据模型--张量（多维数组），属性：名字(name)、维度(shape)、类型(type)
  TensorFlow运行模型--会话
3.变量 tf.Variable(),属性：维度(shape)(可变，设置variable_shape=False，实际中运用较少)，类型(type)(不可变)
4.TensorFlow支持7种不同的优化器，常用的有3种：tf.train.GradientDescentOptimizer、tf.train.AdamOptimizer和
tf.train.MomentumOptimizer
-----------------------------------------------------------------------------------------------------
'''

import tensorflow as tf
# 利用numpy生成模拟数据集
from numpy.random import RandomState

# 定义训练数据的batch大小
batch_size = 8

# 定义神经网络参数
w1 = tf.Variable(tf.random_normal([2,3], stddev=1.0, seed=1))
w2 = tf.Variable(tf.random_normal([3,1], stddev=1.0, seed=1))

# 在shape的一个维度上使用None可以方便使用不同的batch大小。
# 在训练试试需要把数据分成比较小的batch，但是在测试时，可以一次性的使用全部数据。
# 当数据集比较小时这样可以方便测试，但是数据比较大时，将大量数据放入一个batch可能会导致内存溢出
x = tf.placeholder(tf.float32, shape=(None,2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None,1), name='y-input')

# 定义神经网络向前的传播过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

train_step = tf.train

# 定义损失函数
cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))


# 定义反向传播算法
learning_rate = 0.001 # 学习率
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)


# 通过随机生成一个模拟数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
# 定义规则来给出样本标签，在这里所有的x1+x2<1的样例都被认为是正样本（比如零件合格），而其他为负样本（比如零件不合格）
# 与tensorflow游乐场中的表示法不大一样的地方是，在这里使用0来表示负样本，1来表示正样本。
# 大部分解决分类问题的神经网络都会使用0和1的表示fangf
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

# 创建一个会话来运行tensorflow程序
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    # 初始化变量
    sess.run(init_op)
    print(sess.run(w1))
    print(sess.run(w2))
    
    # 设定训练的轮数
    STEPS = 5000
    for i in range(STEPS):
        # 每次选取batch_size个样本进行训练
        start = (i * batch_size) % dataset_size
        end = min(start+batch_size, dataset_size)

        # 通过选取的样本训练神经网络并更新参数
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})

        if i % 1000 == 0:
            # 每隔一段时间计算在所有数据集上的交叉熵并输出
            total_cross_entropy = sess.run(cross_entropy,feed_dict = {x:X, y_:Y})
            print("After %d training step(s), cross_entropy on all data is %g" %
            (i, total_cross_entropy))

    print(sess.run(w1))
    print(sess.run(w2))