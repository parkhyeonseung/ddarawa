#! /usr/bin/env python3

import rospy
import socket
import pickle

def callback_t3(data):
    t3_ip = '192.168.0.16'
    sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    data = pickle.dumps(data)
    sender.sendto(data,(t3_ip,7778))


if __name__=='__main__':
    rospy.init_node('master_receive_t3pose')
    rospy.Subscriber('t3_command', callback=callback_t3)
    rospy.spin()

    pass