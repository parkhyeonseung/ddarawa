#! /usr/bin/env python3

import rospy
import socket
import pickle

if __name__=='__main__':

    turtle_ip = '192.168.0.31'

    command_pose = [0,0,0,0.1]
    command_pose=pickle.dumps(command_pose)

    sender = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)
    sender.sendto(command_pose,(turtle_ip,7778))