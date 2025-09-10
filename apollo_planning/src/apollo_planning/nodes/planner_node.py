#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class PlannerNode(Node):
    def __init__(self):
        super().__init__('planner_node')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.t = 0.0
        self.timer = self.create_timer(0.1, self.on_timer)  # 10 Hz
        self.get_logger().info('Planner started: publishing /cmd_vel')

    def on_timer(self):
        msg = Twist()
        msg.linear.x = 0.5 + 0.3 * math.sin(self.t)
        msg.angular.z = 0.4 * math.sin(self.t * 0.5)
        self.pub.publish(msg)
        self.t += 0.1

def main():
    rclpy.init()
    node = PlannerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
