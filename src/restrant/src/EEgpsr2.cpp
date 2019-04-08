/***********************************************************
Author: Zheng Haosi
Date: 4/6/2017
Abstract: Code for EEGPSR task in IranOpen(only navigation and tracking people)
************************************************************/
//标准头文件
#include<ros/ros.h>
#include<iostream>
#include<std_msgs/String.h>
#include<string.h>
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
using namespace std;

typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient; //简化类型书写为MoveBaseClient
bool estop_in=false;   //急停开关标志 低电平为输入，高电平为信号判断
bool sensorone_in=true;  //激光检测标志1 激光传感器有检测距离，必须离传感器一定远
bool sensortwo_in=true;   //激光检测标志2
bool go = false;
bool stop = false;

int step = -1;  //标志任务类型,0：到点等待命令；1：guide operator去语音发送的点；2：完成任务后返回命令点

geometry_msgs::Twist vel; //控制机器人速度
//定义会场中用到的19个点
geometry_msgs::Pose MyPose1;
geometry_msgs::Pose MyPose2;
geometry_msgs::Pose MyPose3;
geometry_msgs::Pose MyPose4;
geometry_msgs::Pose MyPose5;
geometry_msgs::Pose MyPose6;
geometry_msgs::Pose MyPose7;
geometry_msgs::Pose MyPose8;
geometry_msgs::Pose MyPose9;
geometry_msgs::Pose MyPose10;
geometry_msgs::Pose MyPose11;
geometry_msgs::Pose MyPose12;
geometry_msgs::Pose MyPose13;
geometry_msgs::Pose MyPose14;
geometry_msgs::Pose MyPose15;
geometry_msgs::Pose MyPose16;
geometry_msgs::Pose MyPose17;
geometry_msgs::Pose MyPose18;
geometry_msgs::Pose MyPose19;


void srclocationCallback(const std_msgs::String::ConstPtr& msg);
void followCallback(const std_msgs::String::ConstPtr& msg);
void DigitalInputEventCallback(const kobuki_msgs::DigitalInputEvent::ConstPtr& msg);

//定义的全局变量
std_msgs::String sound_flag; //语音控制标志
std_msgs::String srcloc;//place A 字符
std_msgs::String dstloc;//place B 字符

//ros::Publisher nav_pub;
ros::Publisher cmd_vel_pub;
ros::Publisher sound_pub;

ros::Subscriber button_sub;
ros::Subscriber follow_sub;

void srclocationCallback(const std_msgs::String::ConstPtr& msg)
{
        srcloc.data = msg->data;
        step=1;//进入到目标点的任务
}

