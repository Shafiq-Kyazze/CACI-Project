"""Model file which contains the Data models to be uploaded in the database.
THe file also includes the schema"""

from flask_marshmallow import Marshmallow
from sqlalchemy import Column
from main.init import db

ma = Marshmallow(db)    #Marshmallow instance

# Persona Data model
class persona(db.Model):
    __tablename__ = 'persona_profiles'
    id = Column(db.Integer, primary_key=True,autoincrement=True)
    username = Column(db.String)    #Uniquesness Makes the GET method more effective
    name = Column(db.String)
    sex = Column(db.String)
    address = Column(db.String)
    mail = Column(db.String)
    birthdate = Column(db.Date)
    job = Column(db.String)
    company = Column(db.String)
    ssn = Column(db.String)
    residence = Column(db.String)
    current_latitude = Column(db.Float(8))
    current_longitude = Column(db.Float(8))
    blood_group = Column(db.String)
    website = Column(db.String)

    """Making sure all the atttributes in the class object are filled in during the post method if there was one"""
    def __init__(self, username,name,sex,address,mail,birthdate,job,company,ssn,residence,current_latitude,current_longitude,blood_group,website):
        self.username = username
        self.name = name
        self.sex = sex
        self.address = address
        self.mail = mail
        self.birthdate = birthdate
        self.job = job
        self.company = company
        self.ssn = ssn
        self.residence = residence
        self.current_latitude = current_latitude
        self.current_longitude = current_longitude
        self.blood_group = blood_group
        self.website = website


#Schema
class persona_schema(ma.Schema):  #Automatically generates fields
    class Meta:
        model = persona
        fields = ('username','name','sex','address','mail','birthdate','job','company','ssn','residence','current_Latitude','current_Longitude','blood_group','website')



db.create_all()  #Creating the persona data model

