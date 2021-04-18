"""
Computes the frequency of the London.

It's tricky to determine which games open with the London, since the London doesn't correspond to
a particular range of ECO codes or a particular sequence of moves.
We decided that the London is any game with ECO codes A40-A49 (1. d4 sidelines without 2. c4),
A80-A99 (Dutch), or D00-D05 (1. d4 without 2. c4) where white plays Bf4 in the first 3 moves.

We used HIARCS to filter the database 2300.pgn to create the database london-2300.pgn (likewise for 2600),
which contains all games with ECO codes A40-A49, A80-A99, and D00-D05 (not necessarily London games).

This script is slower than the other scripts because it has to read the moves of the game
(to check if Bf4 occurs in the first 3 moves), while the other scripts either
read the preprocessed databases (very fast) or only read the headers of the pgn.
"""

from compute import *

import chess.pgn as p

# We compute the frequency of the London relative to all 1. d4 openings.
total_d4 = eco_ranges([
    ('A', 40, 99),
    ('D', 0, 99),
    ('E', 0, 99)
])


def check_london(data_2300, data_2600):
    files = ['../databases/london-2300.pgn', '../databases/london-2600.pgn']
    totals = [data_2300, data_2600]
    for i in range(2):
        count = np.zeros(len(years))
        with open(files[i], 'r') as pgn:
            game = p.read_game(pgn)
            num_games = 0
            while game:
                ply = 1
                for move in game.mainline_moves():
                    uci = move.uci()
                    if uci == 'c1f4':
                        year = int(game.headers['Date'].split('.')[0])
                        count[year_index(year)] += 1
                        break
                    ply += 1
                    if ply > 5:
                        break
                num_games += 1
                if num_games % 1000 == 0:
                    print(num_games)
                game = p.read_game(pgn)
                if not game:
                    game = p.read_game(pgn)
            print(num_games)
        total = np.sum(totals[i][:, total_d4], axis=1)
        freq = freq_smooth(count, total)
        plt.plot(years, freq, label=levels[i])
    plt.axis([year_start - 1, year_end + 1, 0, 30])
    plt.grid()
    plt.legend()
    plt.title('London')
    plt.show()


if __name__ == '__main__':
    check_london(*load())
