import requests
from algoliasearch.search_client import SearchClient

def fetch_sample_movies():
    url = "https://dashboard.algolia.com/api/1/sample_datasets?type=movie"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def add_records_to_algolia(index_name: str, records: list):
    app_id = "UQYBDBYQUQ"
    api_key = "c79d5fd6d6c1245a450d38e956b85b8b"

    client = SearchClient.create(app_id, api_key)
    index = client.init_index(index_name)

    index.save_objects(records, {'autoGenerateObjectIDIfNotExist': True})

    print(f"Successfully added {len(records)} records to '{index_name}' index.")

if __name__ == "__main__":
    movies = fetch_sample_movies()
    add_records_to_algolia("movies_index", movies)

