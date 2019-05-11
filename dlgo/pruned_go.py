from six.moves import input

from dlgo import goboard
from dlgo import gotypes
from dlgo import minimax
from dlgo.utils import print_board, print_move, point_from_coords
import time

BOARD_SIZE = 3


def capture_diff(game_state):
    black_stones = 0
    white_stones = 0
    for r in range(1, game_state.board.num_rows + 1):
        for c in range(1, game_state.board.num_cols + 1):
            p = gotypes.Point(r, c)
            color = game_state.board.get(p)
            if color == gotypes.Player.black:
                black_stones += 1
            elif color == gotypes.Player.white:
                white_stones += 1
    diff = black_stones - white_stones
    if game_state.next_player == gotypes.Player.black:
        return diff
    return -1 * diff


def main_vs_human():
    game = goboard.GameState.new_game(BOARD_SIZE)
    bot = minimax.DepthPrunedAgent(2, capture_diff)

    while not game.is_over():
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)


def main_vs_bot():
    board_size = 5
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: minimax.DepthPrunedAgent(1, capture_diff),
        gotypes.Player.white: minimax.DepthPrunedAgent(3, capture_diff),
    }
    while not game.is_over():
        time.sleep(0.03)

        print(chr(27) + "[2J")
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
        print(game.winner())


if __name__ == '__main__':
    main_vs_bot()
