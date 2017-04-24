#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, urllib2; from os import system

class MyBulkSmsSender:
	def __init__(self, ip, password, number, message):
		self.ip, self.password, self.number, self.message = ip, password, number, message
		url = "http://" + str(ip) + ":8080/?number=" + str(number) + "&password=" + str(password) + "&message=" + message
		response = urllib2.urlopen(url).read().find("OK", 4 ,7)
		if response == 5:	print " [+] Message was Sent to: {0}".format(number)
		print "\n"

def main():
	system('clear');print """
______       _ _                         
| ___ \     | | |                        
| |_/ /_   _| | | ____      ____ _ _   _ 
| ___ \ | | | | |/ /\ \ /\ / / _` | | | |
| |_/ / |_| | |   <  \ V  V / (_| | |_| |
\____/ \__,_|_|_|\_\  \_/\_/ \__,_|\__, |
   Author: Muhammad Adeel           __/ |
   Mail:   Chaudhary1337@gmail.com |____/ 
-----------------------------------------\n"""
	if len(sys.argv) < 5:	exit(" [*] Usage: BulkSmsAndroid.py <ip> <password> <number | numberList.txt> <message>\n")
	if sys.argv[3].endswith("txt"):
		with open(sys.argv[3]) as numList:
			for number in numList.readlines():
				number = number.strip("\n")
				app = MyBulkSmsSender(sys.argv[1], sys.argv[2], number, sys.argv[4])
		numList.close()
	else:	app = MyBulkSmsSender(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == '__main__':
	try:
		main()
	except Exception, e:
		print e
		exit()
