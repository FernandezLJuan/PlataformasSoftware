#!/usr/bin/env python
import rospy

rospy.init_node('ejercicio1')
rate=rospy.Rate(2)
while not rospy.is_shutdown():

	print("Hola mundo") #while True, termina cuando se pulsa ctrl+c
	rate.sleep()
