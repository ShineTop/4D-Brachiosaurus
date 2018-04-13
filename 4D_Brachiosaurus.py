#!/usr/bin/python3
########################################################################
#                          4D Brachiosaurus                            #
########################################################################
# Description:                                                         #
# This program contols a toy dinosaur. A button is pressed to make     #
# the brachiosaurus move and bellow.                                   #
#                                                                      #
# This program is also a demonstration of controlling a motor using    #
# the gpiozero module.                                                 #
# This program is also an example of adding color to text displayed to #
# the screen.                                                          #
#                                                                      #
#                                                                      #
# Author: Paul Ryan                                                    #
#                                                                      #
########################################################################

########################################################################
#                          Import files                                #
########################################################################

from gpiozero import Motor, Button, OutputDevice
from time import sleep
from signal import pause
import pygame
import random
import os, sys, logging

########################################################################
#                           Variables                                  #
########################################################################

brachiosaurus_motor = Motor(23, 18, True)		# forward, backward, pwm
brachiosaurus_motor_enable = OutputDevice(24)
blue_button = Button(25)
red_button = Button(9) 

########################################################################
#                           Initialize                                 #
########################################################################

pygame.mixer.init()

logging.basicConfig(filename='Files/Brachiosaurus.log', filemode='w',
	level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
	datefmt='%m/%d/%y %I:%M:%S %p:')

########################################################################
#                            Functions                                 #
########################################################################
'''
This is the main function. It will wait until one of two buttons is 
pressed. One button will start the program and the other button will
stop the program. Pressing Ctrl-C will also stop the program.
'''
def main():
	try:
		logging.info("START")
		# Check to see that the necessary files exist
		file_check()
		# Check to see if files are accessible
		permission_check()
		# Read the dinosaur_facts.txt file to populate the dino_facts list.
		dino_facts = read_file("Files/dinosaur_facts.txt")
		# Check to see if the file is empty
		empty_file_check(dino_facts)
		# Acknowledge that prelimiary checks are complete
		logging.info("Prelimiary checks are complete. Starting program...")
		# Display program header
		print_header()
		# Pre-load the first sound file
		bellow, bellow_length = get_bellow()
		# Prompt the user to press a button
		prompt_user_for_input()
		
		while True:
			
			if blue_button.is_pressed:
				# Print out a random dinosaur fun fact
				print_dinosaur_fact(dino_facts)
				# Move the Brachiosaurus for the duration of the sound file
				activate_brachiosaurus(bellow, bellow_length)
				# Prompt the user again to press a button
				prompt_user_for_input()
				# Load the next sound file
				bellow, bellow_length = get_bellow()
				
			if red_button.is_pressed:
				stop_the_program()
				
	except KeyboardInterrupt:
		stop_the_program()

'''
The file_check function checks to see if the necessary files exist.
If they all exist, the program will continue.
If a file is missing, the program will print a message and exit.
'''
def file_check():
	
	file_missing_flag = 0
	
	logging.info("FILE CHECK")
	# Check to see if dinosaur_facts.txt file exists
	if os.path.isfile('Files/dinosaur_facts.txt'):
		logging.info("dinosaur_facts.txt file was found!")
	else:
		detail_log.error("dinosaur_facts.txt file was not found! Make sure that the dinosaur_facts.txt file exists in the Files folder.")
		file_missing_flag = 1
	# Check to see if brachiosaurus1.mp3 file exists
	if os.path.isfile('Sounds/brachiosaurus1.mp3'):
		logging.info("brachiosaurus1.mp3 file was found!")
	else:
		logging.error("brachiosaurus1.mp3 file was not found! Make sure that the brachiosaurus1.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if brachiosaurus2.mp3 file exists
	if os.path.isfile('Sounds/brachiosaurus2.mp3'):
		logging.info("brachiosaurus2.mp3 file was found!")
	else:
		logging.error("brachiosaurus2.mp3 file was not found! Make sure that the brachiosaurus2.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if brachiosaurus3.mp3 file exists
	if os.path.isfile('Sounds/brachiosaurus3.mp3'):
		logging.info("brachiosaurus3.mp3 file was found!")
	else:
		logging.error("brachiosaurus3.mp3 file was not found! Make sure that the brachiosaurus3.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if brachiosaurus4.mp3 file exists
	if os.path.isfile('Sounds/brachiosaurus4.mp3'):
		logging.info("brachiosaurus4.mp3 file was found!")
	else:
		logging.error("brachiosaurus4.mp3 file was not found! Make sure that the brachiosaurus4.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if brachiosaurus5.mp3 file exists
	if os.path.isfile('Sounds/brachiosaurus5.mp3'):
		logging.info("brachiosaurus5.mp3 file was found!")
	else:
		logging.error("brachiosaurus5.mp3 file was not found! Make sure that the brachiosaurus5.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if brachiosaurus6.mp3 file exists
	if os.path.isfile('Sounds/brachiosaurus6.mp3'):
		logging.info("brachiosaurus6.mp3 file was found!")
	else:
		logging.error("brachiosaurus6.mp3 file was not found! Make sure that the brachiosaurus6.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if brachiosaurus7.mp3 file exists
	if os.path.isfile('Sounds/brachiosaurus7.mp3'):
		logging.info("brachiosaurus7.mp3 file was found!")
	else:
		logging.error("brachiosaurus7.mp3 file was not found! Make sure that the brachiosaurus7.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if brachiosaurus8.mp3 file exists
	if os.path.isfile('Sounds/brachiosaurus8.mp3'):
		logging.info("brachiosaurus8.mp3 file was found!")
	else:
		logging.error("brachiosaurus8.mp3 file was not found! Make sure that the brachiosaurus8.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1

	# If there are no missing files, return to the main function
	# Otherwise print out message and exit the program
	if file_missing_flag == 0:
		return
	else:
		print("\033[1;31;40mErrors were encountered. Check the log in the 'Files' folder for more details.\033[1;31;40m")
		stop_the_program()

'''
The permission_check function checks to see if the user has permission
to read the necessary files. If so, the program will continue. If not, 
messages are printed out to the screen and the program will exit.
'''
def permission_check():
	
	permission_flag = 0
	
	logging.info("PERMISSION CHECK")
	# Check to see if user has read access to dinosaur_facts.txt
	if os.access('Files/dinosaur_facts.txt', os.R_OK):
		logging.info("User has permission to read the dinosaur_facts.txt file.")
	else:
		logging.error("User does not have permission to read the dinosaur_facts.txt file.")
		permission_flag = 1
	# Check to see if user has read access to brachiosaurus1.mp3
	if os.access('Sounds/brachiosaurus1.mp3', os.R_OK):
		logging.info("User has permission to read the brachiosaurus1.mp3 file.")
	else:
		logging.error("User does not have permission to read the brachiosaurus1.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to brachiosaurus2.mp3
	if os.access('Sounds/brachiosaurus2.mp3', os.R_OK):
		logging.info("User has permission to read the brachiosaurus2.mp3 file.")
	else:
		logging.error("User does not have permission to read the brachiosaurus2.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to brachiosaurus3.mp3
	if os.access('Sounds/brachiosaurus3.mp3', os.R_OK):
		logging.info("User has permission to read the brachiosaurus3.mp3 file.")
	else:
		logging.error("User does not have permission to read the brachiosaurus3.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to brachiosaurus4.mp3
	if os.access('Sounds/brachiosaurus4.mp3', os.R_OK):
		logging.info("User has permission to read the brachiosaurus4.mp3 file.")
	else:
		logging.error("User does not have permission to read the brachiosaurus4.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to brachiosaurus5.mp3
	if os.access('Sounds/brachiosaurus5.mp3', os.R_OK):
		logging.info("User has permission to read the brachiosaurus5.mp3 file.")
	else:
		logging.error("User does not have permission to read the brachiosaurus5.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to brachiosaurus6.mp3
	if os.access('Sounds/brachiosaurus6.mp3', os.R_OK):
		logging.info("User has permission to read the brachiosaurus6.mp3 file.")
	else:
		logging.error("User does not have permission to read the brachiosaurus6.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to brachiosaurus7.mp3
	if os.access('Sounds/brachiosaurus7.mp3', os.R_OK):
		logging.info("User has permission to read the brachiosaurus7.mp3 file.")
	else:
		logging.error("User does not have permission to read the brachiosaurus7.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to brachiosaurus8.mp3
	if os.access('Sounds/brachiosaurus8.mp3', os.R_OK):
		logging.info("User has permission to read the brachiosaurus8.mp3 file.")
	else:
		logging.error("User does not have permission to read the brachiosaurus8.mp3 file.")
		permission_flag = 1
	
	if permission_flag == 0:
		return
	else:
		print("\033[1;31;40mErrors were encountered. Check the log in the 'Files' folder for more details.\033[1;31;40m")
		stop_the_program()
'''
The read_file function will read the dinosaur facts file and each 
line of the file will be an element in the fun_facts list. It will then
return the dino_facts list to the main function.
If the program is unable to read the file, it will display an error
message and then exit the program.
If the dino_facts file is empty, an error message will be displayed 
and the program will exit.
'''
def read_file(file_name):
	logging.info("READING DINOSAUR_FACTS.TXT")
	with open(file_name, "r") as f:   # open the file as read-only
		dino_facts = f.readlines()

	return dino_facts
	
'''
This empty_file_check function checks to see if the file is empty. If it
is, the program will print a message to the screen. If not, the program
will continue.
'''
def empty_file_check(file_name):		
	logging.info("EMPTY FILE CHECK")
	if file_name == []:
		logging.error("The dinosaur.txt file is empty. The program won't work.")
		print("\033[1;31;40mErrors were encountered. Check the log in the 'Files' folder for more details.\033[1;31;40m")
		stop_the_program()
	else:
		logging.info("The dinosaur.txt file is not empty.(This is good. We don't want an empty file.)")
		
'''
The print_header function will print out the program header to the 
screen.
'''
def print_header():
	print("\n")
	print("\033[1;34;40m=====================================================================================")
	print("\033[1;34;40m  _  _   ____    ____                 _     _                                        ")
	print("\033[1;34;40m | || | |  _ \  | __ ) _ __ __ _  ___| |__ (_) ___  ___  __ _ _   _ _ __ _   _ ___   ")
	print("\033[1;34;40m | || |_| | | | |  _ \| '__/ _` |/ __| '_ \| |/ _ \/ __|/ _` | | | | '__| | | / __|  ")
	print("\033[1;34;40m |__   _| |_| | | |_) | | | (_| | (__| | | | | (_) \__ \ (_| | |_| | |  | |_| \__ \  ")
	print("\033[1;34;40m    |_| |____/  |____/|_|  \__,_|\___|_| |_|_|\___/|___/\__,_|\__,_|_|   \__,_|___/  ")
	print("\033[1;34;40m                                                                                     ")
	print("\033[1;34;40m=====================================================================================")
	print("\n")
                                                      

'''
The get_bellow function will randomly select one of the Brachiosaurus 
bellow sound files and return it and its file length to the main 
function.
'''
def get_bellow():
	
	bellow1 = "Sounds/brachiosaurus1.mp3"
	bellow2 = "Sounds/brachiosaurus2.mp3"
	bellow3 = "Sounds/brachiosaurus3.mp3"
	bellow4 = "Sounds/brachiosaurus4.mp3"
	bellow5 = "Sounds/brachiosaurus5.mp3"
	bellow6 = "Sounds/brachiosaurus6.mp3"
	bellow7 = "Sounds/brachiosaurus7.mp3"
	bellow8 = "Sounds/brachiosaurus8.mp3"

	bellow1_length = 2       # lenth of file in seconds
	bellow2_length = 3       # lenth of file in seconds
	bellow3_length = 5       # lenth of file in seconds
	bellow4_length = 3       # lenth of file in seconds
	bellow5_length = 2       # lenth of file in seconds
	bellow6_length = 4       # lenth of file in seconds
	bellow7_length = 5       # lenth of file in seconds
	bellow8_length = 6       # lenth of file in seconds
	
	bellows = [bellow1, bellow2, bellow3, bellow4, bellow5, bellow6, bellow7, bellow8]
	
	bellow = random.choice(bellows)   # Selects random sound file
	
	if bellow == bellow1:
		return bellow, bellow1_length
	elif bellow == bellow2:
		return bellow, bellow2_length
	elif bellow == bellow3:
		return bellow, bellow3_length
	elif bellow == bellow4:
		return bellow, bellow4_length
	elif bellow == bellow5:
		return bellow, bellow5_length
	elif bellow == bellow6:
		return bellow, bellow6_length
	elif bellow == bellow7:
		return bellow, bellow7_length
	else:
		return bellow, bellow8_length

'''
The print_dinosaur_fact function prints out a random fact about 
dinosaurs. The dino_facts file needs to be sent to this function.
'''
def print_dinosaur_fact(dino_facts):
	print("\033[1;34;40mDINOSAUR FUN FACT:")
	print(random.choice(dino_facts))

'''
The activate_brachiosaurus funciton takes 2 inputs: bellow and bellow_length. 
This function will play the sound file and then activate the motor for 
the duration of the sound file. 
'''
def activate_brachiosaurus(bellow, bellow_length):
	try:
		brachiosaurus_motor.value = 0.6      # Controls the motor speed
	except ValueError:
		logging.error("A bad value was specified for brachiosaurus_motor. The value should be between 0 and 1.")
		print("\033[1;31;40mAn error was encountered. Check the detail log for more information\n")
		stop_the_program()
	pygame.mixer.music.load(bellow)          # Loads the sound file
	pygame.mixer.music.play()              	 # Plays the sound file
	brachiosaurus_motor_enable.on()        	 # Starts the motor
	sleep(bellow_length)
	brachiosaurus_motor_enable.off()       	 # Stops the motor

'''
The prompt_user_for_input function prompts a user to push a button.
'''
def prompt_user_for_input():
	print("\033[1;37;40mPush the \033[1;34;40mblue button \033[1;37;40mto activate the \033[1;34;40mBrachiosaurus\033[1;37;40m.")
	print("\033[1;37;40mPush the \033[1;31;40mred button \033[1;37;40mor press Ctrl-C to \033[1;31;40mstop \033[1;37;40mthe program.\n")

'''
The release_gpio_pins function realeases the gpio pins.
'''
def release_gpio_pins():
	brachiosaurus_motor.close()
	brachiosaurus_motor_enable.close()
	red_button.close()
	blue_button.close()

def stop_the_program():
	release_gpio_pins()
	print("\033[1;37;40mExiting program.\n")
	logging.info("END")
	exit()
	
if __name__ == '__main__':
	main()
