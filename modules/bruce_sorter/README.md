# BruceSorter

> BruceSorter was originally written by [Emilly Roberts](https://github.com/emroberts95) and later refactored by [Ivan Prokopovich](https://github.com/supervanya). Name is a reference to the vast knowledge of [Bruce Palfey](https://scholar.google.com/citations?user=xsPM4ecAAAAJ) who had to sort the flavoenzymes so we wrote a CLI to allow him to quickly classify and filter scraped enzymes.

⚠️ __Important__:
- run all the commands from the root of the repo
- This instructions are for UNIX systems
- On windows, replace `/` with`\` when specifying path


## Getting Started:
Before using the Sorter, you need two files:
1. `scraped_flavoenzymes.json` - flavoenzyme data (instructions to generate [here](https://github.com/supervanya/flavoenzymes/tree/master#run-the-pipeline))
2. `flavoenzymes_to_sort.csv` (instructions to generate below)

## Generating the CSV
You can generate csv by running the the `csv_generator.py`

run in terminal:
  - `python3 modules/bruce_sorter/csv_generator.py`
  > This will create a `flavoenzymes_to_sort.csv` in the `export/` folder'
  
<details><summary><b>More Details</b></summary>

if you'd like to use custom input or output file pass it using arguments like so:
  - `python3 modules/bruce_sorter/csv_generator.py -i "path/to/in.json" -o "path/to/out.csv"`


### Generated CSV Format
  
  After running the above lines, you should have a CSV of the following format:

|        ec | SYSNAME         | SUBSTRATE                        | PRODUCT                  | bin | OxidativeHalf | ReductionHalf |
|----------:|-----------------|----------------------------------|--------------------------|-----|---------------|---------------|
| 1.14.13.2 | 3-hydroxylating | ["H+", "NADH", "NADP+", "NADPH"] | ["H2O", "NAD+", "NADP+"] |   0 |               |               |

  </details>


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


