#!/usr/bin/env python
import rospy
import random
import numpy as np
from geometry_msgs.msg import Twist

rospy.init_node('ejercicio3')
publicador=rospy.Publisher('/cmd_vel',Twist,queue_size=1)

rate=rospy.Rate(0.5)
dato=Twist()

while not rospy.is_shutdown():
	
	dato.linear.x=np.float64(random.randint(0,499+1))
	dato.linear.y=np.float64(random.randint(0,499+1))
	dato.linear.z=np.float64(random.randint(0,499+1))

	dato.angular.x=np.float64(random.randint(0,499+1))
	dato.angular.y=np.float64(random.randint(0,499+1))
	dato.angular.z=np.float64(random.randint(0,499+1))

	publicador.publish(dato)

	rate.sleep()
	
