from compute import *

total = eco_ranges([
    ('C', 0, 19)
])

groups = compute_groups([
    ('C', 1, 1, '3. exd5 (Exchange)'),
    ('C', 2, 2, '3. e5 (Advance)'),
    ('C', 3, 9, '3. Nd2 (Tarrasch)'),
    ('C', 10, 19, '3. Nc3')
], total=total)

names = [
    '3. Nc3',
    '3. Nd2 (Tarrasch)',
    '3. e5 (Advance)',
    '3. exd5 (Exchange)'
]


if __name__ == '__main__':
    run(groups, names, collect=[range(4)])
