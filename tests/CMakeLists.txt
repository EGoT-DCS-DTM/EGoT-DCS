add_executable(all-tests main.cpp simple-test.cpp)
target_link_libraries(all-tests gtest gmock gtest_main)
add_test(all-tests all-tests)
