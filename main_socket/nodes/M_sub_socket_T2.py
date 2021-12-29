#! /usr/bin/env python3

import rospy
import socket
import pickle

def callback_t2(data):
    t2_ip = '192.168.0.16'
    sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    data = pickle.dumps(data)
    sender.sendto(data,(t2_ip,7778))


if __name__=='__main__':
    rospy.init_node('master_receive_t2pose')
    rospy.Subscriber('t2_command', callback=callback_t2)
    rospy.spin()

    pass