"""
Computes frequency of black's responses after 1. d4 Nf6 2. c4: 2... e6, King's Indian, Grunfeld.

After 1. d4 Nf6 2. c4 g6, we ignored games where white didn't play 3. Nc3. More precisely,
we used a multiplier as described in the README.
"""

from compute import *


if __name__ == '__main__':
    for i in range(2):
        d4_nf6_c4 = load_count('d4-nf6-c4', i)
        d4_nf6_c4_e6 = load_count('d4-nf6-c4-e6', i)
        d4_nf6_c4_g6 = load_count('d4-nf6-c4-g6', i)
        d4_nf6_c4_g6_nc3_bg7 = load_count('d4-nf6-c4-g6-nc3-bg7', i)
        d4_nf6_c4_g6_nc3_d5 = load_count('d4-nf6-c4-g6-nc3-d5', i)
        d4_nf6_c4_g6_nc3 = d4_nf6_c4_g6_nc3_bg7 + d4_nf6_c4_g6_nc3_d5
        multiplier = d4_nf6_c4_g6 / d4_nf6_c4_g6_nc3

        freq_e6 = freq_smooth(d4_nf6_c4_e6, d4_nf6_c4)
        freq_kid = freq_smooth(multiplier * d4_nf6_c4_g6_nc3_bg7, d4_nf6_c4)
        freq_grunfeld = freq_smooth(multiplier * d4_nf6_c4_g6_nc3_d5, d4_nf6_c4)

        freqs = {
            '2... e6': freq_e6,
            'King\'s Indian': freq_kid,
            'Grunfeld': freq_grunfeld
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
