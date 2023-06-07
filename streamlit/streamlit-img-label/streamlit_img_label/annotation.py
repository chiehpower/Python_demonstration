import os
from pycocotools.coco import COCO
import json

def read_json(img_file):
    file_name = img_file.split(".")[0] + '.json'
    if not os.path.isfile(file_name):
        return []
    print(f"Load the json file: {file_name}")
    with open(file_name, 'r') as f:
        file_info = json.load(f)

    rects = []

    label = file_info['categories'][0]['name']
    obj_info = file_info['annotations']
    for obj in obj_info:    
        bbox = obj['bbox']
        x = int(bbox[0])
        y = int(bbox[1])
        w = int(bbox[2])
        h = int(bbox[3])
        rects.append(
            {
                "left": x,
                "top": y,
                "width": w,
                "height": h,
                "label": label,
            }
        )
    return rects


def output_json(img_file, img, rects):
    coco = COCO()
    width, height = img.size

    # add the info of the image
    image_info = {
        'id': 1,
        'width': width,
        'height': height,
        'file_name': img_file
    }

    category_info = {
    'id': 1,
    'name': '',
    'supercategory': 'animal'
    }
    
    coco.dataset = {
        'images': [],
        'annotations': [],
        'categories': []
    }
    coco.createIndex()
    coco.dataset['images'].append(image_info)
    coco.dataset['categories'].append(category_info)  

    # add the annotation info
    number = 1
    for box in rects:
        xmin = box["left"]
        ymin = box["top"]
        # xmax = box["left"] + box["width"]
        # ymax = box["top"] + box["height"]
        
        box_info = {
        'id': number,
        'image_id': 1,
        'category_id': 1,
        'bbox': [xmin, ymin, box["width"], box["height"]],  # [x, y, width, height]
        'segmentation': [],
        'area': -1,  
        'iscrowd': 0,  
        }
        coco.dataset['annotations'].append(box_info)
        number += 1

    # write into COCO file
    output_file = img_file.split(".")[0] + '.json'
    print(output_file)

    with open(output_file, 'w') as f:
        json.dump(coco.dataset, f)
