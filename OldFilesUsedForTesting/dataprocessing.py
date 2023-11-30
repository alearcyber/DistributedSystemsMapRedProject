import cv2
import numpy as np
from skimage import segmentation, color
from sklearn.cluster import spectral_clustering
import matplotlib.pyplot as plt


BLUE = 'blue'
GREEN = 'green'
RED = 'red'

# these are the keys, in the final example, the entries would be the names of the preprocessing methods
PROCESSING_METHODS = [RED, GREEN, BLUE]




#averages pixel, make better comment her
def average_pixels(image_path, color):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # grab single color channel
    if color == BLUE:
        channel = 0
    elif color == GREEN:
        channel = 1
    elif color == RED:
        channel = 2
    else:
        raise Exception("Invalid color passed")

    mono_color_channel = img[:, :, channel]

    # Compute the average of the blue pixels
    total = np.sum(mono_color_channel)
    #total_pixels = np.count_nonzero(mono_color_channel)
    total_pixels = mono_color_channel.size
    average_color = total / total_pixels

    return average_color






####################################################################################
# Takes the weighted mean of two multisets. Formula => (n * x̄ + m * ȳ) / (n + m)
# x and y are the means.
# n is the size of x
# m is the size of y
####################################################################################
def weighted_mean(x, y, n, m):
    numerator = (n * x) + (y * m)
    denominator = n + m
    return numerator / denominator




####################################################################################
# TBD
# Segments iteratively until 2 segments are produced
# The exception below is produced when 2 segments cannot be produced. Ensure that
#  the calling function attempts to handle the failure.
####################################################################################
class BadNumberOfSegments(Exception):
    pass

def segment(image, max_segment_count_request=5):

    labels = None
    segments_produced = 0
    requested_segment_count = 1 # is incremented at start of iteration
    while segments_produced < 2:
        # increment for this iteration
        requested_segment_count += 1

        labels = segmentation.slic(image, compactness=30, n_segments=requested_segment_count, start_label=1,
                                   enforce_connectivity=True)
        segments_produced = len(np.unique(labels))

        # throw exception if we go past the cap
        if requested_segment_count > max_segment_count_request:
            raise BadNumberOfSegments(f"Only produced {segments_produced} segments, max_segment_count_request({max_segment_count_request}) exceeded.")


    #check to see if 2 segments where produced
    if segments_produced != 2:  # 2 was skipped over, throw exception
        raise BadNumberOfSegments(f"Skipped past 2 segments, produced{segments_produced}.")


    #we now guarantee to have 2 segments if we have reached this point in execution.
    out1 = color.label2rgb(labels, image, kind='avg', bg_label=0)
    print("Unique Labels:", np.unique(labels))
    plt.imshow(out1)
    plt.show()




####################################################################################
# PREPROCESSING METHODS HERE
####################################################################################


#REMEMBER TO HAVE CONTROL THAT JUST SEGMENTS WITHOUT PREPROCESSING





#Gaussian Blur, sigmax/y are calculated from the size of the kernel
def gaussian_blur5(image):
    return cv2.GaussianBlur(image, (5, 5), 0)



def gaussian_blur11(image):
    return cv2.GaussianBlur(image, (11, 11), 0)



def gaussian_blur15(image):
    return cv2.GaussianBlur(image, (15, 15), 0)


def gaussian_blur29(image):
    return cv2.GaussianBlur(image, (29, 29), 0)


def gaussian_blur45(image):
    return cv2.GaussianBlur(image, (45, 45), 0)









def main():
    img1 = cv2.imread("/Users/aidanlear/PycharmProjects/Workspace/mapreduce/imageset/test3/cam-low-exposure.png")
    segment(img1)

    segment(gaussian_blur5(img1))
    segment(gaussian_blur11(img1))
    segment(gaussian_blur15(img1))
    segment(gaussian_blur29(img1))
    segment(gaussian_blur45(img1))

if __name__ == "__main__":
    main()

