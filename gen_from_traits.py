from PIL import Image
from pprint import pprint as pp
from random import random
from os.path import exists

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
    ("3_4.png", 0.5),
]
LAYER_3 = [
    ("4_1.png", 1.0),
]

# save image
def craft(out):
    outpath = "{}/{}".format(DIR_OUTPUT, out)
    print('crafting...', outpath)
    if DEBUG: return

    # skip existing file
    if exists(outpath):
        return

    (l0, l1, l2, l3) = list(out.split('.')[0])
    layers = [
        Image.open("{}/1_{}.png".format(DIR_INPUT, l0)),
        Image.open("{}/2_{}.png".format(DIR_INPUT, l1)),
        Image.open("{}/3_{}.png".format(DIR_INPUT, l2)),
        Image.open("{}/4_{}.png".format(DIR_INPUT, l3)),
    ]
    new_img = Image.new("RGBA", layers[0].size)

    for layer in layers:
        #new_img.paste(layer, (0, 0), layer.convert('RGBA')) --- not good border
        #new_img.paste(layer, (0, 0), layer.convert('RGBa')) --- overlay bug
        new_img = Image.alpha_composite(new_img, layer)    # --- perfect!
    new_img.save(outpath, "PNG")

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
