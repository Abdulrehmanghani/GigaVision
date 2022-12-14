import glob
import cv2
import pandas as pd
import numpy
import math
import os
csv_name='training_data.csv'
tracker_csv = pd.read_csv(csv_name)
print(tracker_csv.tail())
print("Start")
imgs=glob.glob('data\\'+'*.jpg')
if len(imgs)>0:
    for imge in imgs:
        img = cv2.imread(imge)
        orig=img.copy()
        print(imge.split('ta')[1])
        frame_data=tracker_csv[tracker_csv['Frame_Number']=='I'+imge.split('\I')[1]].reset_index(drop=True)
        print(frame_data)
        for i in range(len(frame_data)):
            clas = frame_data['Class'][i]
            print(clas)
            height=int(frame_data['height'][i])
            width=int(frame_data['width'][i])
            try:
                xmin=int(frame_data['xmin'][i]*height)
                ymin=int(frame_data['ymin'][i]*width)
                xmax=int(frame_data['xmax'][i]*height)
                ymax=int(frame_data['ymax'][i]*width)
            except:
                continue
            print(frame_data['xmin'][i]*width)
            cv2.rectangle(img,(xmin,ymin),
                                  (xmax,ymax),(0,0,255),10)
            # elif clas== "Head_Player":
            #     cv2.rectangle(img,(xmin,ymin),
            #                       (xmax,ymax),(0,255,0),2)
            # else:
            #     cv2.rectangle(img,(xmin,ymin),
            #                       (xmax,ymax),(255,255,255),2)

        #         elif frame_data['team_id'][i] == 1:
        #             cv2.rectangle(img,(xmin,ymin),
        #                               (xmax,ymax),(0,0,255),2)
        #         elif frame_data['team_id'][i] == -1:
        #             cv2.rectangle(img,(xmin,ymin),
        #                               (xmax,ymax),(255,255,255),2)
        
        cv2.imwrite("img.jpg",img)