import json
from pandas import json_normalize

df = open(r'/CACI-API/CACI-Project/src/fake_profiles.json')

raw_data = json.load(df) #returns a json string

norm_data = json_normalize(raw_data) #Converts from json string to pandas dataframe

print(
    norm_data.info(),
    norm_data.head().T    #Checking the structure of the data provided
)

df.close()