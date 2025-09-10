from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='apollo_perception',
            executable='demo_node',
            name='demo_node',
            output='screen'
        )
    ])

