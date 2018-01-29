from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import input_data
import tensorflow as tf

# 导入数据
mnist = input_data.read_data_sets("./mnist_data/", one_hot=True)

sess = tf.InteractiveSession()

# 创建模型
x = tf.placeholder(tf.float32,[None,784])
w = tf.Variable(tf.zeros([784,10])) # 权重
b = tf.Variable(tf.zeros([10])) # 偏置
y = tf.nn.softmax(tf.matmul(x,w) + b) # 预测的概率分布

# 定义损失函数
y_ = tf.placeholder(tf.float32,[None,10]) # 实际的概率分布

cross_entropy = -tf.reduce_sum(y_ * tf.log(y)) # 计算交叉熵
# 梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 初始化变量
init = tf.global_variables_initializer()
# 启动模型
sess.run(init)

# 开始训练
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    train_step.run({x: batch_xs, y_: batch_ys})

# 模型评估
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))