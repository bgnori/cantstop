#!/usr/bin/python3

import libcs

class SoloGame:
    def __init__(self, player):
        self.camps = {}
        self.player = player

    def on_turn(self, player):
        markers = {}
        done = False

        while not done:
            rs = libcs.roll()
            print('   {}, {}'.format(markers, rs))
            if len(markers) == 3 and libcs.is_burst(rs, markers):
                return None #bursted
            player.place_markers(rs, markers, self.camps)
            done = player.is_done(markers, self.camps)
        print('   {}'.format(markers))
        return markers

    def run(self):
        m = self.on_turn(self.player)
        if m is not None:
            self.camps.update(m)

    def gameover(self):
        count = 0
        for c in self.camps:
            if not available(c, self.camps):
                count += 1
        return count > 2


def available(x, camps):
    return camps.get(x, 0) < libcs.steps[x]

def has_marker(markers, x):
    return x in markers

def move_marker_on(markers, x, camps):
    assert available(x, camps)
    v = markers.get(x, None)
    if v is None:
        v = camps.get(x, 0)
    markers[x] = v + 1
    


class DumbPlayer:
    def __init__(self):
        pass
    def place_markers(self, rs, markers, camps):
        done = False
        for small, big in libcs.candidates(libcs.combinate(rs)):
            if available(small, camps):
                move_marker_on(markers, small, camps)
                done = True
            if available(big, camps):
                if len(markers) < 3 or big in markers:
                    move_marker_on(markers, big, camps)
                    done = True
            if done:
                return

    def is_done(self, markers, camps):
        return len(markers) > 2

dp = DumbPlayer()
sg = SoloGame(dp)

for i in range(70):
    if sg.gameover():
        break
    print('step {}, {}'.format(i, sum(sg.camps.values())))
    sg.run()
    print(sg.camps)

