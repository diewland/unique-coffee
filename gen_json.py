import json, os, glob, random
from pprint import pprint as pp
 
NAME = "Unique Coffee"
DESC = "NFT Unique Coffee of your choice by selecting Volume 2 decimal digits from Apetmism. 3-6 Dollars will be randomly distributed every 2 weeks. Invite everyone to win prizes."
IMG = "https://diewland.github.io/unique-coffee/png/c{:02}.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json"
MAX_SUPPLY = 100

# craft metadata
metadata = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": [
    {
      "trait_type": "Volume",
      "value": "***",
    },
  ],
  "compiler": ENGINE,
}

# build json + write to file
for id in range(0, MAX_SUPPLY):

    # update data
    metadata["name"] = "{} #{:02}".format(NAME, id)
    metadata["image"] = IMG.format(id)
    metadata["attributes"][0]["value"] = ".{:02}".format(id)

    # debug
    #print(metadata)

    # write file
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
