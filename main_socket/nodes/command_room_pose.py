#! /usr/bin/env python3

import rospy
import socket
import pickle
import rospy
import sys, select, termios, tty

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)

    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == '__main__':
    rospy.init_node('movebase_client_py')

    turtle1_ip = '192.168.0.32'
    turtle2_ip = '192.168.0.40'
    turtle3_ip = '192.168.0.31'
    turtle4_ip = '192.168.0.6'

    sender = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)

    settings = termios.tcgetattr(sys.stdin)
    prev_pos = None
    tar_position=None
    bot_ip = None
    room_1 = [1, -1.1, -2.3, 0.0]  ## room number , x, y, z
    room_2 = [2, 2.5, -2.0, 0.0]
    room_3 = [3, -0.5, -0.5, 0.0]
    room_4 = [4, -0.5, -0.5, 0.0]

    while True:
        try:
            key = getKey()
            if key == '1':
                print('room 1')
                tar_position = room_1
                bot_ip = turtle1_ip
            elif key == '2':
                print('room2')
                tar_position = room_2
                bot_ip = turtle2_ip
            elif key == '3':
                tar_position = room_3
                bot_ip = turtle1_ip
            elif key == '4':
                tar_position = room_4
                bot_ip = turtle2_ip

            elif key == 'q':
                break
            else :
                tar_position = None

            if tar_position != None:
                room_pose=pickle.dumps(tar_position)
                sender.sendto(room_pose,(bot_ip,5555))

        except KeyboardInterrupt :
            break