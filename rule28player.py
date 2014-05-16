#!/usr/bin/python3

import libcs



class Rule28Player:
    def __init__(self):
        pass

    def place_markers(self, rs, markers, g):
        pass

    def is_done(self, markers, g):
        return len(markers) > 2


sg = libcs.SoloGame(Rule28Player())

for i in range(70):
    if sg.gameover():
        break
    print('step {}, {}'.format(i, sum(sg.camps.values())))
    sg.run()
    print(sg.camps)





