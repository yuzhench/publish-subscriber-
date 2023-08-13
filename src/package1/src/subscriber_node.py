#!/usr/bin/python3

import rospy
from std_msgs.msg import Int32

def number_callback(msg):
    received_number = msg.data
    doubled_number = received_number * 2
    rospy.loginfo("Received: %d, Doubled: %d", received_number, doubled_number)

def number_subscriber():
    rospy.init_node('number_subscriber')
    rospy.Subscriber('example_topic_int', Int32, number_callback)
    rospy.spin()

if __name__ == '__main__':
    number_subscriber()

