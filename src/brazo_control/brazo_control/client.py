import sys

import rclpy
from rclpy.node import Node

from brazo_interfaces.srv import MoverBrazo


class MoverBrazoClient(Node):
    def __init__(self):
        super().__init__('mover_brazo_client')
        self.cli = self.create_client(MoverBrazo, 'mover_brazo')
        self.request = MoverBrazo.Request()

    def send_request(self, theta1, theta2, theta3):
        if not self.cli.wait_for_service(timeout_sec=2.0):
            self.get_logger().error('Timeout: el servicio mover_brazo no esta disponible.')
            return None

        self.request.theta1 = theta1
        self.request.theta2 = theta2
        self.request.theta3 = theta3
        return self.cli.call_async(self.request)


def main(args=None):
    rclpy.init(args=args)
    node = MoverBrazoClient()

    if len(sys.argv) < 4:
        node.get_logger().error('Uso: mover_brazo_client <theta1> <theta2> <theta3>')
        node.destroy_node()
        rclpy.shutdown()
        sys.exit(1)

    future = node.send_request(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    if future is None:
        node.destroy_node()
        rclpy.shutdown()
        sys.exit(1)

    rclpy.spin_until_future_complete(node, future, timeout_sec=3.0)

    if future.done():
        response = future.result()
        node.get_logger().info(
            f'Respuesta: exito={response.exito}, estado="{response.estado}"'
        )
    else:
        node.get_logger().error('Timeout: el servidor tardó demasiado en responder.')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
