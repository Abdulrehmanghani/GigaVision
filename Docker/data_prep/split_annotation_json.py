#!/usr/bin/env python
# coding: utf-8

# In[59]:


import glob
import cv2
import pandas as pd
import numpy
import math
import os
import json
  
# Opening JSON file
f = open('Tracking-data/instances_train2017.json')
_list = glob.glob('Tracking-data/GigaTrainSamples/*.jpg')
img_list = []
for i in range(len(_list)):
#     print(_list[i].split('\\')[1])
    img_list.append(_list[i].split('/')[2])
# returns JSON object as 
# a dictionary
# print(im_list)
data = json.load(f)
k = 0
image_list= []
ann_list=[]
for i in range(len(data['images'])):
    imge = data["images"][i]['file_name']
    
    if imge  in img_list:
        image_list.append(data["images"][i])
        ids = data["images"][i]['id']
        k = k+1

        for j in range(len(data["annotations"])):
        # print(data["annotations"][j]['image_id'])
            if ids == data["annotations"][j]['image_id']:
#                 print(type(data["annotations"][j]['bbox']),imge,data["annotations"][j]['bbox'])
                if data["annotations"][j]['bbox'][0] < 0 or data["annotations"][j]['bbox'][1] < 0 or data["annotations"][j]['bbox'][2] < 0 or data["annotations"][j]['bbox'][3] < 0:
                    pass
                else:
                    ann_list.append(data["annotations"][j])
               
       


# In[57]:


new ={}
new['annotations'] = ann_list
new['categories'] = data['categories']
new['images'] = image_list
new['info'] = data['categories']
new['licenses'] = data['categories']


# In[58]:


with open('Tracking-data/instances_train2017_split_track.json', 'w') as json_file:
    json.dump(new, json_file, sort_keys=True, indent=4)


# In[ ]:




4