# Gigadetections
To convert the the giga detection training data annotations to the coco format follow these steps.
1. Create the csv from gigadetection  
2. Create the coco fomat json from the csv 
3. Visualization

## Create the csv from gigadetection 
The csv file is created by the [coco_data_prep.ipynb](./Train-annotations-to-coco/coco_data_prep.ipynb) is contains the following fields.

*   Frame_Number	
*   image id	
*   width	
*   height	
*   Class	
*   xmin
*   ymin
*   xmax
*   ymax

To run the [coco_data_prep.ipynb](./Train-annotations-to-coco/coco_data_prep.ipynb) please add the `</person training annotation/>` file and `</vehicle training annotation/>` file. It will discard the data about the `</vehicles, fake, unsure and ignore/>` objects.

## Create the coco fomat json from the csv 
To create the coco fomat json file from the csv file please use the [csv_to_json.py](./Train-annotations-to-coco/csv_to_json.py). The fomat of the json file will be as following.

```json
{
    "annotations": [
        {
            "area": "Area of the bbox",
            "bbox": "[ xmin, ymin, bbox_width,  bbox_hight ]",
            "category_id": "Id of the class from the classes list",
            "id": "Id of the annotated box"  ,
            "image_id": "id of the image",
            "iscrowd": ,
            "segmentation": []
        }],
       "categories": [
        {
            "id": 1,
            "name": "person",
            "supercategory": "person"
        },
        {
            "id": 2,
            "name": "vehicle",
            "supercategory": "vehicle"
        }  ], 
    "images": [
        {
            "date_captured": "2022",
            "file_name": "name of image file",
            "height": "height of the image",
            "id": "id of the image",
            "license": 1,
            "url": "",
            "width": "width of the image"
        }]
```

To run the [csv_to_json.py](./Train-annotations-to-coco/csv_to_json.py) please add the `</Training data csv/>` file.

## Visualization
To visualize the perpared csv and json please use the following code.

For visualization of the csv file on the traing images please use [csv_visualization.py](./Train-annotations-to-coco/csv_visualization.py) and add the `</Training data csv/>` file and `</Training images folder/>`.

For visualization of the json file on the traing images please use [json_visualization.py](./Train-annotations-to-coco/json_visualization.py) and add the `</Training data json/>` file and `</Training images folder/>`.

