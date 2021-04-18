from compute import *

total_e4 = eco_ranges([
    ('B', 0, 99),
    ('C', 0, 99)
])

if __name__ == '__main__':
    data = load()
    plot_years = [range(7, 31), range(7, 31)]
    for i in range(2):
        berlin = count_eco_range(data[i], eco_range('C', 65, 67))
        berlin_endgame = load_count('e4-berlin-endgame', i)
        total = count_eco_range(data[i], total_e4)
        berlin_draw = load_count('e4-berlin-draw', i)

        freq_berlin = freq_smooth(berlin, total)
        freq_berlin_endgame = freq_smooth(berlin_endgame, total)
        percent_endgame = freq_smooth(berlin_endgame, berlin)
        percent_draw = freq_smooth(berlin_draw, berlin)

        plt.plot(years, freq_berlin, label='Berlin')
        plt.plot(years, freq_berlin_endgame, label='Berlin endgame')
        plt.axis([year_start - 1, year_end + 1, 0, 100])
        plt.yticks(range(0, 101, 10))
        plt.grid()
        plt.legend()
        plt.title(levels[i])
        plt.show()

        plt.plot(years[plot_years[i]], percent_endgame[plot_years[i]], label='% of Berlin games reached endgame')
        plt.plot(years[plot_years[i]], percent_draw[plot_years[i]], label='% of Berlin games drawn')
        plt.axis([year_start - 1, year_end + 1, 0, 100])
        plt.yticks(range(0, 101, 10))
        plt.grid()
        plt.legend()
        plt.title(levels[i])
        plt.show()
