# Comandos de Prueba

Antes de probar cualquier ejercicio:

```bash
colcon build
source install/setup.bash
```

## 1. py_pubsub

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

## 2. brazo_control

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

## 3. trayectoria_control

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
