from pathlib import Path
from PIL import Image
from argparse import ArgumentParser

# define minecraft colors
minecraftcolors = {
    "white": (207, 213, 214, 255),
    "light-gray": (135, 135, 135, 255),
    "gray": (62, 68, 71, 255),
    "black": (21, 21, 26, 255),
    "red": (142, 33, 32, 255),
    "orange": (224, 97, 0, 255),
    "yellow": (240, 175, 21, 255),
    "lime": (94, 168, 24, 255),
    "green": (73, 91, 36, 255),
    "cyan": (22, 156, 156, 255),
    "light-blue": (58, 179, 218, 255),
    "blue": (61, 74, 176, 255),
    "purple": (137, 50, 184, 255),
    "magenta": (190, 68, 179, 255),
    "pink": (237, 141, 172, 255),
    "brown": (96, 60, 32, 255)
}

# define needed paths
full_pack_path = Path("full")
resource_pack_path = Path("color-your-blocks")
mask_pack_path = Path("masks")
test_image_path = Path("test\\assets\\minecraft\\textures\\tumblr_8e62b2cb31fbb752647650f0191ee12a_c83283a0_1280.webp")

all_white_path = Path("white (original) a@4fd$")

# iterate over every image
# each pixel should be the previous + the new
# merge into a new resource pack
def merge_image(input_path: Path, color: str):
    mask_path = mask_pack_path / input_path.relative_to(resource_pack_path)
    full_path = full_pack_path / input_path.relative_to(resource_pack_path)

    inputImage = Image.open(input_path).convert("RGBA")

    image = inputImage.load()
    mask = Image.open(mask_path).convert("RGBA").load()
    full = Image.open(full_path).convert("RGBA").load()
    width, height = inputImage.size

    pixelAlphas = inputImage.getchannel("A").load()

    for i in range(width):
        for j in range(height):
            if pixelAlphas[i, j] != 0 and mask[i, j] == minecraftcolors[color]:
                image[i, j] = full[i, j]

    inputImage.save(input_path)

def restart(input_path: Path):
    whitePath = all_white_path / input_path.relative_to(resource_pack_path)
    white = Image.open(whitePath).convert("RGBA").load()

    inputImage = Image.open(input_path).convert("RGBA")
    image = inputImage.load()
    width, height = inputImage.size

    for i in range(width):
        for j in range(height):
            image[i,j] = white[i,j]

    inputImage.save(input_path)

# for path, _, files in os.walk(input_path):
#     for file in files:
#         if (os.path.splitext(file)[1] == ".png"):
#             merge_image(f"{path}/{file}")

# use this function, it is the better one
# for file in resource_pack_path.rglob('**/*.png'):
#     pass

# rename the new resource pack to [previous]+[new]

parser = ArgumentParser()

parser.add_argument('--add-color', '-c', choices=[
    'white',
    'light-gray',
    'gray',
    'black',
    'red',
    'orange',
    'yellow',
    'green',
    'lime',
    'blue',
    'light-blue',
    'cyan',
    'purple',
    'pink',
    'magenta',
    'brown'
])
parser.add_argument('--restart', action='store_true')

args = parser.parse_args()

if args.restart:
    for file in resource_pack_path.rglob('*.png'):
        print(file)
        restart(file)
else:
    for file in resource_pack_path.rglob('*.png'):
        print(file)
        merge_image(file, args.add_color)