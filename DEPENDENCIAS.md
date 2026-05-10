# Dependencias

Sigue estos pasos en orden para que el workspace funcione:

1. Instala ROS 2 Humble.
2. Instala turtlesim si no lo tienes:

```bash
sudo apt-get install ros-humble-turtlesim
```

3. En la carpeta del workspace, compila todo:

```bash
colcon build
```

4. Carga el entorno de ROS 2:

```bash
source install/setup.bash
```

5. Antes de usar cualquier nodo, abre una terminal nueva y vuelve a ejecutar:

```bash
source install/setup.bash
```

Con eso ya puedes usar los comandos que están en [COMANDOS.md](COMANDOS.md).