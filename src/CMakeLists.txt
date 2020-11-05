add_executable(app main.cpp)
target_link_libraries(app PRIVATE Boost::regex Boost::filesystem)
