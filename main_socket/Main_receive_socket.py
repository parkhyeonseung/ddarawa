#! /usr/bin/env python3

import rospy
import socket
import pickle
from std_msgs.msg import Float64MultiArray

if __name__=='__main__':
    rospy.init_node('master_receive_pose')
    main_ip = '192.168.0.16'

    ####### turtlebot들한테서 position을 소켓으로 받는 main#############
    receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    receiver.bind((main_ip,7778))

    ####### Main pub 생성 -- main_sub으로 turtle position을 topic으로 보냄// 한파일을 최소화하기위해 or 통신이 원활하지 않을 수 있어서 ###############
    t1_pub = rospy.Publisher('t1_command',Float64MultiArray)
    t2_pub = rospy.Publisher('t2_command',Float64MultiArray)
    t3_pub = rospy.Publisher('t3_command',Float64MultiArray)
    t4_pub = rospy.Publisher('t4_command',Float64MultiArray)
    t5_pub = rospy.Publisher('t5_command',Float64MultiArray)
    ########################################################################

    ####### 소켓으로 받은 데이터를 main sub node로 보냄 ############################
    while True:
        bytepair = receiver.recvfrom(1024)
        turtle_data = pickle.loads(bytepair[0]) 
        turtle_id = turtle_data[0]
        turtle_data = turtle_data[1:5]

        if turtle_id == 'T1':
            t1_pub.publish(turtle_data)

        elif turtle_id == 'T2':
            t2_pub.publish(turtle_data)

        elif turtle_id == 'T3':
            t3_pub.publish(turtle_data)

        elif turtle_id == 'T4':
            t4_pub.publish(turtle_data)

        elif turtle_id == 'T5':
            t5_pub.publish(turtle_data)