from kafka import KafkaProducer
import time
from datetime import datetime
import json
import base64
import io
from PIL import Image
"""
pip3 install Pillow
"""

a = time.time()
# server = '0.0.0.0:9092'  # From inside
server = '10.1.2.84:9093'  # From outside
producer = KafkaProducer(bootstrap_servers=[server])
print(f"producer take {time.time()-a}")

""" 
寫入的內容
1. created: 2023/12/01 16:30:50
2. user_name: test
3. project_name: db
4. class_ids: {0,0,0,0}
5. keypoints: {{{345,410}},{{1085,401}},{{253,410}},{{1000,403}}} 
6. rois: {{303,383,386,436},{1044,376,1127,427},{209,383,297,437},{956,377,1043,429}}
7. scores: {0.707822,0.6826631,0.68323976,0.67237455}
8. raw_img_path: /workspace/jobs/2023/12/01/h/db/677943_2535938_16-30-50/2535938.jpg     
9. img_result_path: /workspace/jobs/2023/12/01/h/db/677943_2535938_16-30-50/2535938_result.jpg
10. word: {""}
"""
start = time.time()

params = {
    "created": "2023-12-01 16:30:50",
    "user_name": "test",
    "project_name": "db",
    "class_ids": [0, 0, 0, 0],
    "keypoints": [[[345, 410]], [[1085, 401]], [[253, 410]], [[1000, 403]]],
    "rois": [[303, 383, 386, 436], [1044, 376, 1127, 427], [209, 383, 297, 437], [956, 377, 1043, 429]],
    "scores": [0.707822, 0.6826631, 0.68323976, 0.67237455],
    "raw_img_path": "/workspace/jobs/2023/12/01/test/db/677943_2535938_16-30-50/2535938.jpg",
    "img_result_path": "/workspace/jobs/2023/12/01/test/db/677943_2535938_16-30-50/2535938_result.jpg",
    "word": [""]
}

# Convert created to timestamp
# params["created"] = int(datetime.strptime(params["created"], "%Y-%m-%d %H:%M:%S").timestamp())

# Convert JSON to string
message = json.dumps(params)
print(f"Message: {message}")
print(f"Convert to json type taking {time.time() - start}")

for i in range(1):
    b = time.time()
    # message = f'my_value {i}: {b}'
    future = producer.send('baeldung_linux', key=b'my_key', value=bytes(message, 'utf-8'), partition=0)
    result = future.get(timeout=10)
    print(result)
    print(f"No.{i} take {time.time()-b}\n")
    time.sleep(0.5)



print("\nStart to send an image to Kafka...")
image_path = 'assets/test.jpeg'


# 读取图片并调整尺寸
with Image.open(image_path) as img:
    # 设置目标尺寸
    target_width = 400  
    target_height = 400
    # 调整图片尺寸
    resized_img = img.resize((target_width, target_height))
img.close()

resized_img.save('resized_image.jpg')
start = time.time()

# 可选：将调整后的图片数据读取到内存中
buffered = io.BytesIO()
resized_img.save(buffered, format="JPEG")
resized_image_data = buffered.getvalue()

print("Original Size:", img.size)
print("Resized Size:", resized_img.size)

future = producer.send('image_topic', value=resized_image_data)
result = future.get(timeout=10)
print(result)
print(f"Sending an image takes {time.time() - start}")

producer.close()