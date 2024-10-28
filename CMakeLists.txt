cmake_minimum_required(VERSION 3.25.1)
project(Assignment3)

# Required Python Executable.
find_package(Python3 REQUIRED)

# Argument Execution.
add_custom_command(
  OUTPUT assignment3
  COMMAND ${CMAKE_COMMAND} -E create_symlink
          ${CMAKE_CURRENT_SOURCE_DIR}/Project/assignment3.py
          ${CMAKE_CURRENT_BINARY_DIR}/assignment3
  DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/Project/assignment3.py
)

# Custom target to ensure the symlink is created.
add_custom_target(make_symlink ALL DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/assignment3)

# Custom target to run script.
add_custom_target(run
  COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/assignment3 -l 12345 -p "happy"
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/Project
  COMMENT "Running assignment3.py with arguments"
)

# Add the symlink target
add_custom_target(make_symlink ALL DEPENDS assignment3)