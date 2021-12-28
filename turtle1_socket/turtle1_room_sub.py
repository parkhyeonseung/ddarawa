#! /usr/bin/env python3
import rospy
import socket
import pickle
from geometry_msgs.msg import PoseStamped




if __name__ == '__main__':
    rospy.init_node('T1_room_pose')
    pub = rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=10)

    turtle1_ip = '192.168.0.16'
    receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    receiver.bind((turtle1_ip,5555))

    while True:
        bytepair = receiver.recvfrom(1024)
        room_data = pickle.loads(bytepair[0]) 
        try:
            goal = PoseStamped()
            goal.header.frame_id= 'map'
            goal.pose.orientation.w =float(0.5)
            goal.pose.position.x = float(room_data[1])
            goal.pose.position.y  = float(room_data[2])
            goal.pose.orientation.z  = float(room_data[3])
            rospy.sleep(0.5)
            pub.publish(goal)
        except:
            pass