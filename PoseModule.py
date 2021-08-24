#!/usr/bin/env python
# coding: utf-8

# # #Importing Libraries

# In[6]:


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import mediapipe as mp
import time


# # # Pose Detection Class

# Init signature:
# mpPose.Pose(
#     static_image_mode=False,
#     model_complexity=1,
#     smooth_landmarks=True,
#     enable_segmentation=False,
#     smooth_segmentation=True,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5,
# )

# In[7]:



class poseDetector():
    #Based on Init Signature of mpPose.Pose
    def __init__(self,mode=False,complexity = 1,smooth_land = True,segment = False,
                 smooth_segment = True,detectionCon = 0.5,TrackConf = 0.5):
        self.mode = mode
        self.complexity = complexity
        self.smooth_land = smooth_land
        self.segment = segment
        self.smooth_segment = smooth_segment
        self.detectionCon = detectionCon
        self.TrackConf = TrackConf
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.complexity,self.smooth_land,self.segment,
                                self.smooth_segment,self.detectionCon,self.TrackConf)
        
    def findPose(self,img,draw = True):
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return img
    
    #Tracking Mechanism:
    def findPosition(self,img,draw = True):
        lmList = []
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv.circle(img,(cx,cy),3,(255,0,0),cv.FILLED)
        return lmList
    
    
#Defining Main: Universal Function to all: relays data to be processed
def main():
    cap = cv.VideoCapture(0)
    pTime = 0
    detector = poseDetector()

    while True:
        success,img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img,draw = False)
        if len(lmList)!=0:
            print(lmList[int(tracker)])
            cv.circle(img,(lmList[14][1],lmList[14][2]),5,(0,255,244),cv.FILLED)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime


        cv.putText(img,str(int(fps)),(70,50),cv.FONT_HERSHEY_PLAIN,3,(255,0,0))
        cv.imshow('Image',img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
if __name__=='__main__':
    main()
    
    
                    
                
                
                
                
            
            
            
    
    
        
        
        
        
    
    

    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




