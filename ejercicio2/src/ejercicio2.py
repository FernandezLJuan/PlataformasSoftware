#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('ejercicio2')
publicador=rospy.Publisher('/prueba',Int32,queue_size=1)

rate=rospy.Rate(0.5)
contador=Int32()
contador.data=0

while not rospy.is_shutdown():

	publicador.publish(contador)
	contador.data+=1
	rate.sleep()
