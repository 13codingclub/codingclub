from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

import msvcrt
import time
import sys
import os

from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tf.keras.models.load_model("C:/dev/cozmo_sdk/codingclub/thumbsup/keras_model.h5", compile=False )

start_time = time.time()
prediction = []

def on_new_camera_image(evt, **kwargs):
	start = time.time()
	
	# Only process one photo per half second.  We dont want to take up too 
	# much processing power.
	global start_time
	if (time.time() - start_time < 0.5):
		return
	
	start_time = start
	image = kwargs['image'].raw_image
	
	# Create the array of the right shape to feed into the keras model
	# The 'length' or number of images you can put into the array is
	# determined by the first position in the shape tuple, in this case 1.
	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
		
	#resize the image to a 224x224 with the same strategy as in TM2:
	#resizing the image to be at least 224x224 and then cropping from the center
	size = (224, 224)
	image = ImageOps.fit(image, size, Image.ANTIALIAS)
	
	#turn the image into a numpy array
	image_array = np.asarray(image)
	
	# Normalize the image
	normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
	
	# Load the image into the array
	data[0] = normalized_image_array
	
	# run the inference
	global prediction
	prediction = model.predict(data)
	print( prediction )
	
def cozmo_program(robot: cozmo.robot.Robot):
	# move cozmos head up so he can see better
	robot.set_head_angle(degrees(10.0)).wait_for_completed()
	robot.set_lift_height(0.0).wait_for_completed()
	
	# Start taking pictures
	robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)

	while 1:
		if msvcrt.kbhit(): 
			break #exit when a keypress is hit
		time.sleep(0.2)

		global prediction
		if ( len( prediction ) > 0 ) :
			if ( prediction[0][1] > 0.90 ):
				robot.say_text("Thumbs up").wait_for_completed()
				# Reset the prediction variable so we dont do the same thing again.
				prediction = {}

cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)


	




