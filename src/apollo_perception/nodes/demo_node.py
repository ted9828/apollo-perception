#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class DemoNode(Node):
    def __init__(self):
        super().__init__('demo_node')
        self.timer = self.create_timer(1.0, self.on_timer)
        self.get_logger().info('APOLLO Perception demo node started')

    def on_timer(self):
        self.get_logger().info('perception tick')

def main():
    rclpy.init()
    node = DemoNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


