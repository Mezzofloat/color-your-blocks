from pathlib import Path
from PIL import Image

textures = Path("textures")

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
    "Brown": (96, 60, 32, 255),
    "Blank": (0, 0, 0, 0)
}

def checkPixels(pixels, width, height):
    for i in range(width):
        for j in range(height):
            if (pixels[i,j] not in minecraftcolors.values()):
                return (i,j)
            
    return None

def checkwork(image_path):
    im = Image.open(image_path).convert("RGBA")
    width, height = im.size

    pixels = im.load()

    k = checkPixels(pixels, width, height)
    if (k):
        print(f"{image_path}: {k}")

for file in Path("textures/block").rglob("*.png"):
    checkwork(file)

input("Press any key to exit:")