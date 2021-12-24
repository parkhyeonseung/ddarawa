#! /usr/bin/env python3

import rospy
import socket
import pickle

if __name__=='__main__':
    rospy.init_node('master_receive_pose')
    main_ip = '192.168.0.16'
    receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    receiver.bind((main_ip,7778))
    
    while True:
        bytepair = receiver.recvfrom(1024)
        message = pickle.loads(bytepair[0]) 
        