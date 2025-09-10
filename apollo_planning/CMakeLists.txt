cmake_minimum_required(VERSION 3.8)
project(apollo_planning)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(
  PROGRAMS
    src/apollo_planning/nodes/planner_node.py
    src/apollo_planning/nodes/controller_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
