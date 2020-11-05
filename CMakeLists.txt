#
# https://cliutils.gitlab.io/modern-cmake/
#
# Almost all CMake files should start with this
# You should always specify a range with the newest
# and oldest tested versions of CMake. This will ensure
# you pick up the best policies.
cmake_minimum_required(VERSION 3.11...3.19)

# MACRO to allow 3.14+ syntax
if(${CMAKE_VERSION} VERSION_LESS 3.14)
    macro(FetchContent_MakeAvailable NAME)
        FetchContent_GetProperties(${NAME})
        if(NOT ${NAME}_POPULATED)
            FetchContent_Populate(${NAME})
            add_subdirectory(${${NAME}_SOURCE_DIR} ${${NAME}_BINARY_DIR})
        endif()
    endmacro()
endif()

# This is your project statement. You should always list languages;
# Listing the version is nice here since it sets lots of useful variables
project(
  ModernCMakeExample
  VERSION 1.0
  LANGUAGES CXX)
include(FetchContent)

# If you set any CMAKE_ variables, that can go here.
# (But usually don't do this, except maybe for C++ standard)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
enable_testing() # Must be in main file

# Find packages go here.
find_package(Boost REQUIRED regex filesystem)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        master
)

# CMake 3.14+
FetchContent_MakeAvailable(googletest)

# You should usually split this into folders, but this is a simple example

# This is a "default" library, and will match the *** variable setting.
# Other common choices are STATIC, SHARED, and MODULE
# Including header files here helps IDEs but is not required.
# Output libname matches target name, with the usual extensions on your system
# add_library(MyLibExample simple_lib.cpp simple_lib.hpp)

# Link each target with other targets or add options, etc.

# The executable code is here
add_subdirectory(src)
add_subdirectory(tests)
