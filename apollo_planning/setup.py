from setuptools import setup

package_name = 'apollo_planning'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, f'{package_name}.nodes'],
    package_dir={'': 'src'},
    data_files=[
        (f'share/{package_name}', ['package.xml']),
        (f'share/{package_name}/launch', ['launch/plan_control.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='APOLLO',
    maintainer_email='hknuapollo@gmail.com',
    description='APOLLO Planning & Control skeleton',
    license='Proprietary',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'planner_node = apollo_planning.nodes.planner_node:main',
            'controller_node = apollo_planning.nodes.controller_node:main',
        ],
    },
)
