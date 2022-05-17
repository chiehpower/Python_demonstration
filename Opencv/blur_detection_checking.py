"""
Reference: https://pyimagesearch.com/2015/09/07/blur-detection-with-opencv/
"""
import cv2
import argparse

# import the necessary packages


def variance_of_laplacian(image, threshold):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    fm = cv2.Laplacian(image, cv2.CV_64F).var()
    print(fm)
    fm *= 0.01

    blur = False
    if fm < threshold:
        blur = True

    return fm, blur


if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--images", required=True,
                    help="path to input image")
    ap.add_argument("-t", "--threshold", type=float, default=0.5,
                    help="focus measures that fall below this value will be considered 'blurry'")
    args = vars(ap.parse_args())


    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    # method
    image = cv2.imread(args["images"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm, blur = variance_of_laplacian(gray, args["threshold"])
    text = "Not Blurry"
    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if blur:
        text = "Blurry"
    # show the image
    cv2.putText(image, "{}: {:.2f}% ".format(text, fm*100), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

    filename = 'savedImage.jpg'
    print(filename)
    cv2.imwrite(filename, image)
