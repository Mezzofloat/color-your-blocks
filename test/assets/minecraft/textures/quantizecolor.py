from sklearn.cluster import MeanShift, estimate_bandwidth
from pathlib import Path
from PIL import Image
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
    sum = (0,0,0,0)
    for i in range(l):
        sum += i

    return sum / l if l != 0 else sum

def handleMeanShift(meanShifted, imagePath):
    pass

for file in Path('test').rglob("*.png"):
#    meanShift(file)
    pass

path = Path("block\\bricks.png")

test = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGBA)
height, width, _ = np.shape(test)
flat_test = np.reshape(test, (-1,4))
for pixel in flat_test:
    pixel = RGBToOKLAB(pixel)

bandwidth = estimate_bandwidth(flat_test, quantile=0.25)

m = MeanShift(bandwidth=bandwidth)
m.fit(flat_test)
labels = m.labels_

un = np.unique(labels)

segmented_colors = []
for label in un:
    for i in len(flat_test):
        pixel = flat_test[i]
        i_colors = []
        if (labels[i] == label):
            i_colors.append(pixel)

labels = np.reshape(labels, (height, width))

colored_segmented_image = np.uint8(segmented_colors[labels])
test = cv2.cvtColor(test, cv2.COLOR_RGBA2BGR)

test = cv2.resize(test, (width * 15, height * 15), interpolation=cv2.INTER_NEAREST)
colored_segmented_image = cv2.resize(colored_segmented_image, (width * 10, height * 10), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Original", test)
cv2.imshow("Segmented", colored_segmented_image)
cv2.waitKey(0)

# take an image and segment it
# do it to all images

# image_path = "C:/Users/skull/Documents/color-your-blocks/test/assets/minecraft/textures/tumblr_8e62b2cb31fbb752647650f0191ee12a_c83283a0_1280.webp"
# image = cv2.imread(image_path)

# Check if the image was loaded successfully
# if image is None:
#     print(f"Error: Unable to load image at {image_path}")
# else:
    # Convert the image to RGB
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)

# flat_image = lab_image.reshape((-1, 3))

# height, width, _ = image.shape
# x, y = np.meshgrid(np.arange(width), np.arange(height))
# flat_image_with_coordinates = np.column_stack([flat_image, x.flatten(), y.flatten()])

# Estimate bandwidth for Mean Shift
# bandwidth = estimate_bandwidth(flat_image_with_coordinates, quantile=0.2, n_samples=500)

# Perform Mean Shift clustering
# mean_shift = MeanShift(bandwidth=bandwidth, bin_seeding=True)
# mean_shift.fit(flat_image_with_coordinates)
# labels = mean_shift.labels_

# Reshape the labels to the original image shape
# segmented_image = labels.reshape((height, width))

# Generate a colored segmented image
# unique_labels = np.unique(labels)
# segmented_colors = np.random.randint(0, 255, size=(len(unique_labels), 3))
# colored_segmented_image = segmented_colors[segmented_image]