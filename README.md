## **CACI Rest API project**

A Rest API which fetches profiles from a database and in addition to deleting a profile record.

**How the API runs**
The API can be run using your local IDE  through the run.py file or can be deployed on your chosen server

**Endpoints**

The API uses the following methods and url endpoints to fetch or delete data

| Method   | URL End Point    | Summary							   |
|----------|------------------|------------------------------------|
|  	GET	   |  /search/username| Searches for specific person in API|
|  	GET	   |  /people		  | Returns all people  API			   |
|  	DELETE |  /people/username| Deletes a profile from the API	   |

**Swagger UI**

The API also includes a swagger UI that can be loaded through following the steps [here](https://swagger.io/docs/swagger-inspector/how-to-use-swagger-inspector/)
