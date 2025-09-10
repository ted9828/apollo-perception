cmake_minimum_required(VERSION 3.8)
project(apollo_perception)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(
  PROGRAMS
    src/apollo_perception/nodes/demo_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()

