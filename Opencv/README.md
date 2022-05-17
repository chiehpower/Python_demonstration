# Demonstrate how to use OpenCV to draw the class name with background

Mainly the hard part in here is how to get the word size from putText?

We will use the `cv2.getTextSize` to get the text size. 

Here is the result below:

| Before           | After           |
| ---------------- | --------------- |
| ![](example.jpg) | ![](result.jpg) |


---

# Demonstrate how to use OpenCV to check whether an image belongs to blur detetion or not.

Here is the code: [blur_detection_checking.py](./blur_detection_checking.py)

### Usage:

```
python3 blur_detection_checking.py --image cat.png -t 0.5  
```