from compute import *

total = eco_ranges([
    ('B', 0, 99),
    ('C', 0, 99)
])

groups = compute_groups([
    ('B', 10, 19, 'Caro-Kann'),
    ('B', 20, 99, 'Sicilian'),
    ('C', 0, 19, 'French'),
    ('C', 20, 99, '1... e5')
], total=total)

names = [
    'Sicilian',
    '1... e5',
    'French',
    'Caro-Kann',
    name_other
]


if __name__ == '__main__':
    run(groups, names, collect=[range(4)])
