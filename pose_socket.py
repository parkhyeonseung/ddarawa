#! /usr/bin/env python3

import rospy
import socket
import pickle
from std_msgs.msg import String

turtle1_ip = '192.168.0.28'
turtle2_ip = '192.168.0.28'
turtle3_ip = '192.168.0.28'
turtle4_ip = '192.168.0.28'

def callback(data):
    data =  data.data.split(sep='_')
    print(data)
    tb = dict()
    for idx in range(len(data)//4):
        name=data[idx]
        x = data[idx+1]
        y = data[idx+2]
        z = data[idx+3]
        tb[name]=[x, y, z]
    
    # tb에서 데이터 하나씩 뽑기
    for key, value in tb.items():
        print(key, value)
    # 뽑은 터틀봇 주소 확인
        if key == '/tb3-0':
            ip = turtle1_ip
        elif key == '/tb3-1':
            ip = turtle2_ip
        elif key == '/tb3-2':
            ip = turtle3_ip
        elif key == '/tb3-3':
            ip = turtle4_ip
    # 거기다가 좌표 전송
    data=value
    sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    data = pickle.dumps(data)
    sender.sendto(data,(ip,7778))


if __name__ == '__main__':
    rospy.init_node('pose_socket')
    rospy.Subscriber('push_data', String, callback=callback)
    rospy.spin()
