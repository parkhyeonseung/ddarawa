#! /usr/bin/env python3

import rospy
import socket
from geometry_msgs.msg import PoseWithCovarianceStamped
import pickle

master_ip = '192.168.0.16'


def callback(data):
    pose_x = data.pose.pose.position.x
    pose_y = data.pose.pose.position.y
    pose_z = data.pose.pose.orientation.z
    print('data import')
    position = [pose_x,pose_y,pose_z]
    position=pickle.dumps(position)

    sender = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)
    sender.sendto(position,(master_ip,7778))


if __name__ =='__main__':
    rospy.init_node('pose_pub')
    rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback)
    rospy.spin()
    
