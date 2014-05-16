#!/usr/bin/python3

import libcs

class DumbPlayer:
    def __init__(self):
        pass
    def place_markers(self, rs, markers, g):
        done = False
        for small, big in libcs.candidates(libcs.combinate(rs)):
            if g.available(small):
                g.move_marker_on(markers, small)
                done = True
            if g.available(big):
                if len(markers) < 3 or big in markers:
                    g.move_marker_on(markers, big)
                    done = True
            if done:
                return

    def is_done(self, markers, g):
        return len(markers) > 2


sg = libcs.SoloGame(DumbPlayer())

for i in range(70):
    if sg.gameover():
        break
    print('step {}, {}'.format(i, sum(sg.camps.values())))
    sg.run()
    print(sg.camps)



