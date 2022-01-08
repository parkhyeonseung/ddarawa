#! /usr/bin/env python3
import rospy
import socket
from geometry_msgs.msg import PoseStamped

if __name__=='__main__':
    rospy.init_node('a1234')
    turtle1_ip = '192.168.0.28'
    receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    receiver.bind((turtle1_ip,7778))

    while True:
        bytepair = receiver.recvfrom(1024)
        # room_data = pickle.loads(bytepair[0]) 
        print(bytepair)
