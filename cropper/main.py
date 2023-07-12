import cv2


def cropper(image, coordinates):
    cropped_images = []
    for coord in coordinates:
        x1, y1, x2, y2 = coord
        cropped = image[y1:y2, x1:x2]
        cropped_images.append(cropped)

    return cropped_images


if __name__ == '__main__':

    image_path = './input.jpg'
    image = cv2.imread(image_path)
    coordinates = [[1769, 147, 2919, 1277], [1009, 933, 3813, 2450]]

    cropped_images = cropper(image, coordinates)
    for i, cropped in enumerate(cropped_images):
        cv2.imwrite(f"{i+1}.jpg", cropped)
