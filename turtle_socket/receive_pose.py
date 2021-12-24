#! /usr/bin/env python3

import rospy
import socket
import pickle

master_ip = '192.168.0.16'

def func():
    pass

if __name__=='__main__':
    receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    receiver.bind((master_ip,7778))
    while True:
        bytepair = receiver.recvfrom(1024)
        message = pickle.loads(bytepair[0]) 
        print(message)