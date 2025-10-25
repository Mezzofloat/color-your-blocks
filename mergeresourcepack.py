from pathlib import Path
from PIL import Image
import sys

# define minecraft colors
minecraftcolors = {
    "White": (207, 213, 214, 255),
    "Light Gray": (135, 135, 135, 255),
    "Gray": (62, 68, 71, 255),
    "Black": (21, 21, 26, 255),
    "Red": (142, 33, 32, 255),
    "Orange": (224, 97, 0, 255),
    "Yellow": (240, 175, 21, 255),
    "Lime": (94, 168, 24, 255),
    "Green": (73, 91, 36, 255),
    "Cyan": (22, 156, 156, 255),
    "Light Blue": (58, 179, 218, 255),
    "Blue": (61, 74, 176, 255),
    "Purple": (137, 50, 184, 255),
    "Magenta": (190, 68, 179, 255),
    "Pink": (237, 141, 172, 255),
    "Brown": (96, 60, 32, 255)
}

# define needed paths
full_pack_path = Path("full")
resource_pack_path = Path("color-your-blocks")
mask_pack_path = Path("masks")
test_image_path = Path("test\\assets\\minecraft\\textures\\tumblr_8e62b2cb31fbb752647650f0191ee12a_c83283a0_1280.webp")

# iterate over every image
# each pixel should be the previous + the new
# merge into a new resource pack
def merge_image(input_path: str, color: str):
    mask_path = ""
    full_path = ""

    image = Image.open(input_path).convert("RGBA").load()
    mask = Image.open(mask_path).convert("RGBA").load()
    full = Image.open(full_path).convert("RGBA").load()
    width, height = image.size

    pixelAlphas = image.getchannel("A").load()

    for i in range(width):
        for j in range(height):
            if pixelAlphas[i, j] != 0 and mask[i, j] == minecraftcolors[color]:
                image[i, j] = full[i, j]

# for path, _, files in os.walk(input_path):
#     for file in files:
#         if (os.path.splitext(file)[1] == ".png"):
#             merge_image(f"{path}/{file}")

# use this function, it is the better one
# for file in resource_pack_path.rglob('**/*.png'):
#     pass

# rename the new resource pack to [previous]+[new]
print(Image.open(test_image_path).convert("RGBA").load()[0,0])