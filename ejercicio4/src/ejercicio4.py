#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(msg):
	
	print msg.data

rospy.init_node('ejercicio4')
sub=rospy.Suscriber('/prueba',Int32,callback)
rospy.spin()
