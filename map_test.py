#맵 스캔용 충돌회피주행

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np ,math ,time 



def main(data):  # 맵 스캔용 자율주행
    rospy.init_node('parking')
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)

    new_range = [data.ranges[0:4], data.ranges[-4:]]
    new_arry = np.array(new_range)

    result = np.count_nonzero( new_arry >= 0.25)

    msg = Twist()
 
    left_range = data.ranges[85:95]
    left_range = np.array(left_range)
    left_range_result = np.count_nonzero( left_range >= 0.3)
    # print(left_range,'&&&&',left_range_result)

    right_range = data.ranges[265:275]
    right_range = np.array(right_range)
    right_range_result = np.count_nonzero( right_range >= 0.3)
    # print(right_range,'&&&&',right_range_result)


    back_range = data.ranges[175:185]
    back_range = np.array(back_range)
    back_range_result = np.count_nonzero( back_range >= 0.15)
    # print(back_range,'&&&&',back_range_result)


    left_range_45 = data.ranges[33:40]
    left_range_45 = np.array(left_range_45)
    left_range_45_result = np.count_nonzero( left_range_45 >= 0.15)

    right_range_45 = data.ranges[320:327]
    right_range_45 = np.array(right_range_45)
    right_range_45_reselt = np.count_nonzero( right_range_45 >= 0.15)


    if result > 0 :
        msg.angular.z = 0
        msg.linear.x = 0
    
        msg.linear.x = 0.04
        if left_range_45_result == 0:
            msg.angular.z = -1
            time.sleep(0.2)
        if right_range_45_reselt == 0:
            msg.angular.z =1
            time.sleep(0.2)


        if back_range_result == 0:
            msg.linear.x = 0.04
        else :
            pass

    elif result == 0 :
        if right_range_result == 0:
            msg.angular.z = 1
            time.sleep(0.1)
            if back_range_result == 0:
                msg.linear.x = 0.04
            msg.linear.x =-0.01
            # if back_range_result == 0:
            #     msg.linear.x = 0.05
        
        elif left_range_result == 0:
            msg.angular.z = -1
            time.sleep(0.0)
            if back_range_result == 0:
                msg.linear.x = 0.04
            msg.linear.x =-0.01
                # if back_range_result == 0:
                #     msg.linear.x = 0.05
        else :
            msg.angular.z = 1
            msg.linear.x =-0.03
    else :
        msg.linear.x = -0.03

    pub.publish(msg)



if __name__ == '__main__' :
    rospy.init_node('parking')
    rospy.Subscriber('/scan',LaserScan,main)
    rospy.spin()