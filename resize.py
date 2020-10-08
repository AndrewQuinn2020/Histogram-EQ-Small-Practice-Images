#!/usr/bin/python3

 # Anything not directly related to processing here
from mp3_helper import *

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path


np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=1000)


scale = 50

if __name__ == "__main__":
    hello()

    for image in test_images:
        if "hist" in image:
            print("SKIP")
            continue
        print(image)
        im = Image.open(image)
        big_im = im.resize((round(im.size[0]*scale), round(im.size[1]*scale)))
        big_im_path = os.path.join(big_test_images_dir, Path(image).stem + ".bmp")
        print(big_im_path)
        big_im.save(big_im_path)
        big_im_path = os.path.join(big_test_images_dir, Path(image).stem + ".png")
        print(big_im_path)
        big_im.save(big_im_path)

    for image in test_results:
        if "hist" in image:
            print("SKIP")
            continue
        print(image)
        im = Image.open(image)
        big_im = im.resize((round(im.size[0]*scale), round(im.size[1]*scale)), resample=Image.NEAREST)
        big_im_path = os.path.join(big_test_results_dir, Path(image).stem + ".bmp")
        print(big_im_path)
        big_im.save(big_im_path)
        big_im_path = os.path.join(big_test_results_dir, Path(image).stem + ".png")
        print(big_im_path)
        big_im.save(big_im_path)
