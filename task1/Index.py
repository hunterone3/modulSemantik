from rdflib import Graph, Literal
from rdflib.plugins.sparql import prepareQuery

g = Graph()
g.parse("countrues_info.ttl", format="turtle")

query = prepareQuery('''
    SELECT ?countryName ?continentName ?languageName ?rank
    WHERE {
        ?country a :Country .
        ?country :country_name ?countryName .
        ?country :part_of_continent ?continent .
        ?continent :continent_name ?continentName .
        ?countryLang :spoken_in ?country .
        ?countryLang :language_value ?language .
        ?language :language_name ?languageName .
        ?countryLang :rank ?rank .
    }
''', initNs={'': 'http://example.com/demo/'})

results = g.query(query)

continent_countries = {}

for row in results:
    country_name = str(row['countryName'])
    continent_name = str(row['continentName'])
    language_name = str(row['languageName'])
    rank = str(row['rank'])
    
    if continent_name not in continent_countries:
        continent_countries[continent_name] = []
    
    country_info = {
        'Country Name': country_name,
        'Language Name': language_name,
        'Rank': rank
    }
    
    continent_countries[continent_name].append(country_info)

for continent, countries in continent_countries.items():
    print(f"Continent: {continent}")
    for country in countries:
        print(f"  Country: {country['Country Name']}")
        print(f"  Language: {country['Language Name']}")
        print(f"  Rank: {country['Rank']}")
