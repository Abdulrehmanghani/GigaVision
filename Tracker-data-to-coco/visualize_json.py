import glob
import cv2
import pandas as pd
import numpy
import math
import os
import json
  
# Opening JSON file
f = open('instances_train2017.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
print(len(data))
for i in range(len(data['images'])):
    imge = data["images"][i]['file_name']
    print(imge,i)
    img = cv2.imread('GigaTrainSamples\\'+imge)
    orig=img.copy()
    ids = data["images"][i]['id']

    for j in range(len(data["annotations"])):
        # print(data["annotations"][j]['image_id'])
        if ids == data["annotations"][j]['image_id']:
           cat_id=data["annotations"][j]['category_id'] 
    # frame_data=tracker_csv[tracker_csv['Frame_Number']=='I'+imge.split('\I')[1]].reset_index(drop=True)
    # print(frame_data)
    # for i in range(len(frame_data)):
        # clas = frame_data['Class'][i]
        # print(clas)
        # height=int(frame_data['height'][i])
        # width=int(frame_data['width'][i])
            xmin=int(data["annotations"][j]['bbox'][0])
            ymin=int(data["annotations"][j]['bbox'][1])
            xmax=int(data["annotations"][j]['bbox'][0]+data["annotations"][j]['bbox'][2])
            ymax=int(data["annotations"][j]['bbox'][1]+data["annotations"][j]['bbox'][3])
           
            # print(frame_data['xmin'][i]*width)
            cv2.rectangle(img,(xmin,ymin),
                                  (xmax,ymax),(0,0,255),10)
            cv2.putText(img, str(cat_id), (int(xmin)-5, int(ymin)-15), cv2.FONT_HERSHEY_SIMPLEX,  
                           10, (255,0,0), 10, cv2.LINE_AA)
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
    
    cv2.imwrite("testimg\\"+imge,img)