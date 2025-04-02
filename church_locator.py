import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from geopy.geocoders import Nominatim
import numpy as np

# Step 1: Load Dataset
# Replace this with your actual dataset
# Solomon code here
church_postcode = "Enter nearest postcode"
init_postcode = string(church_postcode)
my_postcode = type(init_postcode)
postcodelist = (len(my_postcode)
while postcodelist > 10
print("still searching")
postcodelist = postcodelist -10
else 
print(postcodelist)
#Solomon code here
data = {
    'Postcode': ['EC1A 1BB', 'W1A 0AX', 'SW1A 1AA'],
    'Latitude': [51.5150, 51.5074, 51.5010],
    'Longitude': [-0.1100, -0.1278, -0.1276],
    'Church_Lat': [51.5155, 51.5078, 51.5015],
    'Church_Long': [-0.1105, -0.1282, -0.1280]
}
df = pd.DataFrame(data)

# Step 2: Preprocess Data
# Convert postcodes to coordinates (if not already done)
geolocator = Nominatim(user_agent="church_locator")
def get_coordinates(postcode):
    try:
        location = geolocator.geocode(postcode)
        return (location.latitude, location.longitude)
    except:
        return (None, None)

# Apply geocoding (if needed)
df[['Postcode_Lat', 'Postcode_Long']] = df['Postcode'].apply(lambda x: pd.Series(get_coordinates(x)))

# Drop rows with missing coordinates
df = df.dropna()

# Features and target
X = df[['Postcode_Lat', 'Postcode_Long']]
y = df[['Church_Lat', 'Church_Long']]

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train KNN Model
model = make_pipeline(StandardScaler(), KNeighborsRegressor(n_neighbors=5))
model.fit(X_train, y_train)

# Step 5: Evaluate Model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Step 6: Save Model
import joblib
joblib.dump(model, 'church_locator_model.pkl')
print("Model saved as church_locator_model.pkl")
