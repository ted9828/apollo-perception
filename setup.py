from setuptools import setup

package_name = 'apollo_perception'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, f'{package_name}.nodes'],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        (f'share/{package_name}', ['package.xml']),
        (f'share/{package_name}/launch', ['launch/demo.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='APOLLO',
    maintainer_email='hknuapollo@gmail.com',
    description='APOLLO Perception skeleton',
    license='Proprietary',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo_node = apollo_perception.nodes.demo_node:main',
        ],
    },
)

