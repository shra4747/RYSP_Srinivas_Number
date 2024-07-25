from PIL import Image
import numpy as np
from collections import Counter

def number_to_letter(number):
    return chr(number + ord('a'))

# Grayscale​  = 0.299×r+0.587×g+0.114×b
def grayscale(rgb_arr: list) -> float:
    return 0.333 * rgb_arr[0] + 0.333 * rgb_arr[1] + 0.333 * rgb_arr[2]

def normalize(grayscale_value) -> int:
    return round(grayscale_value / 255 * 25)

image_path = 'images/spectrum.png'
image = Image.open(image_path)
image = image.convert('RGB')
pixel_array = np.array(image)
np.set_printoptions(threshold=np.inf)   

for row_index in range(pixel_array.shape[0]):
    for pixel_index in range(pixel_array.shape[1]):
        letter = str(number_to_letter(normalize(grayscale(pixel_array[row_index, pixel_index])))).lower()

        isSatvikLetter = True
        if letter in ['k']:
            pass
        else:
            pixel_array[row_index, pixel_index] = [255,255,255]


modified_image = Image.fromarray(pixel_array)
modified_image.save('images/only_k_spectrum.png')