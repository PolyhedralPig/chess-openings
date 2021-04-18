from compute import *


if __name__ == '__main__':
    data = load()
    y_limits = [4000, 200]
    plot_years = [range(31), range(12, 30)]
    for i in range(2):
        total = count_eco_range(data[i], eco_range('B', 30, 39))
        d4 = count_eco_range(data[i], eco_range('B', 32, 39))
        rossolimo = load_count('e4-sveshnikov-rossolimo', i)
        svesh_7nd5 = load_count('e4-sveshnikov-7nd5', i)
        svesh_9nd5 = load_count('e4-sveshnikov-9nd5', i)
        svesh_9bxf6 = load_count('e4-sveshnikov-9bxf6', i)
        svesh_total = svesh_7nd5 + svesh_9nd5 + svesh_9bxf6
        multiplier = d4 / svesh_total

        freq_rossolimo = freq_smooth(rossolimo, total)
        freq_svesh_7nd5 = freq_smooth(multiplier * svesh_7nd5, total)
        freq_svesh_9nd5 = freq_smooth(multiplier * svesh_9nd5, total)
        freq_svesh_9bxf6 = freq_smooth(multiplier * svesh_9bxf6, total)

        freqs = {
            'Rossolimo': freq_rossolimo,
            '7. Nd5': freq_svesh_7nd5,
            '9. Nd5': freq_svesh_9nd5,
            '9. Bxf6': freq_svesh_9bxf6
        }
        print(table(freqs, i=i, old_range=range(12, 16), new_range=29))
        print()
        for name, freq in freqs.items():
            plt.plot(years[plot_years[i]], freq[plot_years[i]], label=name)
        plt.axis([year_start - 1, year_end + 1, 0, 100])
        plt.yticks(range(0, 101, 10))
        plt.grid()
        plt.legend()
        plt.title(levels[i])
        plt.show()

        plt.plot(years, total, label='total')
        plt.plot(years, svesh_total, label='svesh_total')
        plt.axis([year_start - 1, year_end + 1, 0, y_limits[i]])
        plt.grid()
        plt.legend()
        plt.title(levels[i])
        plt.show()
