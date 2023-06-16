
import onnx
import os
import io
from io import BytesIO
import base64
from PIL import Image

onnx_model_path = 'model.onnx'
if not os.path.exists(onnx_model_path): 
    print('Cannot find the model.')
    raise

model_onnx = onnx.load(onnx_model_path)    
for metadata in model_onnx.metadata_props:
    if metadata.key == 'image':
        img_data = base64.b64decode(metadata.value)
        img_conv = BytesIO(img_data)
        file_name_ = 'test.png'
        audio_file = Image.open(img_conv)
        img_byte_arr = io.BytesIO()
        audio_file.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        with open(file_name_,'wb') as out: 
            out.write(img_byte_arr)
        print(f"Save the {file_name_}")
