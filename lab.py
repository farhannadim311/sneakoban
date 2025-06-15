"""
6.1010 Lab:
Snekoban Game
"""

# import json # optional import for loading test_levels
# import typing # optional import
# import pprint # optional import

# NO ADDITIONAL IMPORTS!


DIRECTION_VECTOR = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}


def make_new_game(level_description):
    """
    Given a description of a game state, create and return a game
    representation of your choice.

    The given description is a list of lists of lists of strs, representing the
    locations of the objects on the board (as described in the lab writeup).

    For example, a valid level_description is:

    [
        [[], ['wall'], ['computer']],
        [['target', 'player'], ['computer'], ['target']],
    ]

    The exact choice of representation is up to you; but note that what you
    return will be used as input to the other functions.
    """
    copied_game = [[[item for item in cell] for cell in row] for row in level_description]
    return copied_game


def victory_check(game):
    """
    Given a game representation (of the form returned from make_new_game),
    return a Boolean: True if the given game satisfies the victory condition,
    and False otherwise.
    """
    target_counter = 0
    count = 0
    for i in game:
        for j in i:
            if("target" in j and "computer" in j):
                count += 1
            if ("target" in j):
                target_counter += 1
    
    if (count == 0):
        return False
    return (target_counter == count)



def step_game(game, direction):
    """
    Given a game representation (of the form returned from make_new_game),
    return a game representation (of that same form), representing the
    updated game after running one step of the game.  The user's input is given
    by direction, which is one of the following:
        {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    match = make_new_game(game)
    for idx, i in enumerate(match):
        for idx2, j in enumerate(i):
            if "player" in j: 
                if direction in DIRECTION_VECTOR:
                    dx, dy = DIRECTION_VECTOR[direction]
                    new_x = idx + dx
                    new_y = idx2 + dy

    # Check bounds
                if 0 <= new_x < len(match) and 0 <= new_y < len(match[0]):
                    destination = match[new_x][new_y]
                    if "wall" not in destination and "computer" not in destination:
                        match[new_x][new_y].append("player")
                        match[idx][idx2].remove("player")
                        return match
                    
                    elif "computer" in destination:
                        if 0 <= new_x + dx < len(match) and 0 <= new_y + dy < len(match[0]):
                            if ('wall' not in match[new_x + dx][new_y + dy] and 'computer' not in match[new_x + dx][new_y + dy]):
                                match[new_x][new_y].append("player")
                                match[idx][idx2].remove("player") 
                                match[new_x + dx][new_y + dy].append("computer")
                                match[new_x][new_y].remove("computer")
                                return match
                            else:
                                return match
                    else:
                        return match


def dump_game(game):
    """
    Given a game representation (of the form returned from make_new_game),
    convert it back into a level description that would be a suitable input to
    make_new_game (a list of lists of lists of strings).

    This function is used by the GUI and the tests to see what your game
    implementation has done, and it can also serve as a rudimentary way to
    print out the current state of your game for testing and debugging on your
    own.
    """
    return game

def solve_puzzle(game):
    """
    Given a game representation (of the form returned from make_new_game), find
    a solution.

    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None.
    """
    match = make_new_game(game)
    sequence = moves(match)




def sequence_state(game):
    match = make_new_game(game)
    sequence = [match]
    agenda = [match]
    idx = 0
    while (agenda):
        path = agenda.pop(0)
        for i in DIRECTION_VECTOR:
            if (victory_check(path)):
                return sequence
            sequence.append(step_game(match, i))
            agenda.append(step_game(match, i))
    return None

def moves(game):
    sequence = sequence_state(game)
    temp = []
    move_seq = []
    for i in sequence:
        for k in DIRECTION_VECTOR:
            if(step_game(k) == i):
                temp.append(k)
        
    return moves


if __name__ == "__main__":
    pass
