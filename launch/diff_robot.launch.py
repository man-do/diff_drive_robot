from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory, get_package_prefix

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():

    ros_ign_gazebo_dir = get_package_share_directory('ros_ign_gazebo')
    diff_robot_dir = get_package_share_directory('diff_robot')

    # get robot sdf
    # robot_sdf = os.path.join(
    #         get_package_prefix('diff_robot'),
    #         'world',
    #         'robot.sdf'
    #         )

    return LaunchDescription([
        Node(
            package='diff_robot',
            namespace='twist_pub',
            executable='twist_pub',
            name='twist_pub'
        ),

        
        
        # IncludeLaunchDescription(
        # PythonLaunchDescriptionSource(
        #         ros_ign_gazebo_dir + '/launch/ign_gazebo.launch.py' + ' '
        #         + diff_robot_dir + 'world/robot.sdf')),

        
        # Launch Ignition Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution(
                    [
                        FindPackageShare("ros_ign_gazebo"),
                        "launch",
                        "ign_gazebo.launch.py",
                    ]
                )
            ),
            launch_arguments=[("ign_args", 
            ['/home/maverick/upwork/diff_sim_ws/src/diff_robot/world/robot.sdf'])],
        ),
    ])


    # diff_robot_dir + '/world/robot.sdf'