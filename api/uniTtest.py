from run import app
import unittest


"""Creating testing class"""
class ApiTest(unittest.TestCase):

    """Checking if search single profile endpoint works"""
    def test_get(self):
        tester = app.test_client(self)  #Configuring Api application for testing
        response = tester.get("/search/<username>") #Obtaining an object from the search person url end point
        statuscode = response.status_code  #Getting the status code of the response object
        self.assertEqual(statuscode, 200)  #Comparing to see if the response return is the success response i.e 200

    """Checking if get all profiles endpoint works"""
    def test_get_all(self):
        tester = app.test_client(self)
        response = tester.get("/people")
        statuscode=response.status_code
        self.assertEqual(statuscode,200)

    """Checking if delete single profile endpoint works"""
    def test_delete(self):
        tester = app.test_client(self)
        response = tester.delete("/people/<username>") #Deleting profile from database
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    """Checking if content returned by API is in json format"""
    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get("/people")
        self.assertEqual(response.content_type, "application/json")

    """Checking if content return by API is in json format"""
    def test_data_returned(self):
        tester = app.test_client(self)
        response = tester.get("/people")
        self.assertTrue(b"Message" not in response.data)  #'Word "Message" not in the data returned


if __name__ == "__main__":   #Running the python file
    unittest.main(verbosity=1)