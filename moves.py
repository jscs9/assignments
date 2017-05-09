import random as rand

def request_moves(how_many):
    '''
    Generates a string representing moves for a monster in a video game.

    how_many: number of move segments to be generated.  Each segment occurs in a specific
              direction with a distance of between 1 and 5 steps.  Segment directions
              do not repeat, or immediately double back on themselves, e.g. 'u' cannot follow 'd',
              'l' cannot follow 'r', etc.
    Returns: A string of characters made of 'l', 'r', 'u', 'd' that describes
             how the monster moves.
    '''

    dirmap = ['l', 'r', 'u', 'd']   # a list of abbreviations for directions

    # generate an initial direction and distance between 1 and 5 steps
    dir = dirmap[rand.randint(0, 3)]
    moves = dir*rand.randint(1, 5)

    # For each move, randomly determine its direction, and how far (between 1 and 5 steps)
    for i in range(how_many-1):
        # get a random number between 0 and 3

        # generate directions randomly until we get a direction that
        # is not the same as the previous direction.
        dir = moves[-1]
        while (dir == moves[-1] or (dir == 'r' and moves[-1] == 'l') or (dir == 'u' and moves[-1] == 'd') or
                                   (dir == 'l' and moves[-1] == 'r') or (dir == 'd' and moves[-1] == 'u')):

            dir = dirmap[rand.randint(0, 3)]

        # map the number to a legal move character using 'dirmap',
        # make between 1 and 5 copies of that move character,
        # and concatenate it with the existing moves generated so far.
        moves = moves + dir * rand.randint(1, 5)

    return moves
