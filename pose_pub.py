#! /usr/bin/env pyhton3 

from re import split, sub
import rospy
from rospy.timer import Rate 
from std_msgs.msg import String
from  geometry_msgs import PoseStamped
import pickle 


def callback(data):
    
    data =  data.data.split(sep='_')
    tb = dict()
    for idx in range(len(data)//4):
        name=data[idx]
        x = data[idx+1]
        y = data[idx+2]
        z = data[idx+3]
        tb[name]=[x, y, z]
  
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = float(x)
        goal.pose.position.y = float(y)
        goal.pose.orientation.z = float(z)
        pub = rospy.Publisher(str(name)+'/move_pose/goal',PoseStamped,queue_size=1)  
        pub.publish(goal)

if __name__== '__main__':
    try:
        rospy.init_node('talker', anonymous=True)
        rospy.Subscriber('push_data', String, callback=callback)
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass