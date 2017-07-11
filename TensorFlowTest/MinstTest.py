import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# import MNIST data
mnist=input_data.read_data_sets("MNIST_data/", one_hot=True)

# define layer
def add_layer(inputs, in_size, out_size,n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name+'/weights',Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/baises', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
            tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs


sess = tf.Session()

# define compute_accuracy
def compute_accuracy(v_xs,v_ys):
  global prediction
  y_pre=sess.run(prediction,{xs:v_xs})
  correct_prediction=tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
  arruracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
  result=sess.run(arruracy,{xs:v_xs,ys:v_ys})
  return result

# define placeholder for inupts tonetwork
xs=tf.placeholder(tf.float32,[None,784])# 28x28
ys=tf.placeholder(tf.float32,[None,10])

# add output layer
prediction=add_layer(xs,784,10,n_layer=1,activation_function=tf.nn.softmax)

# define error between prediciont adn real data
cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


#important step
sess.run(tf.global_variables_initializer())



for i in range(1000):
    batch_xs,batch_ys=mnist.train.next_batch(100)
    if i%50==0:
       sess.run(train_step,{xs:batch_xs,ys:batch_ys})

       print(compute_accuracy(mnist.test.images,mnist.test.labels))






