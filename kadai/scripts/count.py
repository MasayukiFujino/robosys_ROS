#!/usr/bin/env python

MODULE_AUTHOR("Ryuichi Ueda");
MODULE_DESCRIPTION("send numbers");
MODULE_LICENSE("BSD");
MODULE_VERSION("0.0.1");

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
