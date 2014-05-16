#!/usr/bin/python3

import random

steps = {2:3,
        3:5,
        4:7,
        5:9,
        6:11,
        7:13,
        8:11,
        9:9,
        10:7,
        11:5,
        12:3}


def roll():
    return [random.randint(1, 6) for i in range(4)]

def doubledrop(xs, i, j):
    for n, x in enumerate(xs):
        if n == i or n == j:
            continue
        yield x


def combinate(xs):
    """
    >>> for comb in combinate([1,2,4,8]):print(comb)
    ((1, 2), (4, 8))
    ((1, 4), (2, 8))
    ((2, 4), (1, 8))
    ((1, 8), (2, 4))
    ((2, 8), (1, 4))
    ((4, 8), (1, 2))
    """
    for j in range(4):
        for i in range(j):
            yield (xs[i], xs[j]), tuple(doubledrop(xs, i, j))

def pair(x, y):
    if x < y:
        return (x, y)
    return (y, x)


def candidates(combs):
    """
    >>> candidates(combinate([1,1,1,1]))
    {(2, 2): ((1, 1), (1, 1))}
    >>> candidates(combinate([1,1,1,2]))
    {(2, 3): ((1, 2), (1, 1))}
    >>> candidates(combinate([1,2,4,8]))
    {(5, 10): ((2, 8), (1, 4)), (6, 9): ((1, 8), (2, 4)), (3, 12): ((4, 8), (1, 2))}

    """
    d = {}
    for xs, ys in combs:
        p = pair(sum(xs), sum(ys))
        """
        e = d.get(p, None)
        if e is None:
            e = []
        e.append((xs, ys))
        d[p] = e
        """
        d[p] = (pair(*xs), pair(*ys))
    return d



def is_burst(rolls, markers):
    """
    >>> is_burst([1, 1, 1, 1], {3, 4, 5})
    True
    >>> is_burst([1, 1, 1, 2], {3, 4, 5})
    False
    >>> is_burst([1, 1, 1, 2], {3:2, 4:3, 5:3})
    False

    """
    if len(markers) < 3:
        return False
    d = candidates(combinate(rolls))

    for small, big in d.keys():
        if small in markers or big in markers:
            return False
    return True

def ijk(xs):
    for i in range(len(xs)):
        for j in range(i):
            for k in range(j):
                yield xs[k], xs[j], xs[i]

def on1296():
    for x3 in range(1, 7):
        for x2 in range(1, 7):
            for x1 in range(1, 7):
                for x0 in range(1, 7):
                    yield x0, x1, x2, x3


class SoloGame:
    def __init__(self, player):
        self.camps = {}
        self.player = player

    def on_turn(self, player):
        markers = {}
        done = False

        while not done:
            rs = roll()
            print('   {}, {}'.format(markers, rs))
            if len(markers) == 3 and is_burst(rs, markers):
                return None #bursted
            player.place_markers(rs, markers, self)
            done = player.is_done(markers, self)
        print('   {}'.format(markers))
        return markers

    def run(self):
        m = self.on_turn(self.player)
        if m is not None:
            self.camps.update(m)

    def gameover(self):
        count = 0
        for c in self.camps:
            if not self.available(c):
                count += 1
        return count > 2

    def available(self, x):
        return self.camps.get(x, 0) < steps[x]

    def move_marker_on(self, markers, x):
        assert self.available(x)
        v = markers.get(x, None)
        if v is None:
            v = self.camps.get(x, 0)
        markers[x] = v + 1



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("done")


