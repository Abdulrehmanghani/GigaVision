import glob
import cv2
import pandas as pd
import numpy
import math
import os
import json
  
# Opening JSON file
f = open('Tracking-data/instances_train2017_split_track.json')
data = json.load(f)

outpath = 'Tracking-data/visulization_track'
os.makedirs(outpath)

for i in range(len(data['images'])):
    imge = data["images"][i]['file_name']
    
    img = cv2.imread('Tracking-data/GigaTrainSamples/'+imge)
    orig=img.copy()
    ids = data["images"][i]['id']

    for j in range(len(data["annotations"])):
        # print(data["annotations"][j]['image_id'])
        if ids == data["annotations"][j]['image_id']:
           cat_id=data["annotations"][j]['category_id'] 
   
           xmin=int(data["annotations"][j]['bbox'][0])
           ymin=int(data["annotations"][j]['bbox'][1])
           xmax=int(data["annotations"][j]['bbox'][0]+data["annotations"][j]['bbox'][2])
           ymax=int(data["annotations"][j]['bbox'][1]+data["annotations"][j]['bbox'][3])
           
            # print(frame_data['xmin'][i]*width)
           cv2.rectangle(img,(xmin,ymin),
                                  (xmax,ymax),(0,0,255),10)
           cv2.putText(img, str(cat_id), (int(xmin)-5, int(ymin)-15), cv2.FONT_HERSHEY_SIMPLEX,  
                           10, (255,0,0), 10, cv2.LINE_AA)
    
    cv2.imwrite(outpath+"/"+imge,img)