from setuptools import find_packages, setup

package_name = 'brazo_control'

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
    description='Python service server for the MoverBrazo interface.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'mover_brazo_server = brazo_control.server:main',
            'mover_brazo_client = brazo_control.client:main',
        ],
    },
)
