# BruceSorter

> BruceSorter was originally written by [Emilly Roberts](https://github.com/emroberts95) and later refactored by [Ivan Prokopovich](https://github.com/supervanya). Name is a reference to the vast knowledge of [Bruce Palfey](https://scholar.google.com/citations?user=xsPM4ecAAAAJ) who had to sort the flavoenzymes so we wrote a CLI to allow him to quickly classify and filter scraped enzymes.

Before using the Sorter, you must:
1. run the pipeline to generate the `scraped_flavoenzymes.json`
1. generate the `flavoenzymes_to_sort.csv.csv` (instructions below)

## Running the BruceSorter
to run the sorter, simply run:
  - `python modules/bruce_sorter/BruceSorter_485.py`

you can specify which file to sort by passing an argument:
  - `python modules/bruce_sorter/BruceSorter_485.py -i "path/to/enzymes.csv"`

while running the sorter, you can specify answer by typing the first letter of the answer.
```python
==> Reduction Half Reactions
Options: etrans(e)   thiol(t)   htrans(h)  other   idk
Type 'naf' to mark as non-flavin
Type 'exit' to exit
> 
```
you can type in `e` to answer `etrans`

## Generating the CSV
This project includes a comand line interface to sort through a `.csv` file of the following format (the data is not complete, this is just a sample):
|        ec | SYSNAME         | SUBSTRATE                        | PRODUCT                  | bin | OxidativeHalf | ReductionHalf |
|----------:|-----------------|----------------------------------|--------------------------|-----|---------------|---------------|
| 1.14.13.2 | 3-hydroxylating | ["H+", "NADH", "NADP+", "NADPH"] | ["H2O", "NAD+", "NADP+"] |   0 |               |               |

### You can generate csv by running the the `csv_generator.py`

run in terminal:
  - `python3 modules/bruce_sorter/csv_generator.py`
  > This will output a csv to the `export` folder

if you'd like to use custom input or output file pass it using arguments like so:
  - `python3 modules/bruce_sorter/csv_generator.py -i "path/to/in.json" -o "path/to/out.csv"`

