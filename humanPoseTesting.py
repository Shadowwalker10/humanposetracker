#!/usr/bin/env python
# coding: utf-8

# In[6]:


import PoseModule as pm
import cv2 as cv
import time


# 
# ![Screenshot%202021-08-24%20080516.png](attachment:Screenshot%202021-08-24%20080516.png)

# ![Screenshot%202021-08-24%20080705.png](attachment:Screenshot%202021-08-24%20080705.png)

# In[10]:


detector = pm.poseDetector()
cap = cv.VideoCapture(0)
pTime = 0

while True:
    try:
        
        part = int(input('Enter the part you want to track [0 till 32]'))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
while True:
    success,img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img,draw = False)
    if len(lmList)!=0:
        print(lmList[int(part)])
        cv.circle(img,(lmList[int(part)][1],lmList[int(part)][2]),5,(0,255,244),cv.FILLED)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv.putText(img,str(int(fps)),(70,50),cv.FONT_HERSHEY_PLAIN,3,(255,0,0))
    cv.imshow('Image',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()


# In[ ]:




