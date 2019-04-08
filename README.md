Introduction
========
This project is for 2017 Asia-Pacific RoboCup competition. It includes turtlbot navigation, image recognition and speech functions. The competition contains three tasks which need the combination funcions mentioned above.  
Following are the introduction of each task:

Help Me Carry
--------
The flow of the task:  
First, robot is asked to follow person A out of the room where park a car. When it reach the point, person A will delivery a bag to robot and robot should reach out its arm to take over the bag. Then person A will speak out randomly a room name(ex:livingroom). Robot should recognize the room name and navigation to that room percisely. Then robot should find person B in that room by image recognition and move close to person B. When it arrival in front of person B, it should talk to him and guide him to the car position.  
* Specific tasks that robot should finish:
  * mapping the whole room
  * navigation Point-to-Point
  * interact with human through speech
  * image recognition, includes person recognition
  * real time mapping in unknown area while following the person, and remember a specific location in unknown place 

SPR
--------
The flow of the task:
The robot is surrounded by 5 persons. These 5 persons are located at different directions to the robot. One of these person is choosen randomly to ask robot a question. Then robot should first recognize which person is speaking and turn towards him. And next, it should answer the question according to the question. This will go 5 rounds. Then these persons will stand in a line at some location in the room and ask the robot to take a photo for them. The robot should first find out where they stand by and turn towards them. Then it take a photo of them and speak out how many people in the photo and how many males and females in the photo.
* Specific tasks that robot should finish:
  * ineract with human through speech including understanding the meaning of the conversation and respond to them
  * face recognition and sex recognition

Restaurant
--------
The flow of the task:
First robot is settled nearby a bar, and robot should tell the bar is on its right or left. Then one of the persons in the restaurant begin to waving his hands to call the robot, and robot should recognize him and move towards him. When it moves in front of the person, a conversation begins which maily about which food the person want to order. Then robot should go back to the bar and fetch the wanted food for the person.
* Specific tasks that robot should finish:
  * image recognition 
  * mapping in an unknown area
  * moving detection and object recognition
  * speech interaction with human beings
  * arm controls
  * complex navigation
  
