"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name='Whiskey', species="dog", photo_url="", age="3", notes="like to bark", available="true")
bowser = Pet(name='Bowser', species="dog", photo_url="", age="3", notes="like to bark", available="true") 
spike = Pet(name='Spike', species="porcupine",  photo_url="", age="3", notes="like to bark", available="true")

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# Commit--otherwise, this never gets saved!
db.session.commit()
