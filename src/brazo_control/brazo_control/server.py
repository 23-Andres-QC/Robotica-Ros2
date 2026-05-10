import rclpy
from rclpy.node import Node
from brazo_interfaces.srv import MoverBrazo


class MoverBrazoServer(Node):
    def __init__(self):
        super().__init__('mover_brazo_server')
        self.srv = self.create_service(MoverBrazo, '/mover_brazo', self.handle_mover)
        self.get_logger().info('Servidor de MoverBrazo listo.')

    def handle_mover(self, request, response):
        angulos = {
            'theta1': request.theta1,
            'theta2': request.theta2,
            'theta3': request.theta3,
        }
        self.get_logger().info(f'Petición recibida: {angulos}')
        fuera = [name for name, v in angulos.items() if not (-180.0 <= v <= 180.0)]

        if fuera:
            response.exito = False
            response.estado = (
                f'Ángulos fuera de rango [-180,180]: {", ".join(fuera)}')
            self.get_logger().warning(response.estado)
            return response

        response.exito = True
        response.estado = (
            f'Brazo movido a θ1={request.theta1:.2f}°, '
            f'θ2={request.theta2:.2f}°, θ3={request.theta3:.2f}°'
        )
        self.get_logger().info(response.estado)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = MoverBrazoServer()
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
