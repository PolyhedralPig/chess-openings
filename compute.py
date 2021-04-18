"""
The functions in this file are used in the scripts to compute the results.
run takes a list of ECO ranges and creates a plot of how often each range appears in the database.
load_count loads the preprocessed array of the number of games per year in the database.
See the scripts for example usage.
"""

from preprocess import eco_index
from preprocess import year_index
from preprocess import year_start
from preprocess import year_end
from preprocess import years

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

levels = ['2300', '2600']


def eco_range(letter, start, end):
    """Returns list of indices of ECO codes."""
    output = []
    for i in range(start, end + 1):
        output.append(eco_index(letter + str(i).zfill(2)))
    return output


def eco_ranges(ranges):
    """Returns list of indices of multiple ranges of ECO codes."""
    return [e for r in ranges for e in eco_range(*r)]


def count_eco_range(data, r):
    """
    :param data: database preprocessed by preprocess.py
    :param r: list of indices of ECO codes
    :return: array with an entry for each year, the number of games whose ECO code falls in the range
    """
    return np.sum(data[:, r], axis=1)


name_other = 'other'


def compute_groups(groups_list, total=None):
    """See scripts/d4.py and other scripts for example usage."""
    groups = {}
    for g in groups_list:
        name = g[3]
        r = eco_range(*(g[:3]))
        if name not in groups:
            groups[name] = r
        else:
            groups[name].extend(r)
    if total:
        in_groups = [e for r in groups.values() for e in r]
        other = [e for e in total if e not in in_groups]
        groups[name_other] = other
    return groups


def freq_smooth(count, total):
    """
    :param count: array with an entry for each year
    :param total: array with an entry for each year
    :return: array with an entry for each year, where entry i is the percentage of count
    relative to total for years (i - 1), i, and (i + 1), with year i weighted twice
    """
    offset_left = 1
    offset_right = 1
    extra_weight_middle = 1
    freq = np.zeros(len(count))
    for i in range(len(freq)):
        lower = max(0, i - offset_left)
        upper = min(len(freq) - 1, i + offset_right)
        freq[i] = 100 * (np.sum(count[range(lower, upper + 1)]) + extra_weight_middle * count[i]) \
            / (np.sum(total[range(lower, upper + 1)]) + extra_weight_middle * total[i])
    return freq


def compute_freq(data, groups, names, i=0):
    count = {n: count_eco_range(data, r) for n, r in groups.items()}
    total = np.array([sum([c[year_index(y)] for _, c in count.items()]) for y in years])
    freq = {}
    for n in names:
        freq[n] = freq_smooth(count[n], total)
    print(table(freq, i=i))
    print()
    return freq


def run(groups, names, y_limits=None, collect=None):
    """See scripts/d4.py and other scripts for example usage."""
    data = load()
    freq_2300 = compute_freq(data[0], groups, names, i=0)
    freq_2600 = compute_freq(data[1], groups, names, i=1)
    freq = [freq_2300, freq_2600]
    if y_limits:
        y_limits = iter(y_limits)
    for n in names:
        plt.plot(years, freq[0][n], label=levels[0])
        plt.plot(years, freq[1][n], label=levels[1])
        y_limit = 100 if not y_limits else next(y_limits)
        plt.axis([year_start - 1, year_end + 1, 0, y_limit])
        if y_limit == 100:
            plt.yticks(range(0, 101, 10))
        plt.grid()
        plt.legend()
        plt.title(n)
        plt.show()
    if collect:
        for i in range(2):
            for c in collect:
                for j in c:
                    plt.plot(years, freq[i][names[j]], label=names[j])
                y_limit = 100 if not y_limits else next(y_limits)
                plt.axis([year_start - 1, year_end + 1, 0, y_limit])
                if y_limit == 100:
                    plt.yticks(range(0, 101, 10))
                plt.grid()
                plt.legend()
                plt.title(levels[i])
                plt.show()


def load_eco(name, i):
    """Loads array output by preprocess.py year_eco."""
    path = Path(__file__).parent.absolute()
    file_format = '{}/preprocessed/eco/{}-{}.npy' if name != '' else '{}/preprocessed/{}{}.npy'
    return np.load(file_format.format(path, name, levels[i]))


def load_count(name, i):
    """Loads array output by preprocess.py year_count."""
    path = Path(__file__).parent.absolute()
    return np.load('{}/preprocessed/count/{}-{}.npy'.format(path, name, levels[i]))


def load():
    """Loads preprocessed databases for master level and super-GM level."""
    return load_eco('', 0), load_eco('', 1)


'''
The functions below generate LaTeX for typesetting the tables in the report
(although I had to make some manual modifications afterward).
'''


def cell_color(diff):
    color_positive = 'blue'
    color_negative = 'orange'
    max_color_positive = 50
    max_color_negative = 100
    max_diff = 20
    diff = max(min(diff, max_diff), -max_diff)
    magnitude = round(abs(diff) / max_diff * (max_color_positive if diff >= 0 else max_color_negative))
    color = color_positive if diff >= 0 else color_negative
    return '\\cellcolor{{{}!{}}}'.format(color, magnitude)


def old_new_diff(freq, old_range=None, new_range=None):
    # For the old frequency, we average the frequencies of the first 6 years, although it would
    # also make sense to take a weighted average to account for number of games per year
    if not old_range:
        old_range = range(6)
    if not new_range:
        new_range = len(freq) - 1
    old = np.mean(freq[old_range])
    new = np.mean(freq[new_range])
    diff = new - old
    return old, new, diff


def table_row(name, old, new, diff):
    diff_str = ('+{}' if diff >= 0 else '-{}').format(abs(round(diff)))
    return '{} & {} & {} & {}${}$\\\\\n\\hline'.format(
        name.replace('...', '\\dots'), round(old), round(new), cell_color(diff), diff_str)


def table(freqs, i=0, old_range=None, new_range=None):
    start_str = '\\begin{center}\n' \
                '\\begin{tabular}{|c|c|c|c|}\n' \
                '\\hline\n' \
                '\\multicolumn{4}{|c|}{\\textbf{' + levels[i] + '}}\\\\\n' \
                '\\hline\n' \
                'Variation & 1990-1995 & 2019-2020 & \\enspace Change\\enspace\\\\\n' \
                '\\hlineB{4}'
    end_str = '\\end{tabular}\n' \
              '\\end{center}'
    onds = {n: old_new_diff(f, old_range, new_range) for n, f in freqs.items()}
    rows = {n: table_row(n, *ond) for n, ond in onds.items()}
    names_sorted = sorted(freqs.keys(), key=lambda n: onds[n][2], reverse=True)
    strs = [start_str] + [rows[n] for n in names_sorted] + [end_str]
    return '\n'.join(strs)
