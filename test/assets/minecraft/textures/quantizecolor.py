from PIL import Image
import os

minecraftcolors = {
    "White": (207, 213, 214),
    "Light Gray": (135, 135, 135),
    "Gray": (62, 68, 71),
    "Black": (21, 21, 26),
    "Red": (142, 33, 32),
    "Orange": (224, 97, 0),
    "Yellow": (240, 175, 21),
    "Lime": (94, 168, 24),
    "Green": (73, 91, 36),
    "Cyan": (22, 156, 156),
    "Light Blue": (58, 179, 218),
    "Blue": (61, 74, 176),
    "Purple": (137, 50, 184),
    "Magenta": (190, 68, 179),
    "Pink": (237, 141, 172),
    "Brown": (96, 60, 32)
}

def closest_color(rgb_tuple: tuple[int, int, int, int]):
    r, g, b, a = rgb_tuple
    color_diffs = []
    for color in minecraftcolors:
        cr, cg, cb = minecraftcolors[color]
        color_diff = (r - cr)**2 + (g - cg)**2 + (b - cb)**2
        color_diffs.append((color_diff, color))
    return minecraftcolors[min(color_diffs)[1]]

def convert_image(input_path: str):
    image = Image.open(input_path).convert("RGBA")
    width, height = image.size
    pixels = image.load()
    alphaPixels = image.getchannel("A").load()

    for i in range(width):
        for j in range(height):
            if (alphaPixels[i, j] != 0):
                pixels[i, j] = closest_color(pixels[i, j])

    image.save(input_path)

def convert_images_in_folder(input_path):
    for path, folders, files in os.walk(input_path):
        pass

convert_image("block/furnace_front_on.png")