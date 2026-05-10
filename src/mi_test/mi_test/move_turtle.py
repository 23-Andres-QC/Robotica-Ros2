import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info('Nodo de movimiento listo. Moviendo tortuga...')

    def move_forward(self, distance=1.0, speed=1.0):
        """Mueve la tortuga hacia adelante una distancia especificada."""
        msg = Twist()
        msg.linear.x = speed
        msg.angular.z = 0.0
        
        duration = distance / speed
        start_time = time.time()
        
        while time.time() - start_time < duration:
            self.publisher.publish(msg)
            time.sleep(0.1)
        
        msg.linear.x = 0.0
        self.publisher.publish(msg)
        self.get_logger().info(f'Tortuga movida {distance} unidades.')


def main():
    rclpy.init()
    node = MoveTurtle()
    node.move_forward(distance=2.0, speed=1.0)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
