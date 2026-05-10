import rclpy

from rclpy.action import ActionClient
from rclpy.node import Node

from trayectoria_interfaces.action import EjecutarTrayectoria


class TrayectoriaClient(Node):

    def __init__(self):

        super().__init__('trayectoria_client')

        self._action_client = ActionClient(self, EjecutarTrayectoria, 'ejecutar_trayectoria')
        self._goal_handle = None
        self._cancel_sent = False

    def send_goal(self, angulos):

        if len(angulos) < 4:
            self.get_logger().error('Se requieren al menos 4 angulos.')
            return

        self._action_client.wait_for_server()

        goal_msg = EjecutarTrayectoria.Goal()
        goal_msg.angulos = angulos

        send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback,
        )
        send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):

        self._goal_handle = future.result()

        if not self._goal_handle.accepted:
            self.get_logger().info('Goal rechazado por el servidor.')
            rclpy.shutdown()
            return

        self.get_logger().info('Goal aceptado por el servidor.')
        result_future = self._goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):

        porcentaje = feedback_msg.feedback.porcentaje_completitud
        self.get_logger().info(f'Feedback recibido: {porcentaje:.1f}%')

        if porcentaje > 60.0 and not self._cancel_sent and self._goal_handle is not None:
            self._cancel_sent = True
            self.get_logger().warning('Solicitando cancelacion del goal.')
            self._goal_handle.cancel_goal_async()

    def result_callback(self, future):

        result = future.result().result
        self.get_logger().info(
            f'Resultado final: completado={result.completado}, tiempo_total={result.tiempo_total:.2f}s'
        )
        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)
    client = TrayectoriaClient()
    client.send_goal([30.0, 45.0, -20.0, 90.0])
    rclpy.spin(client)
    client.destroy_node()


if __name__ == '__main__':
    main()
