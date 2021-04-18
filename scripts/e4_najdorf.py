from compute import *


if __name__ == '__main__':
    data = load()
    plot_years = [range(31), range(3, 31)]
    for i in range(2):
        total = count_eco_range(data[i], eco_range('B', 50, 99))
        moscow = count_eco_range(data[i], eco_range('B', 51, 52))
        d4 = count_eco_range(data[i], eco_range('B', 56, 99))
        najdorf = load_count('e4-najdorf', i)
        multiplier = d4 / najdorf
        be3 = load_count('e4-najdorf-be3', i)
        be2 = load_count('e4-najdorf-be2', i)
        bg5 = load_count('e4-najdorf-bg5', i)
        bc4 = load_count('e4-najdorf-bc4', i)
        h3 = load_count('e4-najdorf-h3', i)
        other = najdorf - be3 - bg5 - be2 - bc4 - h3

        freq_moscow = freq_smooth(moscow, total)
        freq_be3 = freq_smooth(multiplier * be3, total)
        freq_be2 = freq_smooth(multiplier * be2, total)
        freq_bg5 = freq_smooth(multiplier * bg5, total)
        freq_bc4 = freq_smooth(multiplier * bc4, total)
        freq_h3 = freq_smooth(multiplier * h3, total)
        freq_other = freq_smooth(multiplier * other, total)

        freqs = {
            '6. Be3': freq_be3,
            '6. Be2': freq_be2,
            '6. Bg5': freq_bg5,
            '6. Bc4': freq_bc4,
            '6. h3': freq_h3,
            '6. other': freq_other,
            'Moscow': freq_moscow
        }
        print(table(freqs, i=i, old_range=[3, 9]))
        print()
        for name, freq in freqs.items():
            plt.plot(years[plot_years[i]], freq[plot_years[i]], label=name)
        plt.axis([year_start - 1, year_end + 1, 0, 100])
        plt.yticks(range(0, 101, 10))
        plt.grid()
        plt.legend()
        plt.title(levels[i])
        plt.show()
