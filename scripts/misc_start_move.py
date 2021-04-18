from compute import *


if __name__ == '__main__':
    data = load()
    for i in range(2):
        total = count_eco_range(data[i], range(500))
        e4 = load_count('e4', i)
        d4 = load_count('d4', i)
        nf3 = load_count('nf3', i)
        c4 = load_count('c4', i)

        freq_e4 = freq_smooth(e4, total)
        freq_d4 = freq_smooth(d4, total)
        freq_nf3 = freq_smooth(nf3, total)
        freq_c4 = freq_smooth(c4, total)

        freqs = {
            '1. e4': freq_e4,
            '1. d4': freq_d4,
            '1. Nf3': freq_nf3,
            '1. c4': freq_c4
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
