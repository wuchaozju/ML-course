import tensorflow as tf

one = tf.constant(1)
op_add = tf.add(one, one)
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init_op)
	print(op_add.eval())
