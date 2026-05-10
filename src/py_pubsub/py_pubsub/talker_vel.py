import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class VelPublisher(Node):

    def __init__(self):
        super().__init__('vel_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.counter = 0
        self.max_ticks = 50
        self.get_logger().info('VelPublisher iniciado, publicando 5 s a 10 Hz')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.1

        self.publisher_.publish(msg)
        self.get_logger().info(
            f'[{self.counter + 1}/50] Publicado lin.x={msg.linear.x} ang.z={msg.angular.z}'
        )

        self.counter += 1
        if self.counter >= self.max_ticks:
            self.get_logger().info('5 s cumplidos, deteniendo el nodo.')
            self.destroy_timer(self.timer)
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = VelPublisher()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass
    finally:
        node.destroy_node()


if __name__ == '__main__':
    main()