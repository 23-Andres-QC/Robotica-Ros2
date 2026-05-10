import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import time


class SpawnTurtles(Node):
    def __init__(self):
        super().__init__('spawn_turtles')
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.get_logger().info('Esperando al servicio de spawn...')
        
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servicio spawn no disponible, esperando...')

    def spawn_turtle(self, x, y, theta, name):
        """Crea una nueva tortuga en las coordenadas especificadas."""
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = name
        
        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future, timeout_sec=2.0)
        
        if future.done():
            response = future.result()
            self.get_logger().info(f'Tortuga "{name}" creada en ({x}, {y})')
            return response
        else:
            self.get_logger().error(f'Timeout al crear tortuga "{name}"')
            return None


def main():
    rclpy.init()
    node = SpawnTurtles()
    
    # Crear segunda tortuga
    node.spawn_turtle(x=5.0, y=5.0, theta=0.0, name='turtle2')
    
    # Crear tercera tortuga
    node.spawn_turtle(x=2.0, y=8.0, theta=1.57, name='turtle3')
    
    node.get_logger().info('Dos tortugas adicionales creadas.')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
