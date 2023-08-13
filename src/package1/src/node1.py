#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

def example_node():
    rospy.init_node('example_node', anonymous=True)
    
    pub = rospy.Publisher('example_topic', String, queue_size=10)

    pub_int = rospy.Publisher('example_topic_int', Int32, queue_size=10)

    
    rate = rospy.Rate(1)  # 1 Hz
    message_int = 0

    while not rospy.is_shutdown():
        # message = "Hello, ROS!"
        rospy.loginfo(message_int)
        # pub.publish(message)
        pub_int.publish(message_int)
        rate.sleep()
        message_int+=1




if __name__ == '__main__':
    try:
        example_node()
    except rospy.ROSInterruptException:
        pass
