from compute import *


if __name__ == '__main__':
    data_2300, data_2600 = load()
    games_2300 = count_eco_range(data_2300, range(500))
    games_2600 = count_eco_range(data_2600, range(500))
    total_2300 = np.sum(games_2300)
    total_2600 = np.sum(games_2600)

    plt.plot(years, games_2300)
    plt.axis([year_start - 1, year_end + 1, 0, 100000])
    plt.grid()
    plt.title('2300 ({} games)'.format(total_2300))
    plt.show()

    plt.plot(years, games_2600)
    plt.axis([year_start - 1, year_end + 1, 0, 5000])
    plt.grid()
    plt.title('2600 ({} games)'.format(total_2600))
    plt.show()
