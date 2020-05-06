# flavoenzymes

# TODO:
- Check if dir deletion works on windows
- Make sure env activation work like in readme and post creation text
- 
⚠️ __Important__:
- run all the commands from the root of the repo

## Getting Started
**Prerequisites**
1. You must have Python 3.3 or above.
    - Check whether you do by running `python3 --version` or `python --version`.
1. You must have pip installed.
   - Check whether you do by running `pip3 --version` or `pip --version`

## Quick start
```sh
python3 modules/helpers/env_setup.py
# IMPORTANT: activate your virtual environment using instructions printed from the command above
pip install -r requirements.txt
python3 scrape-flavoenzymes.py
```

If somethign didn't work, follow these step by step instructions:
<details><summary>Step by step</summary>

**Virtual environment setup**
1. Create virtual environment.
    - `python3 modules/helpers/env_setup.py`
1. Activate the virtual environment
    > if you don't, all packages will be installed to your global environment, if you are ok with that, skip this step
    - On MacOS or Linux run:
        - `source flav_env/bin/activate`
    - On Windows run:
        - `flav_env\Scripts\activate.bat`
1. Install dependancies within the environment.
    - `pip install -r requirements.txt`
</details>

## Run the pipeline
Scraping all the data
  > This will try to scrape all the information from all the websites that have been configured. 
If existing file will be found in `./export/scraped_flavoenzymes.json` the programm will only update it if new entries will be found. (it will also make a backup of the existing file and save it with current date in filename) 
  - `python scrape-flavoenzymes.py`



---


## Loading data into Neo4j

<details>
<summary>Here is the list of useful commands to run</summary>

## Importing files

#### Create from URL
```
WITH "https://raw.githubusercontent.com/supervanya/flavoenzymes/master/export/kegg.json" AS url
```

#### Create from local file
```
WITH "kegg.json" AS url
```


#### Create from JSON
if creating from a local file replace link with file name and place file within import folder of Neo4j
```
WITH "https://raw.githubusercontent.com/supervanya/flavoenzymes/master/export/kegg.json" AS url
CALL apoc.load.json(url) YIELD value AS enzymes
UNWIND keys(enzymes) AS enzName
	MERGE (e:Enzyme {name: enzName})
    
    FOREACH (subsName in enzymes[enzName].SUBSTRATE | 
    	MERGE (s:Substrate {name: subsName})
        MERGE (s)<-[:binds]-(e)
    )
    
    FOREACH (prodName in enzymes[enzName].PRODUCT |
    	MERGE (p:Product {name: prodName})
        MERGE (p)<-[:releases]-(e)
    )
```

## Queries

#### Show all nodes (this will limit to 300 or your settings)    
```
MATCH (n) return n
```

#### 25 enzymes with anything they bind 
```
MATCH (n:Enzyme) 
RETURN (n)-[:binds]->()
LIMIT 25
```

#### 25 enzymes with anything they bind and release 
```
MATCH (n)
RETURN ()<-[:releases]-(n)-[:binds]->() 
LIMIT 25
```

#### Specific enzyme with all links
```
MATCH p=(e:Enzyme)-->()
WHERE e.ec="ec:1.2.99.7" 
RETURN p
```

```
MATCH (e:Enzyme)
MATCH path = (e)-[]->(s:Substrate)
RETURN path;
```
</details>   

---

## Other Modules
[BruceSorter:](modules/bruce_sorter/README.md) Sorting flavoenzymes
