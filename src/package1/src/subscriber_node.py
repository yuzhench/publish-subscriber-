#!/usr/bin/python3

import rospy
from std_msgs.msg import String


def callback(data):
   rospy.loginfo(f"the message we lisen is {data.data}")



def lisener():
   rospy.init_node("subscriber_node",anonymous=True)
   rospy.Subscriber("message_and_time", String, callback)
   rospy.spin()


if __name__ == '__main__':
    try:
      lisener()
    except rospy.ROSInterruptException:
       pass



