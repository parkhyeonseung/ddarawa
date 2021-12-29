#! /usr/bin/env python3

import rospy
import rospy
import sys, select, termios, tty
from geometry_msgs.msg import PoseStamped

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
    rospy.init_node('T5_move_all')
    pub = rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=10)

    settings = termios.tcgetattr(sys.stdin)
    tar_position=None
    room_1 = [1, 0.0, 0.0, 0]  ## room number , x, y, z
    room_2 = [2, .5, .5, 0]
    room_3 = [3, -0.5, -0.5, 0]
    room_4 = [4, 1.0, 1.0, 0]

    while True:
        try:
            key = getKey()
            if key == '1':
                print('room 1')
                tar_position = room_1
            elif key == '2':
                print('room2')
                tar_position = room_2
            elif key == '3':
                tar_position = room_3
            elif key == '4':
                tar_position = room_4

            elif key == 'q':
                break
            else :
                tar_position = None

            if tar_position != None:
                room_data = tar_position[1:4]
                goal = PoseStamped()
                goal.header.frame_id= 'map'
                goal.pose.orientation.w =float(0.5)
                goal.pose.position.x = float(room_data[0])
                goal.pose.position.y  = float(room_data[1])
                goal.pose.orientation.z  = float(room_data[2])
                rospy.sleep(0.5)
                pub.publish(goal)

        except KeyboardInterrupt :
            break