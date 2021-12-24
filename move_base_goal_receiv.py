import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import socket
import pickle ,time

def movebase_client():
    receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    receiver.bind((master_ip,7778))



    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    while True:
        bytepair = receiver.recvfrom(1024)
        message = pickle.loads(bytepair[0]) 
        print(message)
        goal.target_pose.pose.position.x = message[0]
        goal.target_pose.pose.position.y = message[1]
        goal.target_pose.pose.orientation.z = message[2]
        goal.target_pose.pose.orientation.w = message[3]
        time.sleep(0.1)
        break


    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()



master_ip = '192.168.0.16'

if __name__ == '__main__':

    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")