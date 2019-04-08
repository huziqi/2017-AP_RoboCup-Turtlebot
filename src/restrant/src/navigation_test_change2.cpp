/***********************************************************
Author: Zheng Haosi
Date: 3/14/2017
Abstract: Code for navigation task in both Education and OP.
************************************************************/
//标准头文件
#include<ros/ros.h>
#include<iostream>
#include<std_msgs/String.h>
//navigation中需要使用的位姿信息头文件
#include<geometry_msgs/Pose.h>
#include<geometry_msgs/Point.h>
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
int system(const char *string); 

bool go = true;
bool stop = false;
int step=0;
bool Isgrasp=false;
geometry_msgs::Twist vel; //控制机器人速度

using namespace std;
typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient; //简化类型书写为MoveBaseClient

//定义的全局变量
std_msgs::String sound_flag; //语音控制标志
//创建一个话题发布到达消息给语音
ros::Publisher sound_pub;
//创建一个话题发布消息给图像
ros::Publisher nav_pub2;
//订阅完成抓取的话题使之移向下一点
ros::Subscriber arm_sub;
//订阅开始的语音话题
ros::Subscriber start_sub;

void ArmNavCallback(const std_msgs::String::ConstPtr& msg);//为订阅完成抓取动作的Arm2Nav回调函数
void GpsrStartCallback(const std_msgs::String::ConstPtr& msg);//获取语音开始命令的回调函数

void GpsrStartCallback(const std_msgs::String::ConstPtr& msg)
{
    if(msg->data == "start")
    {
		step=1;
	}
}

void ArmNavCallback(const std_msgs::String::ConstPtr& msg)
{
    if(msg->data == "objectDone")
    {
		Isgrasp=true;
	}
}

void followcallback(const std_msgs::String::ConstPtr& msg)
{
    if(msg->data == "follow_me")
    {
        system("/home/huziqi/2017_ws/src/navigation_test/follow_start.sh");
	 }
}

//主函数
int main(int argc, char** argv)
{
    ros::init(argc, argv, "navi_demo");
    ros::NodeHandle n;
    sound_pub=n.advertise<std_msgs::String>("nav_output", 1);
    nav_pub2 = n.advertise<std_msgs::String>("nav2image", 1);
    arm_sub = n.subscribe("/img2nav", 1, ArmNavCallback);
    start_sub = n.subscribe("/gpsr_begin", 1, GpsrStartCallback);
    ros::Subscriber sound_sub = n.subscribe("fromFollowMe", 1, followcallback);
    
    MoveBaseClient mc_("move_base", true); //建立导航客户端
    move_base_msgs::MoveBaseGoal naviGoal; //导航目标点
    
    geometry_msgs::Pose pose1; //路点1
    pose1.position.x = 7.98111;
    pose1.position.y = 2.63526;
    pose1.position.z = 0.000000;
    pose1.orientation.x = 0.000000;
    pose1.orientation.y = 0.000000;
    pose1.orientation.z = 0.757632;
    pose1.orientation.w = 0.652682;

    geometry_msgs::Pose pose2; //路点2
    pose2.position.x = 4.80171;
    pose2.position.y = 2.72721;
    pose2.position.z = 0.000000;
    pose2.orientation.x = 0.000000;
    pose2.orientation.y = 0.000000;
    pose2.orientation.z = 0.757632;
    pose2.orientation.w = 0.652682;
    
    geometry_msgs::Pose pose3; //路点3
    pose3.position.x = 2.39571;
    pose3.position.y = 0.681905;
    pose3.position.z = 0.000000;
    pose3.orientation.x = 0.000000;
    pose3.orientation.y = 0.000000;
    pose3.orientation.z = -0.999726;
    pose3.orientation.w = 0.0234087; 
    

    while(ros::ok())
    {
        if(go == true && stop == false)
        {
                
                if(step == 1)
                {
                    cout<<"Waypoint 1...."<<endl;
                   
                    naviGoal.target_pose.header.frame_id = "map"; 
                    naviGoal.target_pose.header.stamp = ros::Time::now();
                    naviGoal.target_pose.pose = geometry_msgs::Pose(pose1);
                    //导航到waypoint 1
                    while(!mc_.waitForServer(ros::Duration(5.0)))
                    { //等待服务初始化
                        cout<<"Waiting for the server..."<<endl;
                    }
                    mc_.sendGoal(naviGoal);
                    mc_.waitForResult(ros::Duration(10.0));
                    //导航反馈直至到达目标点
                    
                    if(mc_.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
                    {                        
                        cout<<"Yes! The robot has moved to the A point!"<<endl;
                        step=2;
                        //向图像发布抓取的消息给图像部分
	                    std_msgs::String send;
	                    send.data = "grasp";
	                    nav_pub2.publish(send);
                        cout<<"I have sent the signal to image!"<<endl;
                    }

                    
                 }
                
               else if(( step == 2 ) && ( Isgrasp ==true ) )
               {    
                    cout<<"Waypoint 2 ... "<<endl; 
                    naviGoal.target_pose.header.frame_id = "map"; 
                    naviGoal.target_pose.header.stamp = ros::Time::now();
                    naviGoal.target_pose.pose = geometry_msgs::Pose(pose2);
                    
                    mc_.sendGoal(naviGoal);
                    mc_.waitForResult(ros::Duration(10.0));
            
                     if(mc_.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
                     {
                  	     cout<<"Yes! The robot has moved to the B point!"<<endl;
                  	     sound_flag.data="arrive";
                         sound_pub.publish(sound_flag);
                         cout<<"I have sent the signal to sound!"<<endl;
                         
                
                      }
                      else
                           cout<<"Sorry, I failed!"<<endl;
                    
              	}
                 
        
    	}
     ros::spinOnce();
   }
   return 0;
}
