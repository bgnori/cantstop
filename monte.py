#!/usr/bin/python3

import libcs
import sys

def average_roll2burst(markers, N):
    count = 0
    for i in range(N):
        while(not libcs.is_burst(libcs.roll(), markers)):
            count += 1
    return 1.0 * count / N



xs = list(libcs.steps.keys())
vs = [(average_roll2burst(markers, int(sys.argv[1])), markers) for markers in libcs.ijk(xs)]
vs.sort(key=lambda x: x[0])
for v, markers in vs:
    print("{}: {}".format(markers, v))
