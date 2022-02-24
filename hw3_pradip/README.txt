## This is a readme file for HW3 of ENPM 690
## Following software/packages are required to run the package.

1. Ubuntu 180.04
2. ROS melodic
3. Gazebo
3. Gazebo plugin



####################################
### operate robot using keyboard ###
####################################

1. Unzip the package and copy 'trolley' folder into src directory of your catkin workspace
2. From terminal nevigate to your catkin workspace and build the package using below command

	> catkin clean
	> catkin_make

3. Launch the package in gazebo using below command

	> roslaunch trolley template_launch.launch

4. Keep the current terminal as it is and open the new terminal
5. Nevigate to catkin_ws/src/trolley/src
6. Launch the keyboard teleop using below command

	> chmod +x teleop_template.py
	> python teleop_template.py

7. You can move robot in the gazebo using below key from keyboard:

	i - move forwards
	, - move backwards
	u - move left
	o - move right
	j - turn left
	l - turn right
	k - force stop


########################
### check Lidar data ###
########################


1. After launching robot in gazebo (step 1,2 and 3 in above instruction), open new terminal and type below command

	> rostopic echo /trolley/scan -n 1

   It will give you the array of obstacle distance measure by each of 720 lidar points.


######################################
### Obstacle avoidance using Lidar ###
######################################

1. Launch the robot in the gazebo as mentioned above.

2. open new terminal and type below command:

	> chmod +x obstacle_avoidance.py
	> python obstacle_avoidance.py 

3. You should see that robot is moving in circular pattern and avoiding obstacle.





