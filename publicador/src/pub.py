#!/usr/bin/env python

import rospy
from publicador.msg import datos

rospy.init_node('publicador')
pub=rospy.Publisher('/mensajePers',datos,queue_size=1)
rate=rospy.Rate(2)

mensaje=datos()
mensaje.edad=18
mensaje.coeficiente=1.70
mensaje.nombre="Juan"

while not rospy.is_shutdown():

	pub.publish(mensaje)
	rate.sleep()
