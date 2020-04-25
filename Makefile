CSVGEN_INPUT=export/combined.json
CSV_FILE=export/flavoenzymes_to_sort.csv


# checkout --> pyenv 
# create the script init.py

init:
	python helpers/env_setup.py

scrape:
	echo "== running the scrapers == "
	python scrape-flavoenzymes.py

csv:
	python modules/bruce-sorter/csv_generator.py --ifile $(CSVGEN_INPUT) --ofile $(CSV_FILE)

sort:
	python modules/bruce-sorter/BruceSorter_485.py  --ifile $(CSV_FILE)

clean_cache:
	rm export/cache.json
	echo "== cache has been cleaned == "