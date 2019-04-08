echo "riddle.launch start"
gnome-terminal -x bash -c "rostopic pub /five_controller/command std_msgs/Float64 -- -0.5"
sleep 0.7
gnome-terminal -x bash -c "rostopic pub /one_controller/command std_msgs/Float64 -- -2.2"
sleep 0.7


