cmake_minimum_required(VERSION 3.18)
project(aero_gnc LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(PYBIND11_FINDPYTHON ON)

include(FetchContent)
FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11.git
        GIT_TAG v2.13.6
)
FetchContent_MakeAvailable(pybind11)

pybind11_add_module(gnc src/PID.cpp src/bindings.cpp)

target_include_directories(gnc PRIVATE include)

if(MINGW)
    target_link_libraries(gnc PRIVATE -static)
endif()

set_target_properties(gnc PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/scripts"
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/scripts"
)