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
