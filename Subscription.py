#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
import csv

l = csv.writer(open("Location.csv", "wb"))
s = csv.writer(open("Sensor.csv", "wb"))

def callback(odom):
    (x,y,z,w,a,b,g) = (odom.pose.pose.position.x,odom.pose.pose.position.y,odom.pose.pose.position.z,odom.pose.pose.orientation.x,odom.pose.pose.orientation.y,odom.pose.pose.orientation.z,odom.pose.pose.orientation.w)
    #print x,y,z,w,a,b,g
    t = rospy.get_time()
    l.writerow([x,y,z,w,a,b,g,t])

def call(Imu):    
    (al,be,ga,a1,b1,c1) = (Imu.linear_acceleration.x,Imu.linear_acceleration.y,Imu.linear_acceleration.z,Imu.angular_velocity.x,Imu.angular_velocity.y,Imu.angular_velocity.z)
    ti = rospy.get_time()
    s.writerow([al,be,ga,a1,b1,c1,ti])

def listener():

    rospy.init_node('location', anonymous=True)

    rospy.Subscriber("ground_truth/state", Odometry, callback, queue_size = 100)
    rospy.Subscriber("raw_imu", Imu, call, queue_size = 100)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
