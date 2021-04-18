from compute import *


def count(data, i):
    start = count_eco_range(data, eco_range('C', 40, 99))
    petroff = count_eco_range(data, eco_range('C', 42, 43))
    nc6 = count_eco_range(data, eco_range('C', 44, 99))
    ruy = count_eco_range(data, eco_range('C', 60, 99))
    multiplier_ruy = nc6 / ruy
    berlin = count_eco_range(data, eco_range('C', 65, 67))
    a6 = count_eco_range(data, eco_range('C', 68, 99))

    freq_petroff = freq_smooth(petroff, start)
    freq_berlin = freq_smooth(multiplier_ruy * berlin, start)
    freq_a6 = freq_smooth(multiplier_ruy * a6, start)

    freqs = {
        'Petroff': freq_petroff,
        'Berlin': freq_berlin,
        '3... a6': freq_a6
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


if __name__ == '__main__':
    data = load()
    for i in range(2):
        count(data[i], i)
