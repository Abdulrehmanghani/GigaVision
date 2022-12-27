#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
import pandas as pd
# Path of seqinfo.json directory
train_seq_1 = 'Tracking-data/01_University_Canteen/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/01_University_Canteen/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list =[]
f_id = 0
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
#                     print(trckdict[i]['frames'][j]['occlusion'])
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list.append(csv_dict)
    f_id = f_id+1         
        #                 frame_bbx.append(trckdict[i]['frames'][j]['rect'])    

csv_list=pd.DataFrame(csv_list)


# In[9]:


train_seq_1 = 'Tracking-data/02_OCT_Habour/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/02_OCT_Habour/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list1 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list1.append(csv_dict)
    f_id = f_id+1 
csv_list1=pd.DataFrame(csv_list1)


# In[10]:


train_seq_1 = 'Tracking-data/03_Xili_Crossroad/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/03_Xili_Crossroad/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list2 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list2.append(csv_dict)
    f_id = f_id+1 
csv_list2=pd.DataFrame(csv_list2)


# In[11]:


import json
# Path of seqinfo.json directory
train_seq_1 = 'Tracking-data/04_Primary_School/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/04_Primary_School/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list3 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list3.append(csv_dict) 
    f_id = f_id+1 
csv_list3=pd.DataFrame(csv_list3)


# In[12]:


train_seq_1 = 'Tracking-data/05_Basketball_Court/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/05_Basketball_Court/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list4 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list4.append(csv_dict)  
    f_id = f_id+1 
csv_list4=pd.DataFrame(csv_list4)


# In[13]:


train_seq_1 = 'Tracking-data/06_Xinzhongguan/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/06_Xinzhongguan/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list5 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list5.append(csv_dict)   
    f_id = f_id+1 
csv_list5=pd.DataFrame(csv_list5)


# In[14]:


train_seq_1 = 'Tracking-data/07_University_Campus/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/07_University_Campus/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list6 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list6.append(csv_dict)
    f_id = f_id+1 
csv_list6=pd.DataFrame(csv_list6)


# In[15]:


train_seq_1 = 'Tracking-data/08_Xili_Street_1/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/08_Xili_Street_1/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list7 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list7.append(csv_dict)  
    f_id = f_id+1 
csv_list7=pd.DataFrame(csv_list7)


# In[16]:


train_seq_1 = 'Tracking-data/09_Xili_Street_2/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/09_Xili_Street_2/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list8 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list8.append(csv_dict)   
    f_id = f_id+1 
csv_list8=pd.DataFrame(csv_list8)


# In[17]:


train_seq_1 = 'Tracking-data/10_Huaqiangbei/seqinfo.json'
# Path of track.json directory
train_track_1 = 'Tracking-data/10_Huaqiangbei/tracks.json' 
# Opening JSON file
with open(train_seq_1, 'r') as seq:
    seqdict = json.load(seq)
with open(train_track_1, 'r') as trck:
    trckdict = json.load(trck)
IDs = len(trckdict)
total_frames= len(seqdict['imUrls'])
csv_list9 =[]
f_id = f_id-1
for frame_no in range(total_frames):
    for i in range(IDs):
        ID_len = len(trckdict[i]['frames'])
        #print('Tracking ID number ',i+1, 'appears in ', ID_len, 'frames')
        for j in range(ID_len):
            if frame_no == trckdict[i]['frames'][j]['frame id']:
                if trckdict[i]['frames'][j]['occlusion'] == 'serious hide' or trckdict[i]['frames'][j]['occlusion'] == 'disappear' or trckdict[i]['frames'][j]['occlusion'] == 'hide':

                    pass
                else:
                    if trckdict[i]['frames'][j]['rect']['tl']['x'] < 0 or trckdict[i]['frames'][j]['rect']['tl']['y'] < 0 or trckdict[i]['frames'][j]['rect']['br']['x'] < 0 or trckdict[i]['frames'][j]['rect']['br']['y'] < 0:
                        pass
                    else:
                        csv_dict={}
                        csv_dict['Frame_Number']=seqdict['imUrls'][frame_no-1]
                        csv_dict['image id']= f_id
                        csv_dict['width']=seqdict['imWidth']
                        csv_dict['height']=seqdict['imHeight']
                        csv_dict['Class']= 'person'
                        csv_dict['xmin']=trckdict[i]['frames'][j]['rect']['tl']['x']
                        csv_dict['ymin']=trckdict[i]['frames'][j]['rect']['tl']['y']
                        csv_dict['xmax']=trckdict[i]['frames'][j]['rect']['br']['x']
                        csv_dict['ymax']=trckdict[i]['frames'][j]['rect']['br']['y']
                        csv_list9.append(csv_dict)  
    f_id = f_id+1 
csv_list9=pd.DataFrame(csv_list9)


# In[18]:


new = pd.concat([csv_list, csv_list1,csv_list2,csv_list3,csv_list4,csv_list5,csv_list6,csv_list7,csv_list8,csv_list9], axis=0)


# In[19]:


new.to_csv('Tracking-data/tracking_anntoations.csv',index=False)


# In[ ]:




