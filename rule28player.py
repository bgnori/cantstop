#!/usr/bin/python3

import libcs


"""
Source:
    http://www.solitairelaboratory.com/cantstop.html
"""

TABLE = """Column 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12
Spaces 	3 	5 	7 	9 	11 	13 	11 	9 	7 	5 	3
Value when marked 	12 	10 	8 	6 	4 	2 	4 	6 	8 	10 	12
Value when advanced 	6 	5 	4 	3 	2 	1 	2 	3 	4 	5 	6
"""

def parse(table):
    d = {}
    for line in table.splitlines():
        xs = list(map(lambda x: x.strip(), line.split('\t')))
        d[xs[0]] = xs[1:]
    return d

def makex(d):
    t = {}
    cols = d['Column']
    vas = d['Value when advanced']
    vms = d['Value when marked']

    for i, col in enumerate(cols):
        t[col] = {"col": col, "va":vas[i], "vm":vms[i]}
    return t

class Rule28Player:
    table = makex(parse(TABLE))

    def __init__(self):
        self.count = 0

    def place_markers(self, rs, markers, g):
        pass

    def is_done(self, markers, g):
        if g.gameover():
            return True
        return self.count > 27 and len(markers) > 2


if __name__ == "__main__":
    p = Rule28Player()
    for k, v in p.table.items():
        print(k, v)
    
else:
    sg = libcs.SoloGame(Rule28Player())
    for i in range(70):
        if sg.gameover():
            break
        print('step {}, {}'.format(i, sum(sg.camps.values())))
        sg.run()
        print(sg.camps)
    print('done')
