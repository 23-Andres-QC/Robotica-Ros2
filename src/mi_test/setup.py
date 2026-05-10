from setuptools import find_packages, setup

package_name = 'mi_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andresqc',
    maintainer_email='andresqc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'move_turtle = mi_test.move_turtle:main',
            'spawn_turtles = mi_test.spawn_turtles:main',
            'draw_square = mi_test.draw_square:main',
            'draw_circle = mi_test.draw_circle:main',
        ],
    },
)