void followCallback(const std_msgs::String::ConstPtr& msg)
{
        if(msg->data=="go_back")
             step=2;        
}
//主函数
int main(int argc, char** argv)
{
    ros::init(argc, argv, "navi_demo");
    ros::NodeHandle myNode;
    
    sound_pub= myNode.advertise<std_msgs::String>("Point", 1);
    cmd_vel_pub = myNode.advertise<geometry_msgs::Twist>("cmd_vel_mux/input/navi", 1); // 急停开关控制turltebot停止的一个话题

    ros::Subscriber button_sub = myNode.subscribe<kobuki_msgs::DigitalInputEvent>("/mobile_base/events/digital_input",1,DigitalInputEventCallback);
    ros::Subscriber srclocation_sub = myNode.subscribe("/gpsr_srclocation", 1, srclocationCallback);
     ros::Subscriber follow_sub = myNode.subscribe("/ifFollowme", 1, srclocationCallback);
     
    MoveBaseClient mc_("move_base", true); //建立导航客户端
    move_base_msgs::MoveBaseGoal naviGoal; //导航目标点
   
    geometry_msgs::Pose poseA;//临时变量
    //poseA.position.x = 0;
    //poseA.position.y = 0;
    //poseA.position.z = 0;
    //poseA.orientation.x = 0;
    //poseA.orientation.y = 0;
    //poseA.orientation.z =0.703364;
    //poseA.orientation.w = 0.710829 ;
    
    //等待命令的位置
    geometry_msgs::Pose dinning_pose;
    dinning_pose.position.x = 5.83722;
    dinning_pose.position.y = -1.55073;
    dinning_pose.position.z = 0;
    dinning_pose.orientation.x = 0;
    dinning_pose.orientation.y = 0;
    dinning_pose.orientation.z =0.703364;
    dinning_pose.orientation.w = 0.710829 ;
     
     //shelf
        MyPose1.position.x = 0.523831;
        MyPose1.position.y = 0.558826;
        MyPose1.position.z = 0;
        MyPose1.orientation.x = 0;
        MyPose1.orientation.y = 0;
        MyPose1.orientation.z =  0.628986;
        MyPose1.orientation.w = 0.777417;

        //dinner table
        MyPose2.position.x = 2.24752;
        MyPose2.position.y = -0.536046;
        MyPose2.position.z = 0;
        MyPose2.orientation.x = 0;
        MyPose2.orientation.y = 0;
        MyPose2.orientation.z = -0.141832;
        MyPose2.orientation.w = 0.989891;

        //dinning room table
        MyPose3.position.x = 6.21263;
        MyPose3.position.y = 0.628118;
        MyPose3.position.z = 0;
        MyPose3.orientation.x = 0;
        MyPose3.orientation.y = 0;
        MyPose3.orientation.z =0.214557;
        MyPose3.orientation.w = 0.976712;

         //side table
        MyPose4.position.x = 6.13722;
        MyPose4.position.y = -1.55073;
        MyPose4.position.z = 0;
        MyPose4.orientation.x = 0;
        MyPose4.orientation.y = 0;
        MyPose4.orientation.z =-0.0439635;
        MyPose4.orientation.w = 0.999033 ;
        
       //   counch table
        MyPose5.position.x = 5.22392;
        MyPose5.position.y = -3.30516;
        MyPose5.position.z = 0;
        MyPose5.orientation.x = 0;
        MyPose5.orientation.y = 0;
        MyPose5.orientation.z =-0.752561;
        MyPose5.orientation.w = 0.658522  ;
        //     dresser
        MyPose6.position.x = 6.26971;
        MyPose6.position.y = 1.83479;
        MyPose6.position.z = 0;
        MyPose6.orientation.x = 0;
        MyPose6.orientation.y = 0;
        MyPose6.orientation.z =-0.167432;
        MyPose6.orientation.w = 0.985884  ;
          //  side board
        MyPose7.position.x = 5.81939;
        MyPose7.position.y = 4.33161;
        MyPose7.position.z = 0;
        MyPose7.orientation.x = 0;
        MyPose7.orientation.y = 0;
        MyPose7.orientation.z =0.703364;
        MyPose7.orientation.w = 0.710829  ;
        // stove:
        MyPose8.position.x = 3.08759;
        MyPose8.position.y = 3.16413;
        MyPose8.position.z = 0;
        MyPose8.orientation.x = 0;
        MyPose8.orientation.y = 0;
        MyPose8.orientation.z =0.237777;
        MyPose8.orientation.w = 0.97132 ;
         // bar :
        MyPose9.position.x = 1.72632;
        MyPose9.position.y = 2.97096;
        MyPose9.position.z = 0;
        MyPose9.orientation.x = 0;
        MyPose9.orientation.y = 0;
        MyPose9.orientation.z =-0.996101;
        MyPose9.orientation.w = 0.0882175 ;
          // sink :
        MyPose10.position.x = 1.54032;
        MyPose10.position.y = 3.98642;
        MyPose10.position.z = 0;
        MyPose10.orientation.x = 0;
        MyPose10.orientation.y = 0;
        MyPose10.orientation.z =0.990209;
        MyPose10.orientation.w = 0.139596 ;
        //cabinet :
        MyPose11.position.x =2.14951;
        MyPose11.position.y = 4.33037;
        MyPose11.position.z = 0;
        MyPose11.orientation.x = 0;
        MyPose11.orientation.y = 0;
        MyPose11.orientation.z =0.725413;
        MyPose11.orientation.w = 0.688314 ;
        //fridge
        MyPose12.position.x =1.53218;
        MyPose12.position.y = 2.26124;
        MyPose12.position.z = 0;
        MyPose12.orientation.x = 0;
        MyPose12.orientation.y = 0;
        MyPose12.orientation.z =-0.99953;
        MyPose12.orientation.w = 0.0306685;
        //trash bin :

        MyPose13.position.x =2.40188;
        MyPose13.position.y = 0.353196;
        MyPose13.position.z = 0;
        MyPose13.orientation.x = 0;
        MyPose13.orientation.y = 0;
        MyPose13.orientation.z =0.835913;
        MyPose13.orientation.w = 0.548862 ;
        //hanger:

        MyPose14.position.x =0.906567;
        MyPose14.position.y = -4.49404;
        MyPose14.position.z = 0;
        MyPose14.orientation.x = 0;
        MyPose14.orientation.y = 0;
        MyPose14.orientation.z =-0.997616;
        MyPose14.orientation.w = 0.0690093 ;
        //sofa :

        MyPose15.position.x =1.47289;
        MyPose15.position.y = -4.70411;
        MyPose15.position.z = 0;
        MyPose15.orientation.x = 0;
        MyPose15.orientation.y = 0;
        MyPose15.orientation.z =-0.100604;
        MyPose15.orientation.w = 0.994927 ;
        //dinning room sofa :

        MyPose16.position.x =4.30371;
        MyPose16.position.y = -4.52156;
        MyPose16.position.z = 0;
        MyPose16.orientation.x = 0;
        MyPose16.orientation.y = 0;
        MyPose16.orientation.z =-0.113195;
        MyPose16.orientation.w = 0.993573 ;
        //tv :

        MyPose17.position.x =2.89199;
        MyPose17.position.y = -3.27996;
        MyPose17.position.z = 0;
        MyPose17.orientation.x = 0;
        MyPose17.orientation.y = 0;
        MyPose17.orientation.z =-0.731456;
        MyPose17.orientation.w = 0.688314 ;
        //bed :

        MyPose18.position.x =5.7917;
        MyPose18.position.y = 3.53758;
        MyPose18.position.z = 0;
        MyPose18.orientation.x = 0;
        MyPose18.orientation.y = 0;
        MyPose18.orientation.z =0.334706;
        MyPose18.orientation.w = 0.942322 ;
        //desk :

        MyPose19.position.x =4.67132;
        MyPose19.position.y = 4.52118;
        MyPose19.position.z = 0;
        MyPose19.orientation.x = 0;
        MyPose19.orientation.y = 0;
        MyPose19.orientation.z =0.793916;
        MyPose19.orientation.w = 0.608028;
        
   
		      	      
    while(ros::ok())
    {
        if(go == true && stop == false)
        {
                cout<<"The categary type is: "<<step<<endl;
                cout<<"srcloc:"<<srcloc.data;
                if ( srcloc.data == "shelf")
                {
		             poseA=MyPose1;}
	            if ( srcloc.data == "dinner_table")
	            {
		             poseA=MyPose2;	}   
	            if ( srcloc.data == "dinning_table")
	            {
		             poseA=MyPose3;}
                if ( srcloc.data == "side_table")
                {
		             poseA=MyPose4;	}
                if ( srcloc.data == "counch_table")
                {
		             poseA=MyPose5;  }
                if ( srcloc.data == "dresser")
                {
		             poseA=MyPose6; }    
                if ( srcloc.data == "side_board")
                {
		             poseA=MyPose7;	}      
                if ( srcloc.data == "stove")
                {
		             poseA=MyPose8;}
                if ( srcloc.data == "bar")
                {
		             poseA=MyPose9;}      
                if ( srcloc.data == "sink")
                {
		             poseA=MyPose10;}	
                if ( srcloc.data == "cabinent")
                {
		             poseA=MyPose11;}
                if ( srcloc.data == "fridge")
                {
		             poseA=MyPose12;}
                if ( srcloc.data == "trash_bin")
                {
		             poseA=MyPose13;}	      
                if ( srcloc.data == "hanger")
                {
		             poseA=MyPose14;}	
                if ( srcloc.data == "sofa")
                {
		             poseA=MyPose15;}	 
                if ( srcloc.data == "dinning_room_sofa")
                {
		             poseA=MyPose16;}	 
                if ( srcloc.data == "tv")
                {
		             poseA=MyPose17;}	      
                if ( srcloc.data == "ded")
                {
		             poseA=MyPose18;}	
                if ( srcloc.data == "desk")
                {
		             poseA=MyPose19;	 }
                if ( srcloc.data == "living_room")
               {
		             poseA=MyPose15;	 }
	           if ( srcloc.data == "dinning_room")
	           {
		             poseA=dinning_pose;	}      
               if ( srcloc.data == "dedroom")
               {
		             poseA=MyPose19;	}
               if ( srcloc.data == "hallway")
              {
		             poseA=MyPose2;	 }
               if ( srcloc.data == "kitchen")
              {
		             poseA=MyPose11;}
    if(step == 0)
                {
		    cout<<"Moving ...."<<endl;
                    sound_flag.data = "A";      
                    sound_pub.publish(sound_flag);//出发，发送一个“A”消息给语音,"I'm moving now"
                    
		    naviGoal.target_pose.header.frame_id = "map"; 
                    naviGoal.target_pose.header.stamp = ros::Time::now();
                    naviGoal.target_pose.pose = geometry_msgs::Pose(dinning_pose);
                    
                    mc_.sendGoal(naviGoal);
                    mc_.waitForResult(ros::Duration(10.0));
                    //导航反馈直至到达目标点
                    if(mc_.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
                    {                        
                        cout<<"Yes! The robot has moved to the designated position!"<<endl;
                        sound_flag.data = "B";      
                        sound_pub.publish(sound_flag);//I have arrived the designated position!Waiting for your command.
                        //break;
				     }
				 }
				 
                if(step == 1)
                {
                    sound_flag.data=="c";
                    sound_pub.publish(sound_flag);//Please follow me,I will guide you
                    naviGoal.target_pose.header.frame_id = "map"; 
                    naviGoal.target_pose.header.stamp = ros::Time::now();
                    naviGoal.target_pose.pose = geometry_msgs::Pose(poseA);
                    //guide 到 poseA
                    while(!mc_.waitForServer(ros::Duration(5.0)))
                    { 
                        cout<<"Waiting for the server..."<<endl;
                    }
                    mc_.sendGoal(naviGoal);
                    mc_.waitForResult(ros::Duration(10.0));
                    //导航反馈直至到达目标点
                    
                    if(mc_.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
                    {                        
                        cout<<"Yes! The robot has guided you to the goal!"<<endl;
                        
                        sound_pub.publish(srcloc);//到达poseA，发送一个“srcloc”消息给语音
                        step =2;
                    }

                 }
               
                 else if(step == 2)
                 {    
                    cout<<"Returning ... "<<endl; 
                    sleep(20);
                    naviGoal.target_pose.header.frame_id = "map"; 
                    naviGoal.target_pose.header.stamp = ros::Time::now();
                    naviGoal.target_pose.pose = geometry_msgs::Pose(dinning_pose); 
                    mc_.sendGoal(naviGoal);
                    mc_.waitForResult(ros::Duration(10.0));
                        
                    if(mc_.getState() == actionlib::SimpleClientGoalState::SUCCEEDED){
                  	         cout<<"Yes! The robot has gone back!"<<endl;
                  	         sound_flag.data = "back";
                                 sound_pub.publish(sound_flag);//I am back,waiting for your next command
                             
                        }
                     
                     }
                  
			  }                 
         
        
        ros::spinOnce();
    }
    return 0;
}

// 激光和急停开关回调函数
void DigitalInputEventCallback(const kobuki_msgs::DigitalInputEvent::ConstPtr& msg)
{
   estop_in = msg->values[2];
   sensorone_in = msg->values[0];
   sensortwo_in = msg->values[1];
   cout<<"I have heared that ...... "<<endl;
   if(estop_in == true)
   {
        stop = true;
        cout<<"I have heared that the EmergencyButton has been pressed ...."<<endl;
        MoveBaseClient mc_("move_base", true); //建立导航客户端
        mc_.cancelAllGoals();//取消所有导航目标
        vel.linear.x = 0; //设定x方向速度为零
        vel.linear.y = 0; //设定y方向速度为零
        cmd_vel_pub.publish(vel); //让机器人暂停
        
   }
   else
   {
        stop = false;
        cout<<"I have heared that the EmergencyButton has been released ...."<<endl;
   }   
   if(sensorone_in == false&& sensortwo_in==false)
   {
        //go = true;
        //step=0;
        cout<<"I have heared that the door is open "<<endl;
    }
};
