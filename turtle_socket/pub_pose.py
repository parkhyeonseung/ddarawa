#! /usr/bin/env python3

import rospy
import socket
from geometry_msgs.msg import PoseWithCovarianceStamped

master_ip = '192.168.0.16'


def callback(data):
    pose_x = data.pose.pose.position.x
    pose_y = data.pose.pose.position.y
    pose_z = data.pose.pose.orientation.z
    position = [pose_x,pose_y,pose_z]
    sender = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)
    sender.sendto(str.encode(position),(master_ip,1777))


if __name__ =='__main__':
    rospy.init_node('pose_pub')
    rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback)
    rospy.spin()
    
