import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math


class DrawCircle(Node):
    def __init__(self, turtle_name='turtle1'):
        super().__init__('draw_circle')
        self.turtle_name = turtle_name
        self.publisher = self.create_publisher(Twist, f'/{turtle_name}/cmd_vel', 10)
        self.get_logger().info(f'Dibujante de círculos listo para {turtle_name}.')

    def draw_circle(self, radius=1.0, speed=1.0):
        """Dibuja un círculo con la tortuga."""
        msg = Twist()
        
        # Para un círculo: velocidad lineal constante, velocidad angular constante
        # Circunferencia = 2 * pi * radio
        circumference = 2 * math.pi * radius
        duration = circumference / speed
        
        # Velocidad angular necesaria para girar 360 grados en ese tiempo
        angular_velocity = (2 * math.pi) / duration
        
        msg.linear.x = speed
        msg.angular.z = angular_velocity
        
        start_time = time.time()
        while time.time() - start_time < duration:
            self.publisher.publish(msg)
            time.sleep(0.05)
        
        # Detener
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher.publish(msg)
        self.get_logger().info(f'Círculo de radio {radius} dibujado en {self.turtle_name}.')


def main():
    rclpy.init()
    node = DrawCircle(turtle_name='turtle1')
    node.draw_circle(radius=1.0, speed=1.0)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
