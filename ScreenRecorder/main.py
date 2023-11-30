from PIL import ImageGrab
from utils.videostream import WebcamVideoStream
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime
import os

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

filepath = os.getcwd() + '\\Recordings\\' # change according to project

now = datetime.datetime.now()
timestamp = now.strftime('%Y-%m-%d-T%H%M%S')
filename = f'{timestamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(filepath + filename, fourcc, 10.0, (width, height))

webcam = WebcamVideoStream(src=0).start()

while captured_video.isOpened():
    img = ImageGrab.grab(bbox=(0, 0, width, height)) 
    img_np = np.array(img) 
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) # convert to correct color scheme
    frame = webcam.read()
    frame_height, frame_width, _ = frame.shape
    img_final[height-frame_height:height, 0:frame_width, :] = frame[0:frame_height, 0:frame_width, :] # overlay webcam on screen recording
    cv2.imshow('Screen Recorder', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break

captured_video.release()
cv2.destroyAllWindows()