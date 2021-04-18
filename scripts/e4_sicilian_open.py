from compute import *


if __name__ == '__main__':
    variations = [
        ('B', 32, 32, 'Kalashnikov'),
        ('B', 33, 33, 'Sveshnikov'),
        ('B', 34, 39, 'Acc. Dragon'),
        ('B', 41, 43, 'Kan'),
        ('B', 44, 49, 'Taimanov'),
        ('B', 56, 69, 'Classical'),
        ('B', 70, 79, 'Dragon'),
        ('B', 80, 85, 'Scheveningen'),
        ('B', 86, 99, 'Najdorf')
    ]
    '''
    The database e4-sicilian-d6-d4 contains games that started with 1. e4 c5 2. Nf3 d6 and then
    reached the position after 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3, to rule out White's sidelines
    like 4. Qxd4 and 5. f3.
    '''
    data = [[load_eco('e4-sicilian-nc6-d4', 0),
             load_eco('e4-sicilian-e6-d4', 0),
             load_eco('e4-sicilian-d6-d4', 0)],
            [load_eco('e4-sicilian-nc6-d4', 1),
             load_eco('e4-sicilian-e6-d4', 1),
             load_eco('e4-sicilian-d6-d4', 1)]]
    for i in range(2):
        nc6 = load_count('e4-sicilian-nc6', i)
        nc6_d4 = load_count('e4-sicilian-nc6-d4', i)
        multiplier_nc6 = nc6 / nc6_d4
        e6 = load_count('e4-sicilian-e6', i)
        e6_d4 = load_count('e4-sicilian-e6-d4', i)
        multiplier_e6 = e6 / e6_d4
        d6 = load_count('e4-sicilian-d6', i)
        d6_d4 = load_count('e4-sicilian-d6-d4', i)
        multiplier_d6 = d6 / d6_d4
        multipliers = [multiplier_nc6, multiplier_e6, multiplier_d6]

        totals = {}
        for v in variations:
            totals[v[3]] = np.zeros(len(years))
        for j in range(len(data[i])):
            for v in variations:
                name = v[3]
                count = multipliers[j] * count_eco_range(data[i][j], eco_range(*(v[:3])))
                totals[name] += count
        totals['Acc. Dragon'] += load_count('e4-sicilian-g6', i)
        total = np.sum(list(totals.values()), axis=0)
        freqs = {n: freq_smooth(t, total) for n, t in totals.items()}

        print(table(freqs, i=i))
        print()
        names = [
            'Najdorf',
            'Sveshnikov',
            'Classical',
            'Taimanov'
        ]
        for name in names:
            plt.plot(years, freqs[name], label=name)
        plt.axis([year_start - 1, year_end + 1, 0, 100])
        plt.yticks(range(0, 101, 10))
        plt.grid()
        plt.legend()
        plt.title(levels[i])
        plt.show()
