from kafka import KafkaProducer
import time
from datetime import datetime
import json

a = time.time()
producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
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
