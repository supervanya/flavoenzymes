CSVGEN_INPUT=export/combined.json
CSV_FILE=modules/bruce-sorter/flavoenzymes_to_sort.csv


init:
	pip install -r requirements.txt
	echo "== dependencies finished installing == "

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