#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(msg):

	print msg.data

rospy.init_node('suscriptor_basico')
sub=rospy.Subscriber('/contaor',Int32,callback)
rospy.spin()
