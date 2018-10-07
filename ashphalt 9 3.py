import numpy as np
from PIL import ImageGrab as ig
import cv2
import time

import time
from directkeys import ReleaseKey, PressKey, W, A, S, D 


def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)

    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],
                         ], np.int32)
    processed_img = roi(processed_img, [vertices])
    return processed_img



last_time = time.time()
while True:

     screen = np.array(ig.grab(bbox=(50,50,800,640)))
    # print('Loop took {} seconds',format(time.time()-last_time))
     last_time = time.time()
     new_screen=process_img(screen)
     
     cv2.imshow("test",new_screen)
     last_time = time.time()
     if cv2.waitKey(25) & 0xFF == ord('q'):
         cv2.destroyAllWindows()
         break
