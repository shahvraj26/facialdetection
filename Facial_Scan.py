from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "haarcascade_frontalface_default.xml")
ap.add_argument("-o", "--output", required=True,
	help="C:\\Users\\vrajshah\\Desktop\\facial\\VrajShah")
args = vars(ap.parse_args())

# load OpenCV's Haar cascade for face detection from disk
detector = cv2.CascadeClassifier(args["cascade"])
# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus far
print("Starting Video Stream Now...SMILE...")
print("Camera will take 40 pictures of you, so move your head around slowly")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(4.0)
total = 0

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream, clone it, (just
	# in case we want to write it to disk), and then resize the frame
	# so we can apply face detection faster
	frame = vs.read()
	orig = frame.copy()
	frame = imutils.resize(frame, width=400)
	# detect faces in the grayscale frame
	rects = detector.detectMultiScale(
		cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30))
	# loop over the face detections and draw them on the frame
	for (x, y, w, h) in rects:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `k` key was pressed, write the *original* frame to disk
	# so we can later process it and use it for face recognition
	if key == ord("k"):
	    p = os.path.sep.join([args["output"], "{}.png".format(
		    str(total).zfill(5))])
	    cv2.imwrite(p, orig)
	    total += 1
	# if the `q` key was pressed, break from the loop
	elif key == ord("q"):
	    break
print("Please DO NOT CLICK ANYTHING HAVE PATIENCE IF NOTHING IS HAPPENING")
print("{} face images stored in /dataset/YourName".format(total))
print("Cleaning up old photos...Updating to new ones")
cv2.destroyAllWindows()
vs.stop()
