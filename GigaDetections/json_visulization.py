import glob
import cv2
import pandas as pd
import numpy
import math
import os
import json
  
# Opening JSON file
f = open('instances_train2017_split.json')
classes = ['none','person','vehicle']
data = json.load(f)
for i in range(len(data['images'])):
    imge = data["images"][i]['file_name']
    try:
        img = cv2.imread('../val/'+imge)
    except:
        continue
    ids = data["images"][i]['id']
    
    for j in range(len(data["annotations"])):

        if ids == data["annotations"][j]['image_id']:

            cat_id=data["annotations"][j]['category_id'] 

            try:
                xmin=int(data["annotations"][j]['bbox'][0])
                ymin=int(data["annotations"][j]['bbox'][1])
                xmax=int(data["annotations"][j]['bbox'][0]+data["annotations"][j]['bbox'][2])
                ymax=int(data["annotations"][j]['bbox'][1]+data["annotations"][j]['bbox'][3])
            except:
                continue
            cv2.rectangle(img,(xmin,ymin),
                                    (xmax,ymax),(0,0,255),5)
            cv2.putText(img, str(classes[cat_id]), (int(xmin)-5, int(ymin)-15), cv2.FONT_HERSHEY_SIMPLEX,  
                           2, (255,0,0), 2, cv2.LINE_AA)
      
    cv2.imwrite("testimg/"+imge,img)
