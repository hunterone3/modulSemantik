from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
sparql.setQuery("""
SELECT DISTINCT ?actor ?actorLabel ?characterLabel ?movieLabel
WHERE {
  ?actor wdt:P27 wd:Q212. 
  ?movie p:P161 [
    ps:P161 ?actor;
    pq:P453 ?character
  ];
  wdt:P31/wdt:P279* wd:Q11424. 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    actor = result["actorLabel"]["value"]
    character = result["characterLabel"]["value"]
    movie = result["movieLabel"]["value"]
    print(f"Актор: {actor} | Фільм: {movie} | Роль: {character}")
