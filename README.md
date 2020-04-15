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

### Loading data into Neo4j (coming soon)

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
