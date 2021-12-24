import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np ,math ,time 



def main(data):  # 앞 물체 따라가기
    rospy.init_node('follow')
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=5)

    new_range = [data.ranges[0:7], data.ranges[-7:]]
    new_arry = np.array(new_range)

    result = np.count_nonzero( new_arry >= 0.5)
    result2 = np.count_nonzero( new_arry >= 0.13)

    msg = Twist()
 
    left_range = data.ranges[85:95]
    left_range = np.array(left_range)
    left_range_result = np.count_nonzero( left_range >= 0.4)
    # print(left_range,'&&&&',left_range_result)

    right_range = data.ranges[265:275]
    right_range = np.array(right_range)
    right_range_result = np.count_nonzero( right_range >= 0.4)
    # print(right_range,'&&&&',right_range_result)


    back_range = data.ranges[167:173]
    back_range = np.array(back_range)
    back_range_result = np.count_nonzero( back_range >= 0.15)
    # print(back_range,'&&&&',back_range_result)


    left_range_45 = data.ranges[33:40]
    left_range_45 = np.array(left_range_45)
    left_range_45_result = np.count_nonzero( left_range_45 >= 0.4)

    right_range_45 = data.ranges[320:327]
    right_range_45 = np.array(right_range_45)
    right_range_45_reselt = np.count_nonzero( right_range_45 >= 0.4)


    if result == 0 :
        msg.angular.z = 0
        msg.linear.x = 0.1
        if result2 == 0:
            msg.linear.x = -0.1

        if left_range_45_result == 0:
            msg.linear.x = 0.1
            msg.angular.z = 1
        if right_range_45_reselt == 0:
            msg.linear.x = 0.1
            msg.angular.z = -1
    
    # elif result >0 :
    #     msg.angular.z = 1
    #     msg.angular.z = -1
    else :
        if result > 0:
            if right_range_result == 0 :
                msg.angular.z = -1
            if left_range_result == 0 :
                msg.angular.z = 1

            if left_range_45_result == 0:
                msg.linear.x = 0
                msg.angular.z = 1
            if right_range_45_reselt == 0:
                msg.linear.x = 0
                msg.angular.z = -1
        


    pub.publish(msg)



if __name__ == '__main__' :
    rospy.init_node('follow')
    rospy.Subscriber('/scan',LaserScan,main)
    rospy.spin()