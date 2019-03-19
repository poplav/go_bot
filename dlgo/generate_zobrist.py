import random

from dlgo.gotypes import Player, Point


def to_python(player_state):
    if player_state is None:
        return 'None'
    if player_state == Player.black:
        return Player.black
    return Player.white


MAX63 = 0x7fffffffffffffff

table = {}
empty_board = 0
for row in range(1, 20):
    for col in range(1, 20):
        for state in (Player.black, Player.white):
            code = random.randint(0, MAX63)
            table[Point(row, col), state] = code
with open('zobrist.py', 'w') as f:
    f.write('from .gotypes import Player, Point\n')
    f.write('\n')
    f.write("__all__ = ['HASH_CODE', 'EMPTY_BOARD']\n")
    f.write('\n')
    f.write('HASH_CODE = {\n')
    for (pt, state), hash_code in table.items():
        f.write('    (%r, %s): %r,\n' % (pt, to_python(state), hash_code))
    f.write('}\n')
    f.write('\n')
    f.write('EMPTY_BOARD = %d\n' % (empty_board,))
