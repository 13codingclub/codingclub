import cozmo
from cozmo.util import degrees
import time
import sys
import os
imageNumber = 0
directory = 'C:/dev/cozmo_sdk/codingclub/pictures'

def on_new_camera_image(evt, **kwargs):
    pilImage = kwargs['image'].raw_image
    global directory
    pilImage.save( "C:/dev/cozmo_sdk/codingclub/pictures/cozmo-%d.jpg" % kwargs['image'].image_number, "JPEG")

def cozmo_program(robot: cozmo.robot.Robot):
    robot.set_head_angle(degrees(10.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)
    time.sleep(30)
    print("Done: Taking Pictures")
	
cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)