import pandas as pd
import numpy as np

#Load the dataset
data = pd.read_csv("datasets/flood_prediction_dummy_data_final.csv")

#Define the locations
locations_in_chennai = ["T. Nagar", "Adyar", "Velachery", "Anna Nagar", 
"Mylapore", "Porur", "Nungambakkam", "Kodambakkam", "Thiruvanmiyur", "Perambur"]

# Mapping of flood-prone areas to their fixed coordinates
coord = {
    "Velachery": (12.9814, 80.2182),
    "T. Nagar": (13.0405, 80.2337),
    "Kodambakkam": (13.0485, 80.2250),
    "Adyar": (13.0063, 80.2574),
    "Mylapore": (13.0336, 80.2605),
    "Anna Nagar": (13.0846, 80.2195),  
    "Porur": (13.0389, 80.1569), 
    "Nungambakkam": (13.0619, 80.2423),  
    "Thiruvanmiyur": (12.9830, 80.2595),  
    "Perambur": (13.1120, 80.2315) 
}

# Assign locations and their respective coordinates with deviation
data['Location Name'] = np.random.choice(locations_in_chennai, size=len(data))
deviation = 0.001  # Set the deviation for latitude and longitude
#each entry x has a longitude that is based on its location, with a small random deviation added
data['Latitude'] = data['Location Name'].map(lambda x: coord[x][0] + np.random.uniform(-deviation, deviation))
data['Longitude'] = data['Location Name'].map(lambda x: coord[x][1] + np.random.uniform(-deviation, deviation))

#Generate random geographic coordinates
chennai_latitude = np.random.uniform(12.9200, 13.2400, size=len(data))
chennai_longitude = np.random.uniform(80.1234, 80.2700, size=len(data))

# Adjust the ranges for environmental variables based on your specified data
data['Location Name'] = np.random.choice(locations_in_chennai, size=len(data))
data['Temperature (°C)'] = np.random.uniform(20.32, 36.96, size=len(data))
data['Relative Humidity (%)'] = np.random.uniform(60.15, 89.81, size=len(data))
data['Wind Speed (km/h)'] = np.random.uniform(0.07, 39.97, size=len(data))
data['Topography (elevation in meters)'] = np.random.uniform(0.05, 9.97, size=len(data))
data['Soil Moisture Content (%)'] = np.random.uniform(10.24, 99.82, size=len(data))
data['River Water Level (meters)'] = np.random.uniform(0.11, 9.90, size=len(data))
data['Urbanization Rate (%)'] = np.random.uniform(1.63, 99.85, size=len(data))
data['Drainage System Capacity (cubic meters/second)'] = np.random.uniform(0.18, 495.33, size=len(data))
data['Rainfall Amount (mm)'] = np.random.uniform(1.66, 296.07, size=len(data))
data['Previous Flood History'] = np.random.choice([0, 1], size=len(data), p=[0.5, 0.5])  # Assuming a 50/50 chance for simplification
# Add Flood Event column - randomly assign for demonstration
data['Flood Event'] = np.random.choice([0, 1], size=len(data), p=[0.7, 0.3])  # 70% no flood, 30% flood

#Save the cleaned data to a new CSV file
data.to_csv("datasets/backup/test.csv", index=False)
