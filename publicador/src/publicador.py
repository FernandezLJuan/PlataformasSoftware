#!/usr/bin/env python

import rospy
from publicador.msg import datos

rospy.init_node('publicador')
pub=rospy.Publisher('/mensajes_ejemplo',datos,queue_size=1)
rate=rospy.Rate(2)

mensaje=datos()
mensaje.edad=18
mensaje.altura=1.75
mensaje.nombre="Juan"

while not rospy.is_shutdown():
	
	pub.publish(datos)
	rate.sleep()
