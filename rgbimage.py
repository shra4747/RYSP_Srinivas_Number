from PIL import Image
import numpy as np
from collections import Counter
import math
def number_to_letter(number):
    return chr(number + ord('a'))

# Grayscale​  = 0.299×r+0.587×g+0.114×b
def grayscale(rgb_arr: list) -> float:
    return 0.299 * rgb_arr[0] + 0.587 * rgb_arr[1] + 0.114 * rgb_arr[2]

def normalize(grayscale_value) -> int:
    return round(grayscale_value / 255 * 25)
fileName = input("image file name: ")
image_path = f'images/{fileName}.png'
image = Image.open(image_path)
image = image.convert('RGB')
pixel_array = np.array(image)
np.set_printoptions(threshold=np.inf)

counts = [0]*8
for row_index in range(pixel_array.shape[0]):
    for pixel_index in range(pixel_array.shape[1]):
        letter = str(number_to_letter(normalize(grayscale(pixel_array[row_index, pixel_index])))).lower()

        isSatvikLetter = True
        match letter:
            case 's':
                counts[0] += 1
                pixel_array[row_index, pixel_index] = [173, 47, 47]
            case 'a':
                counts[1] += 1
                pixel_array[row_index, pixel_index] = [59, 47, 173]
            case 't':
                counts[2] += 1
                pixel_array[row_index, pixel_index] = [59, 173, 47]
            case 'v':
                counts[3] += 1
                pixel_array[row_index, pixel_index] = [173, 106, 47]
            case 'i':
                counts[4] += 1
                pixel_array[row_index, pixel_index] = [173, 47, 173]
            case 'k':
                counts[5] += 1
                pixel_array[row_index, pixel_index] = [47, 173, 165]
            case 'r':
                counts[6] += 1
                pixel_array[row_index, pixel_index] = [173, 47, 47]
            case 'n':
                counts[7] += 1
                pixel_array[row_index, pixel_index] = [47, 173, 165]
            case _:
                isSatvikLetter = False
                continue
        if isSatvikLetter:
            pixel_array[row_index, pixel_index] = [0,0,0]

print(counts)
def optimized_srinivas_number(counts):
       # S  A  T  V  I  K  R  N
    s = [3, 2, 1, 2, 3, 1, 1, 1]
    res = 1 # srinivas constant
    i = 0
    for a in counts:
        res *= math.perm(a, s[i])
        i += 1
    return int(res)


modified_image = Image.fromarray(pixel_array)
if input("save modified image? (y/n): ").lower() == "y":
    modified_image.save(f'images/modified_{fileName}.png')
modified_image.show()
print(f"OPTICAL SRINIVAS NUMBER for {fileName}.png:", optimized_srinivas_number(counts))