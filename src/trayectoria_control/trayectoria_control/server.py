import rclpy
import time

from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

from trayectoria_interfaces.action import EjecutarTrayectoria


class TrayectoriaServer(Node):

    def __init__(self):

        super().__init__('trayectoria_server')

        self._action_server = ActionServer(
            self,
            EjecutarTrayectoria,
            'ejecutar_trayectoria',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
        )

    def goal_callback(self, goal_request):

        angulos = goal_request.angulos

        if len(angulos) < 4:
            self.get_logger().warning('Goal rechazado: se requieren al menos 4 angulos.')
            return GoalResponse.REJECT

        self.get_logger().info(f'Goal aceptado con {len(angulos)} angulos.')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):

        self.get_logger().info('Solicitud de cancelacion recibida.')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):

        angulos = goal_handle.request.angulos
        total = len(angulos)
        start_time = time.time()
        feedback_msg = EjecutarTrayectoria.Feedback()
        subpasos_por_angulo = 10

        for indice, angulo in enumerate(angulos, start=1):
            self.get_logger().info(f'Ejecutando angulo {indice}/{total}: {angulo}')

            for subpaso in range(subpasos_por_angulo):
                if goal_handle.is_cancel_requested:
                    goal_handle.canceled()
                    result = EjecutarTrayectoria.Result()
                    result.completado = False
                    result.tiempo_total = float(time.time() - start_time)
                    self.get_logger().warning('Goal cancelado por el cliente.')
                    return result

                time.sleep(0.1)
                progreso = ((indice - 1) + (subpaso + 1) / subpasos_por_angulo) * 100.0 / total
                feedback_msg.porcentaje_completitud = float(progreso)
                goal_handle.publish_feedback(feedback_msg)

        goal_handle.succeed()
        result = EjecutarTrayectoria.Result()
        result.completado = True
        result.tiempo_total = float(time.time() - start_time)
        self.get_logger().info('Trayectoria completada correctamente.')
        return result


def main(args=None):

    rclpy.init(args=args)
    node = TrayectoriaServer()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
