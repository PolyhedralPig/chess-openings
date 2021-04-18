from compute import *

total = eco_ranges([
    ('C', 44, 99)
])

groups = compute_groups([
    ('C', 45, 45, 'Scotch'),
    ('C', 46, 49, 'Four Knights'),
    ('C', 50, 59, 'Italian'),
    ('C', 60, 99, 'Ruy Lopez')
], total=total)

names = [
    'Ruy Lopez',
    'Italian',
    'Scotch',
    'Four Knights'
]


if __name__ == '__main__':
    run(groups, names, collect=[range(4)])
