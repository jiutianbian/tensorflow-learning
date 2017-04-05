#coding=utf-8
# 倒入已经通过pip 安装了的tensorflow框架
import tensorflow as tf
# 通过constant命令新建一个tensorflow常量
hello = tf.constant('你好，德玛西亚!')
# 通过Session命令新建会话
sess = tf.Session()
print sess.run(hello)