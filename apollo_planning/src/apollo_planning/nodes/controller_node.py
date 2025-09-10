#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.sub = self.create_subscription(Twist, '/cmd_vel', self.on_cmd, 10)
        self.get_logger().info('Controller started: subscribing /cmd_vel')

    def on_cmd(self, msg: Twist):
        self.get_logger().info(
            f'cmd_vel: v={msg.linear.x:.2f} m/s, yaw_rate={msg.angular.z:.2f} rad/s'
        )

def main():
    rclpy.init()
    node = ControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
