#!/usr/bin/env python
import roslib; roslib.load_manifest('hector_keyboard_teleop')
import rospy
from geometry_msgs.msg import Twist
import sys

twist = Twist()

def direction(input):
    switcher = {'a':(1,0,0,0),'d':(-1,0,0,0),'w':(0,1,0,0),'s':(0,-1,0,0),'.':(0,0,0,0),'z':(0,0,1,0),'c':(0,0,-1,0)}
    twist.linear.x, twist.linear.y, twist.linear.z, twist.angular.z = switcher[input]
	#print twist.linear.x, twist.linear.y, twist.linear.z, twist.angular.z
    #print input
    return twist

def keyboard():
    pub = rospy.Publisher('cmd_vel',Twist, queue_size=1)
    rospy.init_node('hector_keyboard_teleop',anonymous=True)
    rate = rospy.Rate(1) 
    #print 'Out'
    flag = 0
    while not rospy.is_shutdown() and flag == 0:
	#print 'In'        
	twistinfo = 'zzwdsacc'
	for i in range(0,len(twistinfo)):
            twi = direction(twistinfo[i])
	    #print i,twi
	    pub.publish(twi)
	    rospy.sleep(0.1)
  	    pub.publish(twi)
	    rospy.sleep(1)
    flag = 1
    rate.sleep()

if __name__ == '__main__':
    try:       
	keyboard()
    except rospy.ROSInterruptException:
        pass
