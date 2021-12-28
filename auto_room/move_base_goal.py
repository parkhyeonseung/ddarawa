#! /usr/bin/env python3
import rospy
import actionlib
from geometry_msgs.msg import PoseStamped, Pose
from std_msgs.msg import Header
import sys, select, termios, tty

def movebase_client(tar_position):
    room_num = tar_position[0] 
    if room_num == 1:
        # client = actionlib.SimpleActionClient('tb3_1/move_base',MoveBaseAction)
        pub = rospy.Publisher('/move_base_simple/goal',PoseStamped,queue_size=10)
    elif room_num== 2:
        pub = rospy.Publisher('tb3_2/move_base_simple/goal',PoseStamped)
    elif room_num == 3:
        pub = rospy.Publisher('tb3_3/move_base_simple/goal',PoseStamped)
    elif room_num == 4:
        pub = rospy.Publisher('tb3_4/move_base_simple/goal',PoseStamped)

    # goal.target_pose.header.stamp = rospy.Time.now()
    goal = PoseStamped()
    goal.header.frame_id= 'map'
    goal.pose.orientation.w =float(0.5)
    goal.pose.position.x = float(tar_position[1])
    goal.pose.position.y  = float(tar_position[2])
    goal.pose.orientation.z  = float(tar_position[3])
    rospy.sleep(0.5)
    pub.publish(goal)

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
    settings = termios.tcgetattr(sys.stdin)
    prev_pos = None
    tar_position=None
    room_1 = [1, 1.0, -0.5, 1.0]  ## room number , x, y, z
    room_2 = [2, 2.0, 2.0, 2.0]
    room_3 = [3, 3.0, 3.0, 3.0]
    room_4 = [4, 4.0, 4.0, 4.0]
    while True:
        try:
            key = getKey()
            if key == '1':
                print('room 1')
                tar_position = room_1
            elif key == '2':
                tar_position = room_2
            elif key == '3':
                tar_position = room_3
            elif key == '4':
                tar_position = room_4
            elif key == 'q':
                break
            else :
                tar_position = None
            # if (prev_pos != tar_position) and (prev_pos != None):
            if tar_position != None:

                rospy.init_node('movebase_client_py')
                movebase_client(tar_position)
        except KeyboardInterrupt :
            break