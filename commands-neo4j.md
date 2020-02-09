# Neo4j useful commands

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
UNWIND keys(enzymes) AS ec
	MERGE (e:Enzyme {name: ec})
    
    FOREACH (subsName in enzymes[ec].SUBSTRATE | 
    	MERGE (s:Substrate {name: subsName})
        MERGE (s)<-[:binds]-(e)
    )
    
    FOREACH (prodName in enzymes[ec].PRODUCT |
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

#### Specific enzyme with all links
```
MATCH p=(e:Enzyme)-->()
WHERE e.name="ec:1.2.99.7" 
RETURN p
```
