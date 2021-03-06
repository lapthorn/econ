#!/usr/bin/env python3

import random

DEBUG=False

# TODO turn the monty hall bit into a function
# TODO PEP8 the whole thang

# basic parameters
BOXES=3 # the number of boxes (3 for classic Monty Hall)
RUNS=30000 # number of simulation runs

# initialize the counters
CHANGEWINS=0   # number of wins if contestent changes
STICKWINS=0   # number of wins if contestent sticks
ROUNDS=0 # number of rounds so far

CHANGE=False # strategy for player - change or stick - might allow both

print ("Simulating the Monty Hall problem with", BOXES, "boxes, and", RUNS, "runs.")
print ()

while (ROUNDS < RUNS):
    BOXSET={} # set for the possible boxes
    # generate the set of boxes
    for i in range(1,BOXES+1):
        BOXSET=set(BOXSET) | {i}

    MYBOXES=BOXSET # set of boxes for contestent

    if DEBUG: print ('Boxes:', BOXSET)

    # hide the car
    CAR=random.randint(1, BOXES)
    if DEBUG: print (' Car:', CAR)

    # contestent picks a random box
    PICK=random.randint(1, BOXES)
    if DEBUG: print (' Pick:', PICK)

    # monty needs to open an empty door
    # remove the CONTESTENT pick from the possible set
    BOXSET=BOXSET-{PICK}
    MYBOXES=MYBOXES-{PICK}

    # remove the CAR from the possible set
    BOXSET=BOXSET-{CAR}

    if DEBUG: print (' Left:', BOXSET)
    if DEBUG: print (' MYBOXES:', MYBOXES)

    # Monty now picks and shows an empty box.
    # There's either one or two boxes to choose from.
    # Pick one at random

    MONTYPICK=random.sample(set(BOXSET),1)
    if DEBUG: print (' Montypick:', MONTYPICK)

    # remove Monty's choice from the contestent set
    MYBOXES=MYBOXES-set(MONTYPICK)
    if DEBUG: print (' MYBOXES:', MYBOXES)

    # let's collapse the wave function (ie see who won!)

    # stickwins
    if (PICK==CAR):
        STICKWINS+=1
        if DEBUG: print (' STICKWIN!')

    # changewins
    # pop the only remaining choice out of MYBOXES
    CHANGEPICK=MYBOXES.pop()
    if DEBUG: print (' CHANGEPICK:', CHANGEPICK)
    if (CHANGEPICK==CAR):
        CHANGEWINS+=1
        if DEBUG: print (' CHANGEWIN!')

    ROUNDS+=1
    # finish

# the results
print ('  STICKWINS:', STICKWINS, STICKWINS/ROUNDS)
print (' CHANGEWINS:', CHANGEWINS, CHANGEWINS/ROUNDS)
print ('     ROUNDS:', ROUNDS)
print ()
if (CHANGEWINS > STICKWINS):
    print ("It's better to change")
else:
    print ("It's better to stick")
