import sys
import getopt
import os
from pathlib import Path


import json
import pandas as pd


def get_kwards(argv):
    cwd = Path.cwd()
    print(cwd)
    print()

    inputfile  = '../../export/combined.json'
    outputfile = '../../export/flavoenzymes_to_sort.csv'

    infres = Path(inputfile).absolute()
    res = Path.resolve(infres)
    print('lots of info:')
    # print(res)
    # print(Path().absolute())
    # print(Path(__file__).parent.absolute())
    # print(Path(__file__).absolute())
    print(Path(infres).relative_to(cwd))

    help = 'Please use the following format:\npython csv_generator.py -i <inputfile> -o <outputfile>'
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    return Path(inputfile), Path(outputfile)


def read_json_data(path):
    with open(path) as json_file:
        return json.load(json_file)


def main(inputfile, outputfile):
    # reading and creating df from combined data
    flavoenzyme_data = read_json_data(inputfile)
    df = pd.DataFrame(flavoenzyme_data.values(), index=flavoenzyme_data.keys())

    # processing the df
    df.reset_index(inplace=True)
    df.dropna()
    df.rename(columns={'index': 'ec'}, inplace=True)

    df['SUBSTRATE'] = df['SUBSTRATE'].map(json.dumps)
    df['PRODUCT'] = df['PRODUCT'].map(json.dumps)

    df['bin'] = 0
    df['OxidativeHalf'] = 0
    df['ReductionHalf'] = 0

    # outputting the df
    df.to_csv(outputfile, index=False)
    print(f'✅ Success! Written out a csv to "{outputfile}""')

if __name__ == "__main__":
    inputfile, outputfile = get_kwards(sys.argv[1:])
    # main(inputfile, outputfile)
