import sys
import getopt
import os
from pathlib import Path


import json
import pandas as pd


def get_kwards(argv):
    inputfile     = Path('export/combined.json').absolute()
    outputfile    = Path('export/flavoenzymes_to_sort.csv').absolute()
    cwd = Path.cwd().absolute()
    cfd = Path(__file__).parent.absolute()
    if cwd == cfd:
        print('WARNING: you are running this file not from the root of the project, did you mean to do that? You can manually pass the arguments to this program, see instructions here: https://github.com/supervanya/flavoenzymes')
        inputfile    = Path('../../export/combined.json').resolve()
        outputfile   = Path('../../export/flavoenzymes_to_sort.csv').resolve()

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

    # make sure path exists
    folder = outputfile.parent.absolute()
    if not folder.exists():
        Path(folder).mkdir(parents=True, exist_ok=True)

    # outputting the df
    df.to_csv(outputfile, index=False)
    print(f'✅ Success! Written out a csv to "{outputfile}""')

if __name__ == "__main__":
    inputfile, outputfile = get_kwards(sys.argv[1:])
    main(inputfile, outputfile)
