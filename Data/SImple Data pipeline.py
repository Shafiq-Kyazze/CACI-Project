import json
from pandas import json_normalize
import psycopg2
import psycopg2.extras as ex

DATABASE_URI = "postgresql://username@password/database"
connection = psycopg2.connect(DATABASE_URI)
conn = connection


 #OPening json string file
raw_json = open(r'/media/shafiq/New Volume/Dropbox/CACI-API/CACI-Project/Data/fake_profiles.json')   #File location
raw_data = json.load(raw_json)  #Reads the json file

#Manipulating data using pandas
df = json_normalize(raw_data) #Converts from json format to pandas dataframe
df['current_Latitude'] = df.current_location.apply(lambda x: x[0])
df['current_Longitude'] = df.current_location.apply(lambda x: x[1])
df =df[['username','name','sex','address','mail','birthdate','job','company','ssn','residence','current_Latitude','current_Longitude','blood_group','website']] #rearrange to match format in API model
tuple_data = list(map(tuple, df.to_numpy()))

#Using psycopg to upload data
cur = conn.cursor() #Creating cursor
ex.execute_batch(cur,
                 "INSERT INTO persona(username,name,sex,address,mail,birthdate,job,company,ssn,residence,current_Latitude,current_Longitude,blood_group,website)  values(%s ,%s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple_data
                 )
conn.commit()
conn.close()

#Closing json file
raw_json.close()