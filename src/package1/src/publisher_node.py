#!/usr/bin/python3

import rospy
from std_msgs.msg import String 


def talker_node():
    rospy.init_node("publisher_node",anonymous=True)
    pub = rospy.Publisher("message_and_time",String,queue_size=10)
    rate = rospy.Rate(1)

    rospy.loginfo("now, the node is ready to publish the message")

    while not rospy.is_shutdown():
        message = f"Hello world, the time is {rospy.get_time()}"
        pub.publish(message)
        rate.sleep()





if __name__ == '__main__':
    try:
        talker_node()
    except rospy.ROSInterruptException:
        pass
