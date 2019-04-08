#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    play riddle game
"""

import roslib; roslib.load_manifest('speech')
import rospy
import re
import os
from std_msgs.msg import String
from std_msgs.msg import Int8
import time
from sound_play.libsoundplay import SoundClient
import xml.etree.ElementTree as ET

class spr:
	def __init__(self):

		rospy.on_shutdown(self.cleanup)
		self.voice = rospy.get_param("~voice", "voice_cmu_us_rms_cg_clunits")
		self.question_start_signal = rospy.get_param("~question_start_signal", "")



		self.if_say=0
		#for crowd question
		self.appl=['children','adults','elders']
		self.gppl=['females','males','women','men','boys','girls']
		self.people=self.appl+self.gppl
		self.posprs=['standing','sitting','lying']
		self.posppl=['standing','sitting','lying','standing or sitting','standing or lying','sitting or lying']
		self.gesture=['waving','rising left arm','rising right arm','pointing left','pointing right']
		self.gprsng=['male or female','man or woman','boy or girl']
		self.gprsn=['female','male','woman','man','boy','girl']
		self.w=0



		#for object question
		#read object.xml
		self.adja=['heaviest','smallest','biggest','lightest']
		self.adjr=['heavier','smaller','bigger','lighter']
		self.size_order = (
			'mixed-nuts', 'food', 'fork', 'cutlery', 'spoon', 'cutlery',
			'knife', 'cutlery','canned-fish', 'food', 'cup', 'container', 
			'orange-juice', 'drink', 'pringles', 'snack', 'cereal', 'food', 
			'apple-juice', 'drink','milk-tea', 'drink','jelly', 'snack', 
			'milk-biscuit', 'snack', 'root-beer', 'drink', 'potato-chip', 'snack',
			'instant-noodle', 'food', 'green-tea', 'drink','disk','container',
			'cereal-bowl','container','tray','container','shopping-bag','container')
		self.weight_order1= (
            'cup','container',               'cereal-bowl','container',
            'disk','container',           'tray','container',
	    'mixed nuts','food',
	    'potato-chip', 'snack',    'shopping-bag','container',
            'cereal','food',          'instant-noodle','food',
            'milk-biscuit', 'snack',          'pringles','snack',
            'fork', 'cutlery',          'spoon', 'cutlery',
            'knife','cutlery',         'canned-fish','food',
            'apple-juice','drink',   'orange-juice', 'drink',
            'milk-tea', 'drink',          'root-bear','drink',
            'jelly', 'snack',    'green-tea', 'drink')		


		self.weight_order= (
            'cup','the top of the shelf',               'cereal-bowl','the top of the shelf',
            'disk','the top of the shelf',           'tray','the top of the shelf',
	    'mixed nuts','kitchen-table',
	    'potato-chip', 'coffee-table',    'shopping-bag','the top of the shelf',
            'cereal','kitchen-table',          'instant-noodle','kitchen-table',
            'milk-biscuit', 'coffee-table',          'pringles','coffee-table',
            'fork', 'the top of the shelf',          'spoon', 'the top of the shelf',
            'knife','the top of the shelf',         'canned-fish','kitchen-table',
            'apple-juice','bar-table',   'orange-juice', 'bar-table',
            'milk-tea', 'bar-table',          'root-bear','bar-table',
            'jelly', 'coffee-table',    'green-tea', 'bar-table','cutlery','the top of the shelf', 'container','the top of the shelf','food','kitchen-table','snack','bar-table','drink','bar-table')
		self.category = ('container', '5', 'cutlery', '3', 'drink', '5', 'food', '4', 'snack', '4')
		

		self.object_colour = ( 'cup','green red and orange',               'cereal-bowl','red',
		'mixed-nuts','white',
            'disk','blue',         'tray','purple',
	    'potato-chip', 'yellow',    'shopping-bag','red and white',
            'cereal','red and blue',          'instant-noodle','yellow',
            'milk-biscuit', 'blue and red',          'pringles','green and red',
            'fork', 'silver',          'spoon', 'silver',
            'knife','silver',         'canned-fish','red and white',
            'apple-juice','red',   'orange-juice', 'white and greed',
            'milk-tea', 'blue and black',          'root-bear','brown',
            'jelly', 'red and pink',    'green-tea', 'greed')
		









		self.location=('small shelf','living-room','sofa','living-room','coffee-table','living-room',
					   'arm-chair-a','living-room','arm-chair-b','living-room','kitchen-rack','kitchen','kitchen-table','kitchen',
					   'kitchen shelf','kitchen','kitchen-counter','kitchen','fridge','kitchen',
					   'chair','dining-room','dining-table-a','dining-room','little table','dining-room',
					   'right planks','balcony','balcony-shelf','balcony','entrance-shelf','entrance',
					   'bar-table','dining-room','dining-table-b','dining-room','shelf','dining-room')
		self.doornum=('living-room','2','kitchen','1','dining-room','1','hallway','1')
		self.thingnum=('2','arm-chair','living-room','6','chair','dining-room','2','dining-table','dining-room',
				'1','kitchen tack','kitchen','1','kitchen-table','kitchen',
				'1','small shelf','living-room','1','sofa','living-room','1','coffee-table','living-room',
				'1','little table','dining-room','1','bar-table','dining-room','1','shelf','dining-room')


		# Create the sound client object
		self.soundhandle = SoundClient() 
		rospy.sleep(1)
		self.riddle_turn = rospy.Publisher('turn_signal', String, queue_size=15)
		self.soundhandle.stopAll()
		self.soundhandle.say('hello I want to play riddles',self.voice)
		rospy.sleep(3)
		self.soundhandle.say('I will turn back after ten seconds',self.voice)
		rospy.sleep(3)
		self.soundhandle.say('ten',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('nine',self.voice)
		self.riddle_turn.publish("turn_robot")#publish msg to nav
		rospy.sleep(1)
		self.soundhandle.say('eight',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('seven',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('six',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('five',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('four',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('three',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('two',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('one',self.voice)
		rospy.sleep(1)
		self.soundhandle.say('here I come',self.voice)
		rospy.sleep(1)
		rospy.Subscriber('human_num', String, self.h_num)
		rospy.Subscriber('female_num', String, self.f_num)
		rospy.Subscriber('male_num', String, self.m_num)
		rospy.Subscriber('taking_photo_signal', String, self.remind_people)
		if self.if_say==0:
			rospy.Subscriber('recognizer_output', String, self.talk_back)

	def h_num(self,msg):
		msg.data=msg.data.lower()
		self.soundhandle.say('I have already taken the photo',self.voice)
		rospy.sleep(3)
		self.soundhandle.say('please wait for a moment',self.voice)
		rospy.sleep(3)
		self.crowd_num=msg.data
		print "human number is " + msg.data
		self.soundhandle.say('human number is  '+msg.data,self.voice)
		rospy.sleep(4)

	def f_num(self,msg):
		msg.data=msg.data.lower()
		print "female number is " + msg.data
		self.female_num=msg.data
		self.soundhandle.say('female number is  '+msg.data,self.voice)
		rospy.sleep(4)

	def m_num(self,msg):
		msg.data=msg.data.lower()
		print "male number is " + msg.data
		self.male_num=msg.data
		self.soundhandle.say('male number is ' +msg.data,self.voice)
		rospy.sleep(4)
		self.soundhandle.say('who wants to play riddles with me',self.voice)
		rospy.sleep(3.5)
		self.soundhandle.say('please stand in front of me and wait for five seconds',self.voice)
		rospy.sleep(8.5)
		self.soundhandle.say('please ask me after you hear',self.voice)
		rospy.sleep(2.5)
		self.soundhandle.playWave(self.question_start_signal+"/question_start_signal.wav")
		rospy.sleep(1.3)
		self.soundhandle.say('Im ready',self.voice)
		rospy.sleep(1.3)
		self.soundhandle.playWave(self.question_start_signal+"/question_start_signal.wav")
		rospy.sleep(1.3)
		self.w=1

	def answer_How_many_people_are_in_the_crowd(self,msg):
		msg.data=msg.data.lower()
		self.soundhandle.say('the answer is there are '+msg.data+' in the crowd',self.voice)
		rospy.sleep(3.5)
		self.soundhandle.say('OK I am ready for next question', self.voice)
		rospy.sleep(2)
		self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
		rospy.sleep(1.2)

	def remind_people(self, msg):
		msg.data = msg.data.lower()
		if msg.data=='start':
			self.soundhandle.say('Im going to take a photo',self.voice)
			rospy.sleep(3)
			self.soundhandle.say('please look at me and smile',self.voice)
			rospy.sleep(3)
			self.soundhandle.say('three',self.voice)
			rospy.sleep(1)
			self.soundhandle.say('two',self.voice)
			rospy.sleep(1)
			self.soundhandle.say('one',self.voice)
			rospy.sleep(1)

	def talk_back(self, msg):
		msg.data = msg.data.lower()
		print msg.data
		if self.w==1 :
			self.sentence_as_array=msg.data.split('-')
			self.sentence=msg.data.replace('-',' ')
			print self.sentence
			#object
			if msg.data.find('which-city-are-we-in')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared which city are we in ', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is Nagoya', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('Nagoya')
			elif msg.data.find('what-is-the-name-of-your-team')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what is the name of your team', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is our team name is kamerider ', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('our team name is kamerider')
			elif msg.data.find('how-many-teams-participate-in-robocup-at-home-this-year')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared how many teams participate in robocup at home this year', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is thirty one', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('31')
			elif msg.data.find('who-won-the-popular-vote-in-the-us-election')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared who won the popular vote in the us election', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is Hillary Clinton ', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('Hillary Clinton')
			elif msg.data.find('what-is-the-highest-mountain-in-japan')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what is the highest mountain in japan', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is Mount Fuji', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('Mount Fuji')
			elif msg.data.find('platforms')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared name the two robocup at home standard platforms', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer Pepper and HSR', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('Pepper and HSR')
			elif msg.data.find('what-does-dspl-stand-for')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what does dspl stand for', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is Domestic Standard Platform League', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('Domestic Standard Platform League')
			elif msg.data.find('what-does-sspl-stand-for')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what does sspl stand for', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is Social Standard Platform League', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('Social Standard Platform League')
			elif msg.data.find('who-did-alphabet-sell-boston-dynamics-to')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared who did alphabet sell boston dynamics to', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is SoftBank', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('SoftBank')
			elif msg.data.find('nagoya-has-one-of-the-largest-train-stations-in-the-world-how-large-is-it')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared nagoya has one of the largest train stations in the world how large is it', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is over 410000 square metres ', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('over 410000 square metres')
			elif msg.data.find('whats-your-teams-home-city')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared whats your teams home city', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is tianjin', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('tianjin')
			elif msg.data.find('who-created-star-wars')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared who created star wars', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is George Lucas ', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('George Lucas')
			elif msg.data.find('who-lives-in-a-pineapple-under-the-sea')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared who lives in a pineapple under the sea', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is Sponge Bob Squarepants ', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('Sponge Bob Squarepants')
			elif msg.data.find('what-did-grace-hopper-invent')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what did grace hopper invent', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is the inventor of the first compiler ', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(4)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
				rospy.sleep(4)
				print('the inventor of the first compiler')
			elif msg.data.find('which-country-is-the-host-of-robocup-ap')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared which-country-is-the-host-of-robocup-ap', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is thailand', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")

			elif msg.data.find('what-is-the-name-of-your-team')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what is the name of your team', self.voice)
				rospy.sleep(4)
				 
				self.soundhandle.say('the answer is our team name is kamerider ', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('wonder')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				 
				self.soundhandle.say('I heared who-is-the-lead-actress-of-wonder-women', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is gal gadot', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('which-operating-system-are-you-using')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				 	
				self.soundhandle.say('I heared which-operating-system-are-you-using', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is linux', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('who-is-the-richest-man-in-the-world')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared who-is-the-richest-man-in-the-world', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is jeff bezos', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('name-one-of-the-famous-thai-food')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared name-one-of-the-famous-thai-food', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is tom yum goong', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('where-are-you-from')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared where-are-you-from', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('I come from China', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('current')>-1 or msg.data.find('president')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared who-is-current-United-state-president', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is donald trump', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('stations')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared how-many-stations-are-there-in-BTS-skytrains', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is thrity-five', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('next-world')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared where-will-next-world-robocup-be-held', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is Montresl canada ', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('singer')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared Who-is-the-singer-of-the-song-grenade', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is Bruno mars', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('which-robot-platfrorm-is-used-for-educaational=league')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared which-robot-platfrorm-is-used-for-educaational=league', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is turtle bot', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('tell-me-the-name-of-this-venue')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared tell-me-the-name-of-this-venue', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is bangkok international trade and exhibition center ', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('iphone')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared how-much-doex-iphone-x-cost-in usa', self.voice)
				rospy.sleep(5)
				self.soundhandle.say('the answer is 999 us dollars ', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('what-is-the-batman-super-power')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what-is-the-batman-super-power', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is rich ', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('how-many-team-in-at-home-league')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared how-many-team-in-at-home-league', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is 7 teams ', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('what-is-the-biggest-airport-in-thailand')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what-is-the-biggest-airport-in-thailand', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is suvarnabhumi airport', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('what-is-the-tallest-building-in-the-world')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what-is-the-tallest-building-in-the-world', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is burj khalifa', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('what-is-a-name-of-our-galaxy')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what-is-the-name-of-our-galaxy', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is milky way', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('what-is-the-symbolic-animal-of-thailand')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared what-is-the-symbolic-animal-of-thailand', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is elephant', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			elif msg.data.find('how-many-time-robocup-held-in-thailand')>-1:
				os.system("~/catkin_ws/src/speech/kill_pocketsphinx.sh")
				self.soundhandle.say('I heared how-many-time-robocup-held-in-thailand', self.voice)
				rospy.sleep(4)
				self.soundhandle.say('the answer is one time', self.voice)
				rospy.sleep(3)
				self.soundhandle.say('OK I am ready for next question', self.voice)
				rospy.sleep(2.5)
				os.system("~/catkin_ws/src/speech/run_pocketsphinx.sh")
				self.soundhandle.playWave(self.question_start_signal + "/question_start_signal.wav")
			else:
				print 2	

		
		
	def cleanup(self):
		rospy.loginfo("Shutting down spr node...")



if __name__=="__main__":
	rospy.init_node('spr')
	try:
		spr()
		rospy.spin()
	except:
		pass




		
