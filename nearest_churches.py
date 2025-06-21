import time
import requests
from daytona_sdk import (
    Daytona,
    DaytonaConfig,
    CreateSnapshotParams,
    CreateSandboxFromSnapshotParams,
    Resources,
)
from PIL import Image as PILImage

def get_geocode(postcode):
    """Geocode postcode to get latitude and longitude."""
    url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if data["status"] == 200:
        return data["result"]["latitude"], data["result"]["longitude"]
    else:
        raise ValueError(f"Invalid postcode: {postcode}")

def find_nearest_churches(lat, lon, radius_km=5):
    """Find nearest churches within radius using Overpass API."""
    radius_m = radius_km * 1000
    query = f"""
    [out:json][timeout:25];
    (
      node["amenity"="place_of_worship"]["religion"="christian"](around:{radius_m},{lat},{lon});
      way["amenity"="place_of_worship"]["religion"="christian"](around:{radius_m},{lat},{lon});
      relation["amenity"="place_of_worship"]["religion"="christian"](around:{radius_m},{lat},{lon});
    );
    out center;
    """
    url = "http://overpass-api.de/api/interpreter"
    response = requests.post(url, data={"data": query})
    response.raise_for_status()
    data = response.json()
    churches = []
    for element in data.get("elements", []):
        name = element.get("tags", {}).get("name", "Unnamed Church")
        lat_ = element.get("lat") or element.get("center", {}).get("lat")
        lon_ = element.get("lon") or element.get("center", {}).get("lon")
        churches.append({"name": name, "latitude": lat_, "longitude": lon_})
    return churches

def main():
    postcode = input("Enter postcode: ").strip()

    try:
        lat, lon = get_geocode(postcode)
        print(f"Coordinates for {postcode}: {lat}, {lon}")
    except Exception as e:
        print(f"Error geocoding postcode: {e}")
        return

    churches = find_nearest_churches(lat, lon)
    if not churches:
        print("No churches found nearby.")
    else:
        print(f"Found {len(churches)} churches nearby:")
        for church in churches:
            print(f"- {church['name']} at ({church['latitude']}, {church['longitude']})")

    # Initialize Daytona client with string target region (no enum)
    config = DaytonaConfig(target="eu")
    daytona = Daytona(config)

    # Prepare example image for snapshot creation (blank white)
    image = PILImage.new("RGB", (200, 200), color="white")

    # Create snapshot
    snapshot_name = f"python-example:{int(time.time())}"
    snapshot_params = CreateSnapshotParams(
        name=snapshot_name,
        image=image,
        resources=Resources(cpu=1, memory=1, disk=3),
    )
    daytona.snapshot.create(snapshot_params, on_logs=print)

    # Create sandbox from snapshot
    sandbox_params = CreateSandboxFromSnapshotParams(snapshot=snapshot_name, language="python")
    sandbox = daytona.create(sandbox_params)
    print(f"Sandbox created with ID: {sandbox.id}")

    # Refresh sandbox to update properties directly
    sandbox.refresh_data()

    # Access updated sandbox info via flattened properties
    print(f"Refreshed Sandbox state: {sandbox.state}")
    print(f"Refreshed Sandbox auto stop interval: {sandbox.auto_stop_interval}")
    print(f"Refreshed Sandbox runner domain: {sandbox.runner_domain}")

if __name__ == "__main__":
    main()