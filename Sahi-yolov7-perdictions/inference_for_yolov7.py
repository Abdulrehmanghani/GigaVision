#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kadirnar/Yolov7-SAHI/blob/main/demo/inference_for_yolov7.ipynb)

# ## 0. Preperation

# - Install latest version of SAHI and Torch:

# - Import required modules:

# In[1]:


# arrange an instance segmentation model for test
from sahi.utils.yolov7 import download_yolov7_model
# import required functions, classes
from sahi.model import Yolov7DetectionModel
from sahi.predict import get_sliced_prediction, predict, get_prediction
from sahi.utils.file import download_from_url
from sahi.utils.cv import read_image
from IPython.display import Image


# In[2]:


# download yolov7 model to 'models/yolov7.pt'
yolov7_model_path = 'models/yolov7.pt'
download_yolov7_model(destination_path=yolov7_model_path)

# # download test images into demo_data folder
download_from_url('https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/small-vehicles1.jpeg', 'demo_data/small-vehicles1.jpeg')
download_from_url('https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/terrain2.png', 'demo_data/terrain2.png')


detection_model = Yolov7DetectionModel(
    model_path=yolov7_model_path,
    confidence_threshold=0.3,
    image_size=640,
    device="cuda:0", # or 'cuda:0'
)



import glob
import cv2
import json
import pandas as pd
csv_list =[]
ann_list =[]

data_csv = pd.read_csv("training_data.csv")

for image_name in glob.glob('train2017//*.jpg'):
    result  = get_prediction(image_name, detection_model)
    img = cv2.imread(image_name)
    
    data_id = data_csv[data_csv['Frame_Number']==image_name.split("17\\")[1]]
#     print(type(data_id['image id']),len(data_id['image id']))
    print(image_name.split("17\\")[1],data_id['image id'].unique().item())
    ids = data_id['image id'].unique().item()
    ann = result.to_coco_predictions(image_id=ids)
    
    for i in range(len(ann)):
        if ann[i]['category_name'] == 'person' or  ann[i]['category_name'] =='bicycle' or  ann[i]['category_name'] == 'car' or  ann[i]['category_name'] =='motorcycle' or  ann[i]['category_name'] == 'bus' or  ann[i]['category_name'] == 'truck':

            ann_list.append(ann[i])
        
    csv_list.extend(ann_list)

with open('data.json', 'w') as f:
    json.dump(csv_list, f, ensure_ascii=False)


# In[6]:

