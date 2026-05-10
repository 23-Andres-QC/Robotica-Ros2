import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class VelSubscriber(Node):

    def __init__(self):
        super().__init__('vel_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)
        self.get_logger().info('VelSubscriber escuchando en /cmd_vel')

    def listener_callback(self, msg: Twist):
        stamp = self.get_clock().now().to_msg()
        t = f'{stamp.sec}.{stamp.nanosec:09d}'
        self.get_logger().info(
            f'[t={t}] lineal=({msg.linear.x:.2f}, {msg.linear.y:.2f}, {msg.linear.z:.2f}) '
            f'angular=({msg.angular.x:.2f}, {msg.angular.y:.2f}, {msg.angular.z:.2f})'
        )


def main(args=None):
    rclpy.init(args=args)
    node = VelSubscriber()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()