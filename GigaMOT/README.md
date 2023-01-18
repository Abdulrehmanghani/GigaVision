# GigaVision

## Training annotations to COCO
To convert the the giga detection training data annotations to the coco format follow these steps.
1. Create the csv from gigadetection  
2. Create the coco fomat json from the csv 
3. Visualization


## Tracking data to COCO 
To run the docker solution use the docker folder

To convert the the tracking data to the coco annotations format follow these steps.
1. Create the csv from tracking data  
2. Create the coco fomat json from the csv 
3. Visualization

### Create the csv from tracking data 
The csv file is created by the [selective_coco_annotations.ipynb](./selective_coco_annotations.ipynb) is contains the fields as disscused in the training annotaions data.

To run the [selective_coco_annotations.ipynb](./selective_coco_annotations.ipynb) please add the `</seqinfo.json/>` file and `</tracks.json/>` file. It will discard the data about the `</serious hide, and disappear/>` objects. Run this on all the tracking folders one by one. This notebook contains the 10 folders data.

### Create the coco fomat json from the csv 
To create the coco fomat json file from the csv file please use the [csv_to_json.py](./Tracker-data-to-coco/csv_to_json.py). The fomat of the json file will be as same as in the training annotations. Pass the new created csv file to convert it to the json.

### Visualization
To visualize the perpared csv and json please use the following code.

For visualization of the csv file on the traing images please use [csv_visualization.py](./Tracker-data-to-coco/csv_visualization.py) and add the `</Tracking data csv/>` file and `</Tracking images folder/>`.

For visualization of the json file on the traing images please use [json_visualization.py](./Tracker-data-to-coco/json_visualization.py) and add the `</Tracking data json/>` file and `</Tracking images folder/>`.
