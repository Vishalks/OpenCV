# USAGE
# python stitch.py --left left.png --right right.png 

from pyimagesearch.panorama import Stitcher
import argparse
import imutils
import cv2

# Parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--left", required=True,
	help="path to the first image")
ap.add_argument("-s", "--right", required=True,
	help="path to the second image")
args = vars(ap.parse_args())

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(args["left"])
imageB = cv2.imread(args["right"])
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.imwrite("result.jpg", result)
cv2.waitKey(0)
