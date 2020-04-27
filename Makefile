CSVGEN_INPUT=export/combined.json
CSV_FILE=export/flavoenzymes_to_sort.csv


# checkout --> pyenv 
# create the script init.py
init:
	( \
       python modules/helpers/env_setup.py;\
       source flav_env/bin/activate;\
       pip install -r requirements.txt;\
    )

scrape:
	source flav_env/bin/activate && python scrape_flavoenzymes.py

csv:
	python modules/bruce_sorter/csv_generator.py --ifile $(CSVGEN_INPUT) --ofile $(CSV_FILE)

sort:
	python modules/bruce_sorter/BruceSorter_485.py  --ifile $(CSV_FILE)

clean_cache:
	rm export/cache.json
	echo "== cache has been cleaned == "