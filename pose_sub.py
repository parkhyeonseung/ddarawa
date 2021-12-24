#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(data):
    print(data.pose.pose.position.x)
    print(data.pose.pose.position.y)
    print(data.pose.pose.orientation.z)

    pass

rospy.init_node('pose_pub')
rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback)
rospy.spin()