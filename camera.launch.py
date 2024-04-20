# to use this you first need to install the v4l-utils library and enable your camera
# sudo apt install libraspberrypi-bin v4l-utils ros-<distro>-v4l2-camera
# install rqt_image_view: sudo apt install ros-<distro>-image-transport-plugins ros-<distro>-rqt-image-view
import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            parameters=[{
                'image_size': [640,480],
                'camera_frame_id': 'camera_link_optical'
            }]
        )
    ])
