from setuptools import find_packages, setup

package_name = 'trayectoria_control'

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
    description='Action server and client for trajectory execution.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'trajectory_server = trayectoria_control.server:main',
            'trajectory_client = trayectoria_control.client:main',
        ],
    },
)
