import tensorflow as tf

a = tf.constant([[1.1,2.2]])
b = tf.constant([[3.3],[4.4]])

y = tf.matmul(a,b)

with tf.Session() as sess:
    print(sess.run(y))