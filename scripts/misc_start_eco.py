from compute import *

total = eco_ranges([
    ('A', 0, 99),
    ('B', 0, 99),
    ('C', 0, 99),
    ('D', 0, 99),
    ('E', 0, 99)
])

groups = compute_groups([
    ('A', 4, 9, 'Reti'),
    ('A', 10, 39, 'English'),
    ('A', 40, 99, '1. d4'),
    ('B', 0, 99, '1. e4'),
    ('C', 0, 99, '1. e4'),
    ('D', 0, 99, '1. d4'),
    ('E', 0, 99, '1. d4')
], total=total)

names = [
    '1. e4',
    '1. d4',
    'Reti',
    'English'
]


if __name__ == '__main__':
    run(groups, names, collect=[range(4)])
