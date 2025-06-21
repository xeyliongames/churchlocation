from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points on the Earth."""
    R = 6371  # Radius of the Earth in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Example usage in the script:
for church in churches:
    distance = haversine(lat, lon, church['latitude'], church['longitude'])
    print(f"- {church['name']} at ({church['latitude']}, {church['longitude']}) - {distance:.2f} km away")




Thinking

Researching
243 sources read
Favicon for https://missionalmarketing.com/ai-launchpoint/
Favicon for https://www.xpastor.org/video-library/ai-on-mission-effectively-launching-artificial-intelligence-within-your-church-part-2/
Favicon for https://ai-for-churches.com/church-social-media-strategy-ai-transform-digital-ministry/

Research AI Launch Point's church consulting services and implementation strategies.

Evaluate Beautiful.ai, Presentations.AI, and Gamma's API documentation for church content integration.

Research Google Maps API implementation for church location services.

Investigate hosting requirements for church location website on tiiny.site.

Computing

Load maps_api.json and inspect structure

Gracefully handle missing maps_api.json and create a mock dataset for demonstration

Implement haversine formula and calculate distances from a sample user location

Visualize the locations of user and nearest churches on a map

Save nearest churches as a CSV for web integration or further use

(Final) Prepare a minimal HTML snippet to display nearest churches in a table for static site integration

Responding