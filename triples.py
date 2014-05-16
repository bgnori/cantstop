#!/usr/bin/python3


import libcs

xs = list(libcs.steps.keys())
vs = []
for markers in libcs.ijk(xs):
    count = 0
    for rs in libcs.on1296():
        if not libcs.is_burst(rs, markers):
            count += 1
    vs.append((markers, count))
vs.sort(key=lambda x: x[1])

import json
print(json.dumps(vs))
