import pandas as pd
import os
import glob
import json
import numpy as np
import cv2
from natsort import natsorted
from PIL import Image
from pycocotools import mask as cocomask
from pycocotools import coco as cocoapi

soccer_coco={}
soccer_coco["info"] = {"year" : "2022",
                     "version" : "1.0",
                     "description" : "Soccer_coco",
                     "contributor" : "Abdul Rehman",
                     "url" : "",
                     "date_created" : "2022"
                    }
soccer_coco["licenses"] = [{"id": 1,
                  "name": "Attribution-NonCommercial",
                  "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
                 }]

soccer_coco["categories"] =[{'supercategory': 'person', 'id': 1, 'name': 'person'},
 {'supercategory': 'vehicle', 'id': 2, 'name': 'vehicle'}]
 

cat2id = {cat["name"]: catId+1 for catId, cat in enumerate(soccer_coco["categories"] )}
print(cat2id)


annot=pd.read_csv('selective_combined_training_data.csv')
print("Length of data:  ",len(annot.Frame_Number.unique()))

coco_images = []
annotations=[]
k=0
i=0
image_list=[]
for j in range(len(annot['Frame_Number'])):
    
    class_name=annot['Class'][j]

    height=int(annot['height'][j])
    width=int(annot['width'][j])
  
    xmin=int(annot['xmin'][j]*width)
    ymin=int(annot['ymin'][j]*height)
    xmax=int(annot['xmax'][j]*width)
    ymax=int(annot['ymax'][j]*height)
    w=xmax-xmin
    h=ymax-ymin
    
    area = int(w*h)

    if class_name=='person':
        class_name='person'
    if class_name=="small car" or class_name=="baby carriage" or class_name== "midsize car" or class_name== "large car" or class_name== "bicycle" or class_name== "motorcycle" or class_name== "tricycle" or class_name== "electric car":
        class_name='vehicle'

    if annot['Frame_Number'][j] in image_list:
    	pass
    else:
        image_list.append(annot['Frame_Number'][j])
        coco_images.append({"date_captured" : "2022",
                "file_name" : annot['Frame_Number'][j], 
                "id" : np.uint32(annot['image id'][j]).item(),
                "license" : 1,
                "url" : "",
                "height" : int(annot['height'][j]),
                "width" : int(annot['width'][j])})
            
        i=i+1
    annotations.append({"segmentation" : [],
                        "area" : np.float64(area),
                        "iscrowd" : 0,
                        "image_id" : np.uint32(annot['image id'][j]).item(),
                        "bbox" : [xmin,ymin,w,h],
                        "category_id" : cat2id[class_name],
                        "id": k+1})
    k=k+1

   
soccer_coco['images']=coco_images
soccer_coco['annotations']=annotations

with open('instances_train2017.json', 'w') as json_file:
    json.dump(soccer_coco, json_file, sort_keys=True, indent=4)

