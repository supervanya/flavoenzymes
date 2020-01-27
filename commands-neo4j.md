
// Create from URL
`WITH "https://raw.githubusercontent.com/supervanya/flavoenzymes/master/export/kegg.json" AS url`

// Create from local file
`WITH "kegg.json" AS url`


// Create from JSON
```
WITH "kegg.json" AS url
CALL apoc.load.json(url) YIELD value AS enzymes
UNWIND keys(enzymes)[0..10] AS ec
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

// Show them all    
`MATCH (n) return n`

// Partial return
```
MATCH (n:Enzyme) 
RETURN (n)-[:binds]->()
LIMIT 25
```

// Specific enzyme
```
MATCH p=(e:Enzyme)-->()<--()
WHERE e.name="ec:1.2.99.7" 
RETURN p
```