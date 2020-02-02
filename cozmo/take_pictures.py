import cozmo
from cozmo.util import degrees
import time
import sys
import os
import msvcrt

directory = "C:/codingclub/cozmo/pictures/"
if not os.path.exists(directory):
    os.mkdir(directory)

start_time = time.time()
image = 0

def on_new_camera_image(evt, **kwargs):
	start = time.time()
	
	# Only take one photo per half second. 
	global start_time
	if (time.time() - start_time < 0.5):
		return
	
	start_time = start
	pilImage = kwargs['image'].raw_image
	
	global image
	global directory
	image = image + 1
	print( "took photo " + str(image) )
	pilImage.save( directory + "/cozmo-%d.jpg" % image, "JPEG")

def cozmo_program(robot: cozmo.robot.Robot):
	robot.set_head_angle(degrees(10.0)).wait_for_completed()
	robot.set_lift_height(0.0).wait_for_completed()
	robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)
	while 1:
		if msvcrt.kbhit(): 
			break #exit when a keypress is hit
		time.sleep(0.2)	
		
cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)