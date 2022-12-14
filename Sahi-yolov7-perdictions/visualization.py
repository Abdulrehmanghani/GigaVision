import glob
import cv2
import pandas as pd
import numpy
import math
import os
import json
  
# Opening JSON file
f = open('result.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
df=pd.read_csv('training_data.csv')
k = 1
for i in range(len(df['image id'].unique())):
    # img_id = data[i]["image_id"]
    da=df[df['image id']==k]
    
    imge = da['Frame_Number'].unique().item()
    print(imge)
    img = cv2.imread('train2017\\'+imge)
    orig=img.copy()
    # ids = data[i]["images"]['id']

    for j in range(len(data)):
        # print(data["annotations"][j]['image_id'])
        if k == data[j]['image_id']:
            
    # frame_data=tracker_csv[tracker_csv['Frame_Number']=='I'+imge.split('\I')[1]].reset_index(drop=True)
    # print(frame_data)
    # for i in range(len(frame_data)):
        # clas = frame_data['Class'][i]
        # print(clas)
        # height=int(frame_data['height'][i])
        # width=int(frame_data['width'][i])
            
            # try:
            xmin=int(data[j]['bbox'][0])
            ymin=int(data[j]['bbox'][1])
            xmax=int(data[j]['bbox'][0]+data[j]['bbox'][2])
            ymax=int(data[j]['bbox'][1]+data[j]['bbox'][3])
            cat_id = data[j]['category_id']
            # print(cat_id,ymax)

            # except:
            #     continue
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
    k = k+1
    cv2.imwrite("json_result\\"+imge,img)