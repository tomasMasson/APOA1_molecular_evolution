#!/usr/bin/env python3

import argparse
import more_itertools as mit

def apr_distribution(data, score):
    
    with open(data, 'r') as fh:
        next(fh)
        residues = [float(row.split()[5]) for row in fh]
    score = score

    regions = [ index
            for index, res in enumerate(residues, 1)
            if res >= score]
    
    apr = []
    for group in mit.consecutive_groups(regions):
        group = list(group)
        position = (group[-1] + group[0]) // 2
        length = group[-1] - group[0] + 1
        apr.append([position, length])
    
    return apr

def main():
    ''' Command line argument parser. '''

    parser = argparse.ArgumentParser()
    parser.add_argument('data', help='file with TANGO output')
    parser.add_argument('score', type=int, help='Aggregation score minimum threshold')
    args = parser.parse_args()
    data, score = args.data, args.score
    results = apr_distribution(data, score)
    for row in results:
        print(f'{row[0]},{row[1]}')

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(repr(error))