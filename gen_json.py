import json, glob
from random import shuffle
from pprint import pprint as pp
 
TOKEN_SIZE = 20
START_ID = 80
ASSETS_DIR = 'assets'
OUTPUT_DIR = 'json'

NAME = "Jigsaw Bowling Edition"
DESC = "1st Bowling Tournament powered by MajorVerse. Saturday Night, 27 August 2022 at Esplanade Ratchada."
IMG = "https://diewland.github.io/jigsaw-bowling/assets"
ENGINE = "Jigsaw Engine"

ATTR_FIELDS = [
    "Background",
    "Bowling Color",
    "Pattern",
]
ATTR_MAPPING = [
    # background
    [
        "Energize Red",
        "Midnight Black",
    ],
    # bowling color
    [
        "Brown",
        "Blue",
        "Green",
        "Yellow",
        "Orange",
        "Pink",
    ],
    # pattern
    [
        "Rainbow",
        "Mini-Heart",
        "Stars",
        "Ethereum",
    ],
]

# shuffle asset file path
assets = [ f for f in glob.iglob('{}/*.png'.format(ASSETS_DIR)) ]
for i in range(0, 100): shuffle(assets) # shuffle 100 times

# loop
for id, asset_path in enumerate(assets):

    # extract cidx
    code = asset_path.split('/')[1].split('.')[0]
    cidx = [ int(c) for c in list(code) ]

    # craft attributes
    attrs = [
        {
          "trait_type": "Collection",
          "value": NAME, 
        },
    ]
    for idx, cid in enumerate(cidx):
        if idx >= len(ATTR_FIELDS):
            break
        field = ATTR_FIELDS[idx]
        value = ATTR_MAPPING[idx][cid-1]
        attrs += [ { "trait_type": field, "value": value } ]

    # craft metadata
    metadata = {
      "name": "{} #{}".format(NAME, id),
      "description": DESC,
      "image": "{}/{}.png".format(IMG, code),
      "attributes": attrs,
      "compiler": ENGINE,
    }

    #pp(metadata)
    #continue

    # write to file
    with open("./{}/{}".format(OUTPUT_DIR, START_ID + id), "w") as f:
        json.dump(metadata, f)
