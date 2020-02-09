import cozmo
from cozmo.util import degrees
import time
import sys, getopt
import os
import msvcrt

image = 0
savePhoto = 0
directory = ""

def on_new_camera_image(evt, **kwargs):
	
	global savePhoto
	if savePhoto:
		pilImage = kwargs['image'].raw_image
	
		global image
		global directory
		image = image + 1
		print( "took photo " + str(image) )
		pilImage.save( directory + "/cozmo-%d.jpg" % image, "JPEG")
		savePhoto = 0

def cozmo_program(robot: cozmo.robot.Robot):
	robot.set_head_angle(degrees(10.0)).wait_for_completed()
	robot.set_lift_height(0.0).wait_for_completed()
	robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)
	print( "press q to exit, press p to take a photo" )
	
	while 1:
		if msvcrt.kbhit(): 
			c =  msvcrt.getch()
			print( c )
			if c == b'p':
				print( "saving photo" )
				global savePhoto
				savePhoto = 1
			if c == b'q':
				print( "quiting" )
				break #exit when 'q' is hit, take a photo when 'p' is hit
		time.sleep(0.2)	

def main(argv):
	outputDirectory = "pictures"
	
	try:
		opts, args = getopt.getopt( argv, "o:")
	except getopt.GetoptError:
		print( "test.py -o=<outputdirectory>" )
		sys.exit(2)

	for opt, arg in opts:
		print( opt )
		if opt == '-o':
			outputDirectory = arg

	global directory
	directory = "C:/codingclub/cozmo/" + outputDirectory + "/"
	if not os.path.exists(directory):
		os.mkdir(directory)

	print( "photo output directory is ", directory )

	cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
	

if __name__ == "__main__": 
    main(sys.argv[1:])