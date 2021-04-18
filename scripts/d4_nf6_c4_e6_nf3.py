"""
Computes the frequency of 3... b6 and 3... d5 after 1. d4 Nf6 2. c4 e6 3. Nf3.
"""

from compute import *


if __name__ == '__main__':
    for i in range(2):
        d4_nf6_c4_e6_nf3 = load_count('d4-nf6-c4-e6-nf3', i)
        d4_nf6_c4_e6_nf3_b6 = load_count('d4-nf6-c4-e6-nf3-b6', i)
        d4_nf6_c4_e6_nf3_d5 = load_count('d4-nf6-c4-e6-nf3-d5', i)

        freq_b6 = freq_smooth(d4_nf6_c4_e6_nf3_b6, d4_nf6_c4_e6_nf3)
        freq_d5 = freq_smooth(d4_nf6_c4_e6_nf3_d5, d4_nf6_c4_e6_nf3)

        freqs = {
            '3... b6 (Queen\'s Indian)': freq_b6,
            '3... d5 (Queen\'s Gambit Declined)': freq_d5
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
