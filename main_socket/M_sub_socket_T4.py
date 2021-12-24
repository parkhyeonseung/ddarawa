#! /usr/bin/env python3

import rospy
import socket
import pickle

def callback_t4(data):
    t4_ip = '192.168.0.16'
    sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    data = pickle.dumps(data)
    sender.sendto(data,(t4_ip,7778))


if __name__=='__main__':
    rospy.init_node('master_receive_pose')
    rospy.Subscriber('t4_command', callback=callback_t4)
    rospy.spin()

    pass