from collections import Counter
import math
import itertools
import matplotlib.patches as patches
import time
import random
import io

MATCH = "satvikrn"

def optimized_srinivas_number(counts):
       # S  A  T  V  I  K  R  N
    s = [3, 2, 1, 2, 3, 1, 1, 1]
    res = 1 # srinivas constant
    i = 0
    for a in counts:
        res *= math.perm(a, s[i])
        i += 1
    return int(res)


def srinivas_number(text: str) -> int:
    SRINIVAS_NUMBER = 1
    text_counter = dict(Counter(text.lower().strip()))
    satvik_letter_counter  = {"s": text_counter["s"], "a": text_counter["a"], "t": text_counter["t"], "v": text_counter["v"], "i": text_counter["i"], "k": text_counter["k"], "r": text_counter["r"], "n": text_counter["n"]}   
    # print(satvik_letter_counter)
    satvik_spaces_counter = {"s": 3, "a": 2, "t": 1, "v": 2, "i": 3, "k": 1, "r": 1, "n": 1}
    # print(satvik_spaces_counter)
    for letter in MATCH:
        # print('n', satvik_letter_counter[letter], 'k', satvik_spaces_counter[letter])
        combinations = (math.factorial(
            satvik_letter_counter[letter]))//(math.factorial(satvik_letter_counter[letter]-satvik_spaces_counter[letter])
        )
        # print(combinations)
        SRINIVAS_NUMBER *= combinations

    if SRINIVAS_NUMBER < 0:
        return 0
    else:
        return int(SRINIVAS_NUMBER)

def optimized_io(fileName: str):

    counts = [0]*8
    with io.open(fileName, 'r', buffering=8192) as file:
        for c in file.read():
            match c:
                case 's':
                    counts[0] += 1
                case 'a':
                    counts[1] += 1
                case 't':
                    counts[2] += 1
                case 'v':
                    counts[3] += 1
                case 'i':
                    counts[4] += 1
                case 'k':
                    counts[5] += 1
                case 'r':
                    counts[6] += 1
                case 'n':
                    counts[7] += 1
                case _:
                    continue
    
    return counts


def srinivas_combinations(input_text) -> list:
    letter_indexes = {"s": [], "a": [], "t": [], "v": [], "i": [], "k": [], "r": [], "n": []}
    for index, letter in enumerate(input_text):
        try:
            letter_indexes[letter].append(index)
        except:
            continue # letter not in satvikrn
        
    count = 0
    def backtrack(combination, used_indexes, depth):
        if depth == len(letters):
            combinations.append(combination[:])
            return
        
        current_letter = letters[depth]
        for index in letter_indexes[current_letter]:
            if index not in used_indexes:
                combination.append(index)
                used_indexes.add(index)
                backtrack(combination, used_indexes, depth + 1)
                combination.pop()
                used_indexes.remove(index)

    letters = ['s', 'a', 't', 'v', 'i', 'k', 's', 'r', 'i', 'n', 'i', 'v', 'a', 's']
    combinations = []
    backtrack([], set(), 0)

    return combinations


import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot(data: list, colormap='viridis'):
    m = max(map(max, data))
    fig, ax = plt.subplots()
    for i, array in enumerate(data):
        for j, value in enumerate(array):
            color = plt.get_cmap(colormap)(value / m)
            rect = patches.Rectangle((j, i), 1, 1, linewidth=0, edgecolor=None, facecolor=color)
            ax.add_patch(rect)

    # Set the custom labels for the x-axis
    labels = ["S", "A", "T", "V", "I", "K", "S", "R", "I", "N", "I", "V", "A", "S"]
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)

    plt.xlim(0, 14)
    plt.ylim(0, len(data))
    plt.gca().invert_yaxis()
    plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

def heatmap(data):
    plt.figure(figsize=(10, 8))
    labels = ["S", "A", "T", "V", "I", "K", "S", "R", "I", "N", "I", "V", "A", "S"]
    sns.heatmap(data, cmap='viridis', xticklabels=labels, yticklabels=False)
    plt.show()
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
def line_plot(data):
    plt.figure()
    for row in data:
        plt.plot(row, marker='o')
    labels = ["S", "A", "T", "V", "I", "K", "S", "R", "I", "N", "I", "V", "A", "S"]
    plt.xticks(range(len(labels)), labels)
    plt.show()



if __name__ == '__main__':
    # input_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut laborek et dolorev magna aliqua. Ut enim ad minim ve'''
    # input_text = '''Lorem ipsum kdolor sit amet, consectetur adipiscking elit. Vivamus lacinia odio vitae vestikbulum vestibulum. Cras venenatis euismkod malesuada. Nullam ac erat kante. Proin ac libero non nisi consequat bibendum. Maecenas non nisi ut magna maleksuada facilisis. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed niksi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praeskent mauris. Fusce nec telklus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nkulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptkos himenaeos. Curabitkur sodales ligula in libero. Sed dignissim lacinia nuknc. Curabitur tortor. Pellentesque nibh. Aenkean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tkristique sem. Proin ut ligula vel nunc egestas porkttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus nkon, massa. Fusce ac turpis quis ligukla lacinia aliquet'''
    # input_text = "abcdefghijlkmnopqrstuvwxyzabcdefghijlkmnopqrstuvwxyzabcdefghijlkmnopqrstuvwxyz"
    # input_text = "satviksrinivas"

    # input_text = "satviksrinivas"
    # combinations = srinivas_combinations(input_text)
    # # for x in combinations:
    # #     print(x)
    # print("SRINIVAS NUMBER:", srinivas_number(input_text))
    print("OPTIMIZED SRINIVAS NUMBER:", optimized_srinivas_number(optimized_io("words.txt")))
    # print("OPTICAL SRINIVAS NUMBER", optimized_srinivas_number([63498, 41023, 65835, 71302, 28258, 62139, 77195, 51653]))
# 
    # start_time = time.time()

    # x=srinivas_number(input_text)
    # N=int(pow(10,1000000))
    # y=optimized_srinivas_number([x * N for x in [4,2,3,2,4,2,2,2]])

    # line_plot(combinations)
    # end_time = time.time()

    # execution_time = end_time - start_time
    # print(f"Execution time: {execution_time} seconds\n\n")
    # print(x)
    # print(y)
    
    # plot(combinations, colormap='gist_earth')
