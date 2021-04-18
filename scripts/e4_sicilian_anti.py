from compute import *

total = eco_ranges([
    ('B', 20, 99)
])

groups = compute_groups([
    ('B', 22, 22, 'Alapin'),
    ('B', 23, 26, 'Closed'),
    ('B', 30, 31, 'Rossolimo'),
    ('B', 32, 39, 'Open'),
    ('B', 41, 49, 'Open'),
    ('B', 51, 52, 'Moscow'),
    ('B', 56, 99, 'Open')
], total=total)

names = [
    'Open',
    'Alapin',
    'Closed',
    'Rossolimo',
    'Moscow'
]


if __name__ == '__main__':
    run(groups, names, collect=[range(5)])
