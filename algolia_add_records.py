# algolia_add_records.py
from algoliasearch.search_client import SearchClient

# Algolia credentials
ALGOLIA_APP_ID = "Q8M45RCO3N"
ALGOLIA_ADMIN_API_KEY = "YourAlgoliaAdminAPIKey"  # Replace with your Admin API key (private)
ALGOLIA_INDEX_NAME = "nearest_churches"

def add_records_to_algolia(records):
    """
    Adds a list of church records to the Algolia index.
    Each record must have a unique 'objectID'.
    """
    client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_ADMIN_API_KEY)
    index = client.init_index(ALGOLIA_INDEX_NAME)

    # Save multiple objects to Algolia index (add/update)
    index.save_objects(records, {
        "autoGenerateObjectIDIfNotExist": False
    })
    print(f"Indexed {len(records)} records to Algolia index '{ALGOLIA_INDEX_NAME}'.")

if __name__ == "__main__":
    # Example usage with dummy data - replace or call from nearest_churches.py
    sample_records = [
        {
            "objectID": "example_1",
            "postcode": "SW1A 1AA",
            "name": "Example Church 1",
            "latitude": 51.501009,
            "longitude": -0.141588,
            "_geoloc": {
                "lat": 51.501009,
                "lng": -0.141588
            }
        },
        {
            "objectID": "example_2",
            "postcode": "SW1A 1AA",
            "name": "Example Church 2",
            "latitude": 51.499479,
            "longitude": -0.124809,
            "_geoloc": {
                "lat": 51.499479,
                "lng": -0.124809
            }
        },
    ]

    add_records_to_algolia(sample_records)