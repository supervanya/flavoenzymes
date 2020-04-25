CSVGEN_INPUT=export/combined.json
CSV_FILE=modules/bruce-sorter/flavoenzymes_to_sort.csv


# checkout --> pyenv 
# create the script init.py

init:
	( \
       echo "== removing old virtual environment if exists == "\
       rm -rf ENV;\
       echo "== creating a virtual environment == ";\
       virtualenv ENV;\
       echo "== activating the virtual environment == ";\
       source ENV/bin/activate;\
       echo "== installing dependencies == ";\
       pip install -r requirements.txt;\
       echo "== All done ✅== ";\
    )

activate:
	( \
	source ENV/bin/activate; \
	pip install -r requirements.txt; \
	)

	
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