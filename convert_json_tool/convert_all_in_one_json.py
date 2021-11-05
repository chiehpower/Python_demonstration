"""
Maintainer: Chieh
Date: 2021/11/05
"""

import os
import warnings
warnings.filterwarnings("ignore")
from os import listdir
import json
import shutil

class CocoDataset():
    def __init__(self, folder_path, real_name=False):
        """
        folder path
        """
        self.folder_path = folder_path
        self.real_name = real_name

    def generate_data_json(self, root_path=None):
        """
        Generate whole dataset image and each json to one json files. 
        """
        new_folder_path = os.path.join(self.folder_path, 'new_dataset')
        print(f">>> New Dataset path: {new_folder_path} \n")

        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path, exist_ok=True)

        total_files = listdir(os.path.join(self.folder_path))

        data = {}
        
        annotation_files = [os.path.join(self.folder_path, f) for f in total_files if f.split('.')[-1].lower() == 'json'] # get json file 
        for ann in annotation_files:
            img_ = ann.replace('json', 'jpg')
            try:
                if os.path.isfile(img_):
                    data[str(ann)] = img_
            except:
                print(f"{ann} cannot match the image.")
        
        assert len(data) > 0, "There is no any file inside."

        collect_classes = {}
        with open(os.path.join(os.path.abspath(self.folder_path), annotation_files[0]), 'r') as reader:
            jf = json.loads(reader.read())
            collect_classes['categories'] = jf['categories']

        num = 1
        data_counter = 1

        image_list = []
        annotation_list = []
        for tvt in annotation_files:
            print(f"---------------------------\nStatus: {tvt}\n")

            # copy image to new path and rename
            
            if self.real_name:
                image_name = os.path.basename(data[tvt])
                new_img_path = os.path.join(new_folder_path, image_name)
            else:
                img_format = data[tvt].split('.')[-1]
                new_img_path = os.path.join(new_folder_path, f"{int(data_counter):09d}" + '.' + img_format)
            print(f"Image name: {new_img_path}")
            shutil.copyfile(data[tvt], new_img_path)

            with open(tvt, 'r') as reader:
                jf = json.loads(reader.read())

            jf['images'][0]['id'] = jf['images'][0]['id'] + data_counter - 1 
            if not self.real_name:
                jf['images'][0]['file_name'] = f"{int(data_counter):09d}" + '.' + img_format
            
            for ii in range(len(jf['annotations'])):
                jf['annotations'][ii]['image_id'] = jf['images'][0]['id']
                jf['annotations'][ii]['id'] = num
                annotation_list.append(jf['annotations'][ii])
                num += 1 

            image_list.append(jf['images'][0])
            
            data_counter += 1

        collect_classes['images'] = image_list
        annotation_list = sorted(annotation_list, key=lambda x:x['id'])    
        collect_classes['annotations'] = annotation_list

        saving_coco_json = os.path.join(new_folder_path, 'coco.json')
        
        with open(saving_coco_json,'w') as f:
            print(f"\nFile saves to {saving_coco_json}")
            json.dump(collect_classes, f)


if __name__ == "__main__":

    folder_path = 'datasets'
    real_name = False
    dataset_ = CocoDataset(folder_path, real_name)
    dataset_.generate_data_json()
