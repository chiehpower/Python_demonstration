"""
Source from : https://juejin.cn/post/7016538643565117453
Mainly I was changing the loading library from PIL to cv2.
"""
#!/usr/bin/env python3
from typing import Tuple, NewType
import cv2
from sys import argv
from PIL import Image

Pixel = NewType("Pixel", Tuple[int, int, int, int])

CHARACTERS = (' ', '.', '°', '*', 'o', 'O', '#', '@')

MAX_CHANNEL_INTENSITY = 255
MAX_CHANNEL_VALUES = MAX_CHANNEL_INTENSITY * 4 # 4 is the number of channels of a Pixel

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASCII Art</title>
</head>
<body>
    <div style="background-color: black; color: white; line-height: 10px">
        <pre>{}</pre>
    </div>
</body>
</html>
"""


def map_intensity_to_character(intensity):
    return CHARACTERS[round(intensity * len(CHARACTERS))]


def get_pixel_intensity(pixel):
    return sum(pixel) / 1020 # 1020 = 255 * 4


def print_ascii_art(size, characters):
    index = 0
    for _ in range(size[1]):
        print(characters[index:index+size[0]])
        index += size[0]


def ascii_image_to_html(image_name, characters, size):
    with open(image_name + '.html', 'w') as image_file:
        ascii_image = ''    
        index = 0
        for _ in range(size[1]):
            ascii_image += characters[index:index+size[0]] + '\n'
            index += size[0]
        print(ascii_image)
        image_file.write(HTML_TEMPLATE.format(ascii_image))


def convert_image(image):
    ascii_string = ''
    for pixel in image.getdata():
        intensity = get_pixel_intensity(pixel)
        character = map_intensity_to_character(intensity)
        ascii_string += character
    return ascii_string


def art(image_name):

    image = Image.open(image_name)
    print("Origial image size :", image.size)
    width = 183
    ratio = int(image.size[1] * width / image.size[0])
    image = image.resize((width, ratio))

    print("After resize:", image.size, image.mode)

    ascii_image = convert_image(image)

    #print_ascii_art(image.size, ascii_image)

    ascii_image_to_html(image_name, ascii_image, image.size)

# def cv2_art(image_name):

#     image = cv2.imread(image_name)
#     print("Origial image size :", image.shape)
#     width = 183
#     ratio = int(image.shape[1] * width / image.shape[0])
#     image = image.reshape((width, ratio))

#     print("After reshape:", image.shape, image.mode)

#     ascii_image = convert_image(image)

#     #print_ascii_art(image.shape, ascii_image)

#     ascii_image_to_html(image_name, ascii_image, image.shape)


if __name__ == '__main__':

    image_name = 'image.jpg' 
    art(image_name)
    # cv2_art(image_name)

    print("Haven't done it yet...")