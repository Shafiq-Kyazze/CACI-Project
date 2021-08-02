# **CACI Rest API project**

- [ ] A Rest API which fetches profiles from a database and in addition to deleting a profile record.
- [ ] The Restful API can be found in the api folder.
- [ ] The data folder contians a simple data pipeline and dat folder depicting data being uploaded to the database after the api created the Data model


#### **How the API runs**

- [ ] The API can be run using your local IDE such as pycharm. 
- [ ] The API contains a run.py file in the api folder which has to be executed to deploy the API on your local server(computer)



#### **Endpoints**

The API uses the following methods and url endpoints to fetch or delete data

| Method   | URL End Point    | Summary							   |
|----------|------------------|------------------------------------|
|  	GET	   |  /search/username| Searches for specific person in API|
|  	GET	   |  /people		  | Returns all people  API			   |
|  	DELETE |  /people/username| Deletes a profile from the API	   |



**Swagger UI**

The API also includes a swagger UI that can be loaded through following the steps as shown [here](https://swagger.io/docs/swagger-inspector/how-to-use-swagger-inspector/)
