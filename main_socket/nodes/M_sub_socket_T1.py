#! /usr/bin/env python3

import rospy
import socket
import pickle

def callback_t1(data):
    t1_ip = '192.168.0.16'
    sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    data = pickle.dumps(data)
    # sender.sendto(data,(t1_ip,7778))
    print(data)


if __name__=='__main__':
    rospy.init_node('master_receive_t1pose')
    rospy.Subscriber('t1_command', callback=callback_t1)
    rospy.spin()

    pass