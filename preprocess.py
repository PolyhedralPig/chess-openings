"""
The function year_eco preprocesses a database given as a pgn file.
The output is an array with a row for each year and a column for each of the 500 ECO codes.
Each entry is the number of games with the given ECO code in the given year.
The function year_count preprocesses a database given as a pgn file.
The output is an array with the number of games per year in the database.
"""

import numpy as np
import chess.pgn as p

year_start = 1990
year_end = 2020
years = np.arange(year_start, year_end + 1)


def year_index(year):
    """Returns index of the given year in the output array."""
    return year - year_start


def eco_index(eco):
    """Returns index of the given ECO code (e.g. A00) in the output array."""
    letter = eco[0]
    number = int(eco[1:])
    return (ord(letter) - ord('A')) * 100 + number


def year_eco(pgn_file):
    """See comment at beginning of file."""
    output_2300 = np.zeros((len(years), 500), dtype=np.int_)
    output_2600 = np.zeros((len(years), 500), dtype=np.int_)
    with open(pgn_file, 'r') as pgn:
        headers = p.read_headers(pgn)
        num_games = 0
        while headers:
            if 'ECO' in headers:
                year = int(headers['Date'].split('.')[0])
                eco = headers['ECO']
                white_elo = int(headers['WhiteElo'])
                black_elo = int(headers['BlackElo'])
                # Assuming the database is already filtered for 2300+
                output_2300[year_index(year), eco_index(eco)] += 1
                if white_elo >= 2600 and black_elo >= 2600:
                    output_2600[year_index(year), eco_index(eco)] += 1

            num_games += 1
            if num_games % 10000 == 0:
                print(num_games)
            headers = p.read_headers(pgn)
            '''
            chess.pgn seems to have trouble when the header contains %evp:
            the next header will be read as None even if there are more games in the file.
            Calling read_headers again is a workaround, but I don't know if it works for all pgn files.
            I checked that it works for my pgn files by checking num_games at the end.
            '''
            if not headers:
                headers = p.read_headers(pgn)
        print(num_games)
    return output_2300, output_2600


def year_count(pgn_file):
    """See comment at beginning of file."""
    output_2300, output_2600 = year_eco(pgn_file)
    return np.sum(output_2300, axis=1), np.sum(output_2600, axis=1)


def preprocess_helper(name, preprocess_fn, output_file_format):
    print(name)
    if name == '':
        input_file = 'databases/2300.pgn'
    else:
        input_file = 'databases/positions/{}.pgn'.format(name)
    output_file_2300 = output_file_format.format(name, '2300')
    output_file_2600 = output_file_format.format(name, '2600')
    output_2300, output_2600 = preprocess_fn(input_file)
    np.save(output_file_2300, output_2300)
    np.save(output_file_2600, output_2600)
    print()


def year_eco_helper(name):
    output_file_format = 'preprocessed/eco/{}-{}' if name != '' else 'preprocessed/{}{}'
    preprocess_helper(name, year_eco, output_file_format)


def year_count_helper(name):
    preprocess_helper(name, year_count, 'preprocessed/count/{}-{}')


if __name__ == '__main__':
    # I deleted the pgn files after preprocessing them to save space
    # (except for the London database, which I didn't preprocess)

    # to_eco = [
    #     '',
    #     'e4-sicilian-d6-d4',
    #     'e4-sicilian-e6-d4',
    #     'e4-sicilian-nc6-d4'
    # ]
    # for n in to_eco:
    #     year_eco_helper(n)
    # to_count = [
    #     'e4',
    #     'd4',
    #     'nf3',
    #     'c4',
    #     'd4-main',
    #     'd4-main-bb4',
    #     'd4-main-be7',
    #     'd4-main-c5',
    #     'd4-main-c6',
    #     'd4-main-dxc4',
    #     'd4-nf6-c4',
    #     'd4-nf6-c4-e6',
    #     'd4-nf6-c4-e6-nf3',
    #     'd4-nf6-c4-e6-nf3-b6',
    #     'd4-nf6-c4-e6-nf3-d5',
    #     'd4-nf6-c4-g6',
    #     'd4-nf6-c4-g6-nc3-bg7',
    #     'd4-nf6-c4-g6-nc3-d5',
    #     'e4-berlin-draw',
    #     'e4-berlin-endgame',
    #     'e4-najdorf',
    #     'e4-najdorf-bc4',
    #     'e4-najdorf-be2',
    #     'e4-najdorf-be3',
    #     'e4-najdorf-bg5',
    #     'e4-najdorf-h3',
    #     'e4-sicilian-d6',
    #     'e4-sicilian-d6-d4',
    #     'e4-sicilian-e6',
    #     'e4-sicilian-e6-d4',
    #     'e4-sicilian-g6',
    #     'e4-sicilian-nc6',
    #     'e4-sicilian-nc6-d4',
    #     'e4-sveshnikov-7nd5',
    #     'e4-sveshnikov-9bxf6',
    #     'e4-sveshnikov-9nd5',
    #     'e4-sveshnikov-rossolimo'
    # ]
    # for n in to_count:
    #     year_count_helper(n)
    pass
