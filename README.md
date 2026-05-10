# Robotica ROS 2

## Preparación

```bash
colcon build
source install/setup.bash
```

## 1) servicio_suma

Terminal 1:

```bash
source install/setup.bash
ros2 run servicio_suma add_server
```

Terminal 2:

```bash
source install/setup.bash
ros2 run servicio_suma add_client 5 10
```

Resultado esperado:

```text
Respuesta: sum=15
```

## 2) brazo_control

Terminal 1:

```bash
source install/setup.bash
ros2 run brazo_control mover_brazo_server
```

Terminal 2:

```bash
source install/setup.bash
ros2 run brazo_control mover_brazo_client 30 -45 90
```

Resultado esperado:

```text
Respuesta: exito=True, estado="Brazo movido a θ1=30.00°, θ2=-45.00°, θ3=90.00°"
```

## 3) trayectoria_control

Terminal 1:

```bash
source install/setup.bash
ros2 run trayectoria_control trajectory_server
```

Terminal 2:

```bash
source install/setup.bash
ros2 run trayectoria_control trajectory_client
```

Resultado esperado:

```text
Feedback progresivo (2.5%, 5.0%, ...)
Solicitud de cancelación cuando supera 60%
Resultado final: completado=False, tiempo_total=...
```

## 4) py_pubsub

Terminal 1:

```bash
source install/setup.bash
ros2 run py_pubsub listener_vel
```

Terminal 2:

```bash
source install/setup.bash
ros2 run py_pubsub talker_vel
```

Resultado esperado:

```text
Listener imprime lineal=(0.50, 0.00, 0.00) angular=(0.00, 0.00, 0.10)
Talker publica a 10 Hz y se detiene solo a los 5 s
```

## 5) mi_test

Terminal 1:

```bash
ros2 run turtlesim turtlesim_node
```

Terminal 2:

```bash
source install/setup.bash
ros2 run mi_test move_turtle
```

Otros comandos:

```bash
source install/setup.bash
ros2 run mi_test spawn_turtles
ros2 run mi_test draw_square
ros2 run mi_test draw_circle
```

Resultado esperado:

```text
La tortuga se mueve y/o dibuja en la ventana de turtlesim según el nodo ejecutado.
```