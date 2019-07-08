import cv2
from numpy import genfromtxt
import numpy as np
import math
import os
cap = cv2.VideoCapture("1.MOV")
#_, first_frame = cap.read()


skip_frame = 60
frame_number = 1

path_roa = os.path.isfile('ROA.csv')
path_rois = os.path.isfile('ROIs.csv')

#ROA = np.array([])
_, frame = cap.read()

#def Skip_frame(cap):

#boxes = []
def on_mouse(event, x, y, flags, params):
    if event == cv.CV_EVENT_LBUTTONDOWN:
        print ('Start Mouse Position: '+str(x)+', '+str(y))
        sbox = [x, y]
        boxes.append(sbox)
    elif event == cv.CV_EVENT_LBUTTONUP:
        print ('End Mouse Position: '+str(x)+', '+str(y))
        ebox = [x, y]
        boxes.append(ebox)

def draw(event,x,y,flags,params):
    global ix,iy,drawing
    # Left Mouse Button Down Pressed
    if(event==1):
        drawing = True
        ix = x
        iy = y
    if(event==0):
        if(drawing==True):
            #For Drawing Line
            cv2.line(image,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=3)
            ix = x
            iy = y
            # For Drawing Rectangle
            # cv2.rectangle(image,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=3)
    if(event==4):
        drawing = False


def Select_Regions(frame):
	ROA = np.array([])
	ROIs = np.array([])
	cv2.namedWindow('real image')
	cv2.setMouseCallback('real image', draw, 0)
	if path_roa:
	    key = input("Saved ROA detected. Press Enter if you want to proceed with it otherwise press anything and Enter")
	    if key == '':
	        #read from csv write into ROA
	        ROA = genfromtxt('ROA.csv', delimiter=',')
	        frame = frame[int(ROA[1]):int(ROA[1]+ROA[3]), int(ROA[0]):int(ROA[0]+ROA[2])]    
	        
	    else:
	        ROA_det = cv2.selectROI('Select Region of Area', frame, False)	      
	        ROA = np.array(ROA_det)
	        ROA = np.asarray(ROA)
	        np.savetxt("ROA.csv", ROA, delimiter=",")
	        cv2.destroyWindow('Select Region of Area')
	        frame = frame[int(ROA_det[1]):int(ROA_det[1]+ROA_det[3]), int(ROA_det[0]):int(ROA_det[0]+ROA_det[2])]    

	else:
	    ROA_det = cv2.selectROI('Select Region of Area', frame, False)	      
	    ROA = np.array(ROA_det)
	    ROA = np.asarray(ROA)
	    np.savetxt("ROA.csv", ROA, delimiter=",")
	    cv2.destroyWindow('Select Region of Area')
	    frame = frame[int(ROA_det[1]):int(ROA_det[1]+ROA_det[3]), int(ROA_det[0]):int(ROA_det[0]+ROA_det[2])]    

	
	if path_rois:
	    key = input("Saved ROIs detected. Press Enter if you want to proceed with it otherwise press anything and Enter")
	    if key == '':
	        #read from csv write into ROIs
	        ROIs = genfromtxt('ROIs.csv', delimiter=',')
	    else:
	       cv2.imshow('real image', frame)
	       if cv2.waitKey(20) & 0xFF == ord('q'):
	           print(ix)
	           print(iy)
	       #print(boxes)
	    while  True:
	        	a = 2
	    '''
	        ROIs = cv2.selectROIs('Select Region of interests', frame, False)	      
	        ROIs = np.array(ROIs)
	        ROIs = np.asarray(ROIs)
	        np.savetxt("ROIs.csv", ROIs, delimiter=",")
	        cv2.destroyWindow('Select Region of interests')
	        '''
	else:
	    ROIs = cv2.selectROIs('Select Region of interests', frame, False)	      
	    ROIs = np.array(ROIs)
	    ROIsA = np.asarray(ROIs)
	    np.savetxt("ROIs.csv", ROIs, delimiter=",")
	    cv2.destroyWindow('Select Region of interests')
	
	return ROA , ROIs

roa , rois = Select_Regions(frame)

print(rois)
print(roa)



while True:
    # Read image
    
    frame_number = frame_number + 1
    if frame_number%skip_frame == 0:
        
        '''
        text = raw_input("Press ENTER if you want to go to the next frame else for car Press c, for motorbike press m for rickshaw press r ")
        if text == '':
        	continue
        elif text == "c":
        	imCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
            	
        cv2.imshow("Image", imCrop)
        text = raw_input("Press enter if you want to go to the next frame else for car a ")
        '''
        #print(r)
    key = cv2.waitKey(30)
    if key == 27:
        break




cap.release()
cv2.destroyAllWindows()
