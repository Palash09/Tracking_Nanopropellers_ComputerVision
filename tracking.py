import cv2
import numpy as np

video_file = "Propellers_Video.avi" #test video

kernel_dil = np.ones((20,20),np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

fgbg = cv2.createBackgroundSubtractorKNN() #Background Subtraction function

cap = cv2.VideoCapture(video_file)

#cap = cv2.VideoCapture(0) for taking input from computer’s camera

while True:
	ret,frame = cap.read()

	fshape = frame.shape
	
	frame = frame[1:fshape[0]-2,:fshape[1]-2,:] #cropping the video size

#print frame.shape
	if ret == True:
		fgmask = fgbg.apply(frame)
		fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
		dilation = cv2.dilate(fgmask,kernel_dil,iterations = 1)
		(contours,hierarchy) = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		
		for pic, contour in enumerate(contours):
			area = cv2.contourArea(contour)
			
			if(area>200):
				x,y,w,h = cv2.boundingRect(contour)
				img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
				roi_vehicle = frame[y:y-10+h+5,x:x-8+w+10]
		cv2.imshow("original",frame)
		if cv2.waitKey(25) & 0xFF == ord("q"):
			break
cap.release()
cv2.destroyAllWindows()