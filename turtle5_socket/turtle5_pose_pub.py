#! /usr/bin/env python3

import rospy
import socket
from geometry_msgs.msg import PoseWithCovarianceStamped
import pickle

def callback(data):
    pose_x = data.pose.pose.position.x
    pose_y = data.pose.pose.position.y
    pose_z = data.pose.pose.orientation.z
    pose_w = data.pose.pose.orientation.w
    print('data import')
    
    position = ['T5',pose_x,pose_y,pose_z,pose_w]
    position=pickle.dumps(position)

    sender = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)
    sender.sendto(position,(master_ip,7778))


if __name__ =='__main__':
    master_ip = '192.168.0.16'
    rospy.init_node('turtle5_pose_pub')
    rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback)
    rospy.spin()
    
