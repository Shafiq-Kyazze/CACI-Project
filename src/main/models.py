"""Model.py"""

from flask_marshmallow import Marshmallow
from sqlalchemy import Column
from main.init import db




class persona(db.Model):
    #Profiles table to house the data
    __tablename__ = 'persona'
    id = Column(db.Integer, primary_key=True,autoincrement=True)
    username = Column(db.String,unique=True)    #Uniquesness Makes the GET method more effective
    name = Column(db.String)
    sex = Column(db.String)
    address = Column(db.String)
    mail = Column(db.String)
    birthdate = Column(db.Date)
    job = Column(db.String)
    company = Column(db.String)
    ssn = Column(db.String)
    residence = Column(db.String)
    current_location_Latitude = Column(db.Float(8))
    current_location_Longitude = Column(db.Float(8))
    blood_group = Column(db.String)
    website = Column(db.String)

    def __init__(self, username,name,sex,address,mail,birthdate,job,company,ssn,residence,current_location_Latitude,current_location_Longitude,blood_group,website):
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
        self.current_location_Latitude = current_location_Latitude
        self.current_location_Longitude = current_location_Longitude
        self.blood_group = blood_group
        self.website = website

ma = Marshmallow(db)

class persona_schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = persona
        load_instance = True

db.create_all()


