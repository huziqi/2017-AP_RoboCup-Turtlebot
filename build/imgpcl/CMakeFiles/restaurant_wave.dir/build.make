# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kamerider/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kamerider/catkin_ws/build

# Include any dependencies generated for this target.
include imgpcl/CMakeFiles/restaurant_wave.dir/depend.make

# Include the progress variables for this target.
include imgpcl/CMakeFiles/restaurant_wave.dir/progress.make

# Include the compile flags for this target's objects.
include imgpcl/CMakeFiles/restaurant_wave.dir/flags.make

imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o: imgpcl/CMakeFiles/restaurant_wave.dir/flags.make
imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o: /home/kamerider/catkin_ws/src/imgpcl/src/restaurant_wave.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/kamerider/catkin_ws/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o"
	cd /home/kamerider/catkin_ws/build/imgpcl && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o -c /home/kamerider/catkin_ws/src/imgpcl/src/restaurant_wave.cpp

imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.i"
	cd /home/kamerider/catkin_ws/build/imgpcl && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/kamerider/catkin_ws/src/imgpcl/src/restaurant_wave.cpp > CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.i

imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.s"
	cd /home/kamerider/catkin_ws/build/imgpcl && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/kamerider/catkin_ws/src/imgpcl/src/restaurant_wave.cpp -o CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.s

imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o.requires:
.PHONY : imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o.requires

imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o.provides: imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o.requires
	$(MAKE) -f imgpcl/CMakeFiles/restaurant_wave.dir/build.make imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o.provides.build
.PHONY : imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o.provides

imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o.provides.build: imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o

# Object files for target restaurant_wave
restaurant_wave_OBJECTS = \
"CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o"

# External object files for target restaurant_wave
restaurant_wave_EXTERNAL_OBJECTS =

/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: imgpcl/CMakeFiles/restaurant_wave.dir/build.make
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libcv_bridge.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libimage_transport.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libpcl_ros_filters.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libpcl_ros_io.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libpcl_ros_tf.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_common.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_octree.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_io.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_kdtree.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_search.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_sample_consensus.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_filters.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_features.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_keypoints.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_segmentation.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_visualization.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_outofcore.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_registration.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_recognition.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_surface.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_people.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_tracking.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libpcl_apps.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_iostreams.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_serialization.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libqhull.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libOpenNI.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libflann_cpp_s.a
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libvtkCommon.so.5.8.0
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libvtkRendering.so.5.8.0
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libvtkHybrid.so.5.8.0
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libvtkCharts.so.5.8.0
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libdynamic_reconfigure_config_init_mutex.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libnodeletlib.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libbondcpp.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libuuid.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libclass_loader.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/libPocoFoundation.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libdl.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libroslib.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/librospack.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libpython2.7.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libtinyxml.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/librosbag.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/librosbag_storage.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libroslz4.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/liblz4.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libtopic_tools.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libtf.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libtf2_ros.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libactionlib.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libmessage_filters.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libtf2.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libroscpp.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/librosconsole.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/librosconsole_log4cxx.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/librosconsole_backend_interface.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/liblog4cxx.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libxmlrpcpp.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libroscpp_serialization.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/librostime.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /opt/ros/indigo/lib/libcpp_common.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave: imgpcl/CMakeFiles/restaurant_wave.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave"
	cd /home/kamerider/catkin_ws/build/imgpcl && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/restaurant_wave.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
imgpcl/CMakeFiles/restaurant_wave.dir/build: /home/kamerider/catkin_ws/devel/lib/imgpcl/restaurant_wave
.PHONY : imgpcl/CMakeFiles/restaurant_wave.dir/build

imgpcl/CMakeFiles/restaurant_wave.dir/requires: imgpcl/CMakeFiles/restaurant_wave.dir/src/restaurant_wave.cpp.o.requires
.PHONY : imgpcl/CMakeFiles/restaurant_wave.dir/requires

imgpcl/CMakeFiles/restaurant_wave.dir/clean:
	cd /home/kamerider/catkin_ws/build/imgpcl && $(CMAKE_COMMAND) -P CMakeFiles/restaurant_wave.dir/cmake_clean.cmake
.PHONY : imgpcl/CMakeFiles/restaurant_wave.dir/clean

imgpcl/CMakeFiles/restaurant_wave.dir/depend:
	cd /home/kamerider/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kamerider/catkin_ws/src /home/kamerider/catkin_ws/src/imgpcl /home/kamerider/catkin_ws/build /home/kamerider/catkin_ws/build/imgpcl /home/kamerider/catkin_ws/build/imgpcl/CMakeFiles/restaurant_wave.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : imgpcl/CMakeFiles/restaurant_wave.dir/depend

