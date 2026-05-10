import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math


class DrawSquare(Node):
    def __init__(self, turtle_name='turtle1'):
        super().__init__('draw_square')
        self.turtle_name = turtle_name
        self.publisher = self.create_publisher(Twist, f'/{turtle_name}/cmd_vel', 10)
        self.get_logger().info(f'Dibujante de cuadrados listo para {turtle_name}.')

    def draw_square(self, side_length=1.0, speed=1.0):
        """Dibuja un cuadrado con la tortuga."""
        msg = Twist()
        
        for _ in range(4):
            # Mover hacia adelante
            msg.linear.x = speed
            msg.angular.z = 0.0
            duration = side_length / speed
            start_time = time.time()
            
            while time.time() - start_time < duration:
                self.publisher.publish(msg)
                time.sleep(0.05)
            
            # Girar 90 grados a la izquierda
            msg.linear.x = 0.0
            msg.angular.z = math.pi / 2  # 90 grados
            rotate_duration = (math.pi / 2) / 1.5  # velocidad angular = 1.5 rad/s
            start_time = time.time()
            
            while time.time() - start_time < rotate_duration:
                self.publisher.publish(msg)
                time.sleep(0.05)
        
        # Detener
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher.publish(msg)
        self.get_logger().info(f'Cuadrado de lado {side_length} dibujado en {self.turtle_name}.')


def main():
    rclpy.init()
    node = DrawSquare(turtle_name='turtle1')
    node.draw_square(side_length=2.0, speed=1.0)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
