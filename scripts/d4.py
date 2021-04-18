"""
Computes frequency of 1. d4 openings.
"""

from compute import *

total = eco_ranges([
    ('A', 40, 99),
    ('D', 0, 99),
    ('E', 0, 99)
])

groups = compute_groups([
    ('D', 10, 19, 'Slav'),
    ('D', 20, 29, 'Queen\'s Gambit Accepted'),
    ('D', 30, 42, 'Queen\'s Gambit Declined'),
    ('D', 43, 49, 'Semi-Slav'),
    ('D', 50, 69, 'Queen\'s Gambit Declined'),
    ('D', 70, 99, 'Grunfeld'),
    ('E', 0, 9, 'Catalan'),
    ('E', 12, 19, 'Queen\'s Indian'),
    ('E', 20, 59, 'Nimzo-Indian'),
    ('E', 60, 99, 'King\'s Indian')
], total=total)

names = [
    'Queen\'s Gambit Declined',
    'Slav',
    'Semi-Slav',
    'Queen\'s Gambit Accepted',
    'Nimzo-Indian',
    'Queen\'s Indian',
    'Catalan',
    'King\'s Indian',
    'Grunfeld',
    name_other
]


if __name__ == '__main__':
    y_limits = ([30] * 9) + [100] + ([30] * 4)
    collect = [range(4), range(4, 9)]
    run(groups, names, y_limits=y_limits, collect=collect)
