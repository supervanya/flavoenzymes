# flavoenzymes

### Getting Started
1. To run the project create a virtual environment with Python 3.6
    - `virtualenv ENV`
1. Activate the environment
    - `source ENV/bin/activate`
1. Install dependancies
    - `pip install -r requirements.txt`

### Run the pipeline

#### Scraping all the data
> This will try to scrape all the information from all the websites that have been configured. 
If existing file will be found in `./export/scraped-flavoenzymes.json` the programm will only update it if new entries will be found. (it will also make a backup of the existing file and save it with current date in filename) 
- `python scrape-flavoenzymes.py

#### Loading it into Neo4j (coming soon)
