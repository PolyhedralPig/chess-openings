from compute import *

total = eco_ranges([
    ('B', 10, 19)
])

groups = compute_groups([
    ('B', 12, 12, '3. e5 (Advance)'),
    ('B', 13, 14, '3. exd5 (Exchange)'),
    ('B', 15, 19, '3. Nc3, Nd2 (Classical)')
], total=total)

names = [
    '3. Nc3, Nd2 (Classical)',
    '3. e5 (Advance)',
    '3. exd5 (Exchange)',
    name_other
]


if __name__ == '__main__':
    run(groups, names, collect=[range(4)])
