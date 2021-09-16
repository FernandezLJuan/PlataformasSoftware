#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('publicador_texto')

pub=rospy.Publisher('/mensajes',String,queue_size=1)
rate=rospy.Rate(2)

while not rospy.is_shutdown():

	pub.publish('hola mundo')
