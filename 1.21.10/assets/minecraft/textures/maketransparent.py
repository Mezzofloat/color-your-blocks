from pathlib import Path
from PIL import Image

def transparify(image_path):
    im = Image.open(image_path).convert("RGBA")
    width, height = im.size

    pixels = im.load()

    for i in range(width):
        for j in range(height):
            if (pixels[i,j][0] == 0 and pixels[i,j][1] == 0 and pixels[i,j][2] == 0):
                pixels[i,j] = (0,0,0,0)

    im.save(image_path)

for path in Path("../textures").rglob("*.png"):
    transparify(path)