from PIL import Image
from pprint import pprint as pp
from random import random

# test shuffle
DEBUG = False

# img folder
DIR_INPUT = './traits'
DIR_OUTPUT = './assets'

# trait config
LAYER_0 = [
    ("1_1.png", 1.0),
    ("1_2.png", 0.3),
]
LAYER_1 = [
    ("2_1.png", 1.0),
    ("2_2.png", 1.0),
    ("2_3.png", 1.0),
    ("2_4.png", 0.8),
    ("2_5.png", 0.8),
    ("2_6.png", 0.8),
]
LAYER_2 = [
    ("3_1.png", 0.8),
    ("3_2.png", 1.0),
    ("3_3.png", 1.0),
]
LAYER_3 = [
    ("4_1.png", 1.0),
]

# save image
def craft(out):
    print('crafting...', out)
    if DEBUG: return

    (l0, l1, l2, l3) = list(out.split('.')[0])

    img_l0 = Image.open("{}/1_{}.png".format(DIR_INPUT, l0))
    img_l1 = Image.open("{}/2_{}.png".format(DIR_INPUT, l1))
    img_l2 = Image.open("{}/3_{}.png".format(DIR_INPUT, l2))
    img_l3 = Image.open("{}/4_{}.png".format(DIR_INPUT, l3))
    layers = [ img_l1, img_l2, img_l3 ]

    for layer in layers:
        img_l0.paste(layer, (0, 0), layer.convert('RGBA'))
    img_l0.save("{}/{}".format(DIR_OUTPUT, out), "PNG")

# loop
for l0 in LAYER_0:
    for l1 in LAYER_1:
        for l2 in LAYER_2:
            for l3 in LAYER_3:

                # skip from rarity
                r = random()
                if r > l0[1]: continue
                if r > l1[1]: continue
                if r > l2[1]: continue
                if r > l3[1]: continue

                # craft image
                traits = [
                    l0[0],
                    l1[0],
                    l2[0],
                    l3[0],
                ]
                out = "{}.png".format(''.join([ t.split('.')[0][-1] for t in traits ]))
                craft(out)
