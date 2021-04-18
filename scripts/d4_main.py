"""
Computes the frequency of black's 4th move in the main position of 1. d4,
which arises from 1. d4 Nf6 2. c4 e6 3. Nf3 d5 4. Nc3 and other move orders.

We used HIARCS to create the following databases:
Filter 2300.pgn to create d4-main-2300.pgn, all games that reach the main position.
Filter d4-main-2300.pgn to create d4-main-be7-2300.pgn, all games from the main position where
black played 4... Be7. Note that we filter d4-main-2300.pgn, not 2300.pgn,
so we don't count games that reached the position after 4... Be7 but didn't reach the main position.
Likewise, we created databases for the other 4th moves.
"""

from compute import *


if __name__ == '__main__':
    for i in range(2):
        d4_main = load_count('d4-main', i)
        d4_main_be7 = load_count('d4-main-be7', i)
        d4_main_bb4 = load_count('d4-main-bb4', i)
        d4_main_c6 = load_count('d4-main-c6', i)
        d4_main_dxc4 = load_count('d4-main-dxc4', i)
        d4_main_c5 = load_count('d4-main-c5', i)

        freq_be7 = freq_smooth(d4_main_be7, d4_main)
        freq_bb4 = freq_smooth(d4_main_bb4, d4_main)
        freq_c6 = freq_smooth(d4_main_c6, d4_main)
        freq_dxc4 = freq_smooth(d4_main_dxc4, d4_main)
        freq_c5 = freq_smooth(d4_main_c5, d4_main)

        freqs = {
            '4... Be7 (QGD)': freq_be7,
            '4... Bb4 (Ragozin)': freq_bb4,
            '4... c6 (Semi-Slav)': freq_c6,
            '4... dxc4 (Vienna)': freq_dxc4,
            '4... c5 (Semi-Tarrasch)': freq_c5
        }
        print(table(freqs, i=i))
        print()
        for name, freq in freqs.items():
            plt.plot(years, freq, label=name)
        plt.axis([year_start - 1, year_end + 1, 0, 100])
        plt.yticks(range(0, 101, 10))
        plt.grid()
        plt.legend()
        plt.title(levels[i])
        plt.show()
