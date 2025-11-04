from sklearn.cluster import MeanShift, estimate_bandwidth
from pathlib import Path
#from PIL import Image
import numpy as np
import cv2

def RGBToOKLAB(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    a = pixel[3]

    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b

    l_ = l ** (1/3)
    m_ = m ** (1/3)
    s_ = s ** (1/3)

    oklabl = 0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*s_
    oklaba = 1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*s_
    oklabb = 0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*s_

    return (oklabl, oklaba, oklabb, a)

def OKLABToRGB(pixel):
    oklabl = pixel[0]
    oklaba = pixel[1]
    oklabb = pixel[2]
    a = pixel[3]

    l_ = oklabl + 0.3963377774 * oklaba + 0.2158037573 * oklabb
    m_ = oklabl - 0.1055613458 * oklaba - 0.0638541728 * oklabb
    s_ = oklabl - 0.0894841775 * oklaba - 1.2914855480 * oklabb

    l = l_ * l_ * l_
    m = m_ * m_ * m_
    s = s_ * s_ * s_

    return (
		int(+4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s),
		int(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s),
		int(-0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s),
        a
    )

def meanShift(imagePath: str, bandwidth):
    pass

def avg(list):
    l = len(list)
    if (l == 0):
        return (0,0,0,0)
    else:
        return tuple([sum(x)/len(x) for x in zip(*list)])

def handleMeanShift(meanShifted, imagePath):
    pass

for file in Path('test').rglob("*.png"):
#    meanShift(file)
    pass

path = Path("block\\bricks.png")

test = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGBA)
height, width, _ = np.shape(test)
flat_test = np.reshape(test, (-1,4))
flat_test = np.apply_along_axis(RGBToOKLAB, axis=1, arr=flat_test)

bandwidth = estimate_bandwidth(flat_test, quantile=0.21)

m = MeanShift(bandwidth=bandwidth)
m.fit(flat_test)
labels = m.labels_

un = np.unique(labels)
segmented_colors = []
for label in un:
    i_colors=[]
    for i in range(len(flat_test)):
        pixel = flat_test[i]
        if (labels[i] == label):
            i_colors.append(pixel)
    average = avg(i_colors)
    rgb = OKLABToRGB(average)
    segmented_colors.append(rgb)

labels = np.reshape(labels, (height, width))

colored_segmented_image = np.uint8(np.array(segmented_colors)[labels])

test = cv2.cvtColor(test, cv2.COLOR_RGBA2BGR)
colored_segmented_image = cv2.cvtColor(colored_segmented_image, cv2.COLOR_RGBA2BGR)

test = cv2.resize(test, (width * 15, height * 15), interpolation=cv2.INTER_NEAREST)
colored_segmented_image = cv2.resize(colored_segmented_image, (width * 15, height * 15), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Original", test)
cv2.imshow("Segmented", colored_segmented_image)
cv2.waitKey(0)