import json, os, glob, random
from datetime import datetime
from pprint import pprint as pp
 
NAME = "Unique Coffee"
DESC = "NFT Unique Coffee of your choice by selecting Volume 2 decimal digits from Apetmism. 3-6 Dollars will be randomly distributed every 2 weeks. Invite everyone to win prizes."
IMG = "https://diewland.github.io/unique-coffee/png/c{:02}.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json_shuffle"
MAX_SUPPLY = 100
SHUFFLE_TIME = 99

# helper
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
def now():
    return format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# build chunk
chunk = []
for id in range(0, MAX_SUPPLY):

    # template
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

    # update data
    metadata["name"] = "{} #{:02}".format(NAME, id)
    metadata["image"] = IMG.format(id)
    metadata["attributes"][0]["value"] = ".{:02}".format(id)

    # add to chunk
    chunk.append(metadata)

# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(chunk)
    # log
    print("<{}> shuffle #{:02}".format(now(), rnd))
    for cc in chunker(chunk, 25):
        print('-'.join([ c['name'].split('#')[1] for c in cc ]))
    print('')

# write file
for id, metadata in enumerate(chunk):
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
    # log
    print("<{}> ID {:02} -> {}".format(now(), id, metadata['name']))
