# realsense_spencer_adaptor
A ROS package for running spencer people tracking from a realsense D435i camera.
Contains:

 - a node `realsense_spencer_adaptor.py` for changing the encoding on the realsense depth images to something spencer can handle.
 - a launch file `realsense_people_tracking.launch`, which launches the realsense driver, the spencer algorithm and the adaptor node, and remaps the appropriate topics to ensure everything is connected correctly.

## Usage

 1. Install the [realsense driver](http://wiki.ros.org/realsense2_camera) and [spencer tracking](https://github.com/spencer-project/spencer_people_tracking).
 2. Clone and catkin_make this package in your catkin workspace. Source the workspace.
 4. `roslaunch realsense_spencer_adaptor realsense_people_tracking.launch`

## References

 - Github issue which discusses the depth image encoding issue: https://github.com/spencer-project/spencer_people_tracking/issues/4 
 - Spencer people tracking github: https://github.com/spencer-project/spencer_people_tracking
 - D435 ROS driver: http://wiki.ros.org/realsense2_camera 


