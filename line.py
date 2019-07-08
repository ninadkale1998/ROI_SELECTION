import cv2
from time import time
sbox = []
ebox = []
def on_mouse(event, x, y, flags, params):
    #global b
    print("mouse event")
    '''
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Start Mouse Position: '+str(x)+', '+str(y))
        sbox = [x, y]
        
    elif event == cv2.EVENT_LBUTTONUP:
        print ('End Mouse Position: '+str(x)+', '+str(y))
        ebox = [x, y]
        b = False

   '''     

b = True

def select_roi(img):
    key = ''
    roi_no = 1
    cordinates_line = []
    
    while key == '':  #want to select roi
        print("Please select detection line")
        
        b = True
        count = 0
        while b:
            
            cv2.namedWindow('ROI no: ' + str(roi_no))
            print("up")
            cv2.setMouseCallback('ROI no: ' + str(roi_no), on_mouse, 0)
            print("down")
            cv2.imshow('ROI no: ' + str(roi_no), img)
            cordinates_line.append(sbox)
            cordinates_line.append(ebox)
            print(b)

            if count < 50:
                if cv2.waitKey(33) == "z":
                    cv2.destroyAllWindows()
                    break
            elif count >= 50:
                if cv2.waitKey(0) == "z":
                    cv2.destroyAllWindows()
                    break
                count = 0
            
            count += 1

        b = True
        print("Please select line to for speed detection. Considering car direction, keep this line before detection line")
        cv2.line(img, sbox, ebox, (0,255,0), 2)
        while b:
            cv2.setMouseCallback('ROI no: ' + str(roi_no), on_mouse, 0)
            cv2.imshow('ROI no: ' + str(roi_no), img)
            cordinates_line.append(sbox)
            cordinates_line.append(ebox)
        b = True    
        cv2.line(img, sbox, ebox, (0,255,0), 2)    
        key = input("Do you want to select another ROI")
        if key != '':
            break
        roi_no = roi_no + 1
    return cordinates_line
    
    while True:
        cv2.namedWindow('real image')
        cv2.setMouseCallback('real image', on_mouse, 0)
        cv2.imshow('real image', img)
        cordinates_line.append(sbox)
        

    return cordinates_line
img = cv2.imread('1.JPG',0)
cord = select_roi(img)
print(cord)

'''
count = 0

while(b):
    count += 1
    img = cv2.imread('1.JPG',0)
    
    cv2.namedWindow('real image')
    cv2.setMouseCallback('real image', on_mouse, 0)
    cv2.imshow('real image', img)
    
    
    if cv2.waitKey(33) == ord('z'):
        
        break

    if count < 50:
        if cv2.waitKey(33) == 27:
            cv2.destroyAllWindows()
            break
    elif count >= 50:
        if cv2.waitKey(0) == 27:
            cv2.destroyAllWindows()
            break
        count = 0
'''        