#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def callback(msg):

	print msg.linear
	print msg.angular

rospy.init_node('ejercicio5')
suscriptor=rospy.Subscriber('/cmd_vel',Twist,callback)

rospy.spin()
