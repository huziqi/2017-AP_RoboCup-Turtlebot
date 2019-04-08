//标准头文件
#include<ros/ros.h>
#include<iostream>
#include<std_msgs/String.h>
#include<string.h>
//navigation中需要使用的位姿信息头文件
#include<geometry_msgs/Pose.h>
#include<geometry_msgs/Point.h>
#include<geometry_msgs/PoseWithCovariance.h>
#include<geometry_msgs/PoseWithCovarianceStamped.h>
#include<geometry_msgs/Twist.h>
#include<geometry_msgs/Quaternion.h>
#include <kobuki_msgs/DigitalInputEvent.h>
#include <kobuki_msgs/ButtonEvent.h>
//move_base头文件
#include<move_base_msgs/MoveBaseGoal.h>
#include<move_base_msgs/MoveBaseAction.h>
//actionlib头文件
#include<actionlib/client/simple_action_client.h>
#include <stdlib.h>
#include<cstdlib>
using namespace std;
//定义的全局变量
typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient; //简化类型书写为MoveBaseClient
int step=0;

//定义不同房间位置的坐标点
geometry_msgs::Pose ViewPoint;
geometry_msgs::Pose OutPoint;

ros::Publisher nav2speech_pub;
ros::Subscriber move_sub;
ros::Subscriber speech_sub;
ros::Publisher nav_inspect;
bool switch_state=0;
void moveCallback(const std_msgs::String::ConstPtr& msg)
{
  if(msg->data == "opened")
  {
	   step = 1;
	   cout<<"opened"<<endl;
	}
}
void speechCallback(const std_msgs::String::ConstPtr& msg)
{
  if(msg->data == "go_out")
  {
	   step = 2;
	   cout<<"go_out"<<endl;
	}
	if(msg->data == "false"）
｛
	switch_state=true;
｝
}
//主函数
int main(int argc, char** argv)
{
	//set pose
	//people
	ViewPoint.position.x = -2.67234942455;//0.860085680301;
	ViewPoint.position.y = -5.16863730594;//-2.83426480702;
	ViewPoint.position.z = 0;
	ViewPoint.orientation.x = 0;
	ViewPoint.orientation.y = 0;
	ViewPoint.orientation.z = -0.0587035979362;//0.097098622328;
	ViewPoint.orientation.w = 0.99827545677;//0.995274764847;

	//living_room
	OutPoint.position.x = 5.72396173042;
	OutPoint.position.y = -7.99834111498;
	OutPoint.position.z = 0;
	OutPoint.orientation.x = 0;
	OutPoint.orientation.y = 0;
	OutPoint.orientation.z = -0.652757540095;
	OutPoint.orientation.w = 0.757566890677;
	ros::init(argc, argv, "navi_demo");
	ros::NodeHandle myNode;
	cout<<"Welcome to Help-me-carry!"<<endl;

	nav2speech_pub= myNode.advertise<std_msgs::String>("nav2speech", 1);
	nav_inspect= myNode.advertise<std_msgs::String>("inspect2speech", 1);

	//ros::Subscriber move_sub = myNode.subscribe("/doorstate", 1, moveCallback);
	ros::Subscriber speech_sub = myNode.subscribe("go_out", 1, speechCallback);

	MoveBaseClient  mc_("move_base", true); //建立导航客户端
	move_base_msgs::MoveBaseGoal naviGoal; //导航目标点
	while(ros::ok())
	{
		if(step==0&&switch_state==true)
		{
			naviGoal.target_pose.header.frame_id = "map";
			naviGoal.target_pose.header.stamp = ros::Time::now();
			naviGoal.target_pose.pose = geometry_msgs::Pose(ViewPoint);

			while(!mc_.waitForServer(ros::Duration(5.0)))
			{
				//等待服务初始化
				cout<<"Waiting for the server..."<<endl;

			}
			mc_.sendGoal(naviGoal);
			mc_.waitForResult(ros::Duration(40.0));

			if(mc_.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
			{
				cout<<"I have reach viewpoint"<<endl;
				std_msgs::String str;
				str.data = "get_pose";
				nav_inspect.publish(str);
			}
			else
			{
				cout<<"I have reach viewpoint nearby"<<endl;
				std_msgs::String str;
				str.data = "nav2speech";
				nav2speech_pub.publish(str);
			}
			step = 0;
		}
		if(step==2)
		{
			naviGoal.target_pose.header.frame_id = "map";
			naviGoal.target_pose.header.stamp = ros::Time::now();
			naviGoal.target_pose.pose = geometry_msgs::Pose(OutPoint);

			while(!mc_.waitForServer(ros::Duration(5.0)))
			{
				//等待服务初始化
				cout<<"Waiting for the server..."<<endl;
			}
			mc_.sendGoal(naviGoal);
			mc_.waitForResult(ros::Duration(40.0));

			//导航反馈直至到达目标点
			if(mc_.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
			{
				cout<<"Yes! The robot has moved to another door!"<<endl;
			}
			step = 0;
		}
		ros::spinOnce();
	}
	return 0;
}
