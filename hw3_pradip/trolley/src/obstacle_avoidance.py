#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float64

def callback_laser(msg):
    
    scanning_area = {
    
        'front_right' : min(min(msg.ranges[180:300]),5),
        'front': min(min(msg.ranges[331:420]),5),
        'front_left': min(min(msg.ranges[421:540]),5),
    
    }
    move_car(scanning_area)
                
def move_car(scanning_area):
    
    msg1 = Float64()
    msg2 = Float64()

    
    scanning_status= ''
    
    if scanning_area['front'] > 4 and scanning_area['front_left'] > 4 and scanning_area['front_right'] > 4:
        scanning_status = 'There is nothing in front of car. Car is moving forward'
        rospy.loginfo(scanning_status)
        msg1 = 10
        pub3.publish(msg1)
        pub4.publish(-msg1)
        msg2 = 0.01
        pub1.publish(msg2)
        pub2.publish(-msg2)
        
    elif scanning_area['front'] < 4 and scanning_area['front_left'] < 4 and scanning_area['front_right'] < 4:
        scanning_status = 'There is a obstacle in front of car. Car is steeing toward right side'
        rospy.loginfo(scanning_status)
        msg1 = 10
        pub3.publish(msg1)
        pub4.publish(-msg1)
        msg2 = -4.0
        pub1.publish(msg2)
        pub2.publish(-msg2)
        
    elif scanning_area['front'] < 4 and scanning_area['front_left'] < 4 and scanning_area['front_right'] > 4:
        scanning_status = 'There is a obstacle in front or front left  of car. Car is steeing toward right side'
        rospy.loginfo(scanning_status)
        msg1 = 10
        pub3.publish(msg1)
        pub4.publish(-msg1)
        msg2 = -4.0
        pub1.publish(msg2)
        pub2.publish(-msg2)
        
    elif scanning_area['front'] < 4 and scanning_area['front_left'] > 4 and scanning_area['front_right'] < 4:
        scanning_status = 'There is a obstacle front or front right of car. Car is steeing toward left side'
        rospy.loginfo(scanning_status)
        msg1 = 10
        pub3.publish(msg1)
        pub4.publish(-msg1)
        msg2 = 4.0
        pub1.publish(msg2)
        pub2.publish(-msg2)
        
    elif scanning_area['front'] > 4 and scanning_area['front_left'] < 4 and scanning_area['front_right'] > 4:
        scanning_status = 'There is a obstacle in front left  of car. Car is steeing toward right side'
        rospy.loginfo(scanning_status)
        msg1 = 10
        pub3.publish(msg1)
        pub4.publish(-msg1)
        msg2 = -4.0
        pub1.publish(msg2)
        pub2.publish(-msg2)
        
    elif scanning_area['front'] > 4 and scanning_area['front_left'] > 4 and scanning_area['front_right'] < 4:
        scanning_status = 'There is a obstacle in front right of car. Car is steeing toward right side'
        rospy.loginfo(scanning_status)
        msg1 = 10
        pub3.publish(msg1)
        pub4.publish(-msg1)
        msg2 = 4.0
        pub1.publish(msg2)
        pub2.publish(-msg2)
        
    elif scanning_area['front'] > 4 and scanning_area['front_left'] < 4 and scanning_area['front_right'] < 4:
        scanning_status = 'There is a nothing in front of car. Car is moving forward'
        rospy.loginfo(scanning_status)
        msg1 = 10
        pub3.publish(msg1)
        pub4.publish(-msg1)
        msg2 = 0.01
        pub1.publish(msg2)
        pub2.publish(-msg2)
        
    else:
        scanning_status = 'Status not determined'
        rospy.loginfo(scanning_area)
        
def main():
    
    global pub1 , pub2 , pub3, pub4
    
    rospy.init_node('obstacle_avoidance', anonymous = True)
    
    pub1 = rospy.Publisher('/trolley/FL_axel_controller/command', Float64, queue_size=1)
    pub2 = rospy.Publisher('/trolley/FR_axel_controller/command', Float64, queue_size=1)
    pub3 = rospy.Publisher('/trolley/RL_wheel_controller/command', Float64, queue_size=1)
    pub4 = rospy.Publisher('/trolley/RR_wheel_controller/command', Float64, queue_size=1)
    
    sub = rospy.Subscriber('/trolley/scan', LaserScan, callback_laser)

    rospy.spin()        

if __name__=='__main__':
        main()
    
    
    


