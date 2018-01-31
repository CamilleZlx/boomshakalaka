# import tensorflow as tf    
# x=tf.constant([[1.,2.],[5.,2.]])    
  
  
# xShape=tf.shape(x)  
# z1=tf.reduce_mean(x,axis=0)#沿axis=0操作  
# z2=tf.reduce_mean(x,axis=1)#沿axis=1操作  
  
  
# with tf.Session() as sess:  
#     xShapeValue,d1,d2=sess.run([xShape,z1,z2])  
#     print('shape= %s'%(xShapeValue))  
#     print(d1)  
#     print(d2)

import tensorflow as tf    
x=tf.constant([[[1.,2.],[5.,2.]],[[1.,2.],[5.,2.]]])    
  
xShape=tf.shape(x)  
z1=tf.reduce_mean(x,axis=0)#沿axis=0操作  
z2=tf.reduce_mean(x,axis=1)#沿axis=1操作  
  
with tf.Session() as sess:  
    xShapeValue,d1,d2=sess.run([xShape,z1,z2])  
    print('shape= %s'%(xShapeValue))  
    print(d1)  
    print(d2) 