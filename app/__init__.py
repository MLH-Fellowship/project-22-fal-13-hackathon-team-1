import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_googlemaps import GoogleMaps, Map, icons
import json

load_dotenv()
app = Flask(__name__)

os.getenv("API_KEY") 

@app.route('/')
def landingPage():
    return render_template('landingPage.html', title="MLH Fellow", url=os.getenv("URL"))

# Hobbies data
hobbyData = [
    {"imgSrc": "/static/img/logo.jpg",
    "name": "Photography", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur convallis orci nulla, id dignissim diam vulputate a. Ut ullamcorper, ex et elementum posuere, arcu ante vulputate risus, non aliquet augue metus eget enim. Sed auctor non nibh eget porttitor. Aliquam consectetur ipsum eget mi tempus tempus. "},
    {"imgSrc": "/static/img/logo.jpg", 
    "name": "Hiking", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur convallis orci nulla, id dignissim diam vulputate a. Ut ullamcorper, ex et elementum posuere, arcu ante vulputate risus, non aliquet augue metus eget enim. Sed auctor non nibh eget porttitor. Aliquam consectetur ipsum eget mi tempus tempus. "},
    {"imgSrc": "/static/img/logo.jpg", 
    "name": "Dancing", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur convallis orci nulla, id dignissim diam vulputate a. Ut ullamcorper, ex et elementum posuere, arcu ante vulputate risus, non aliquet augue metus eget enim. Sed auctor non nibh eget porttitor. Aliquam consectetur ipsum eget mi tempus tempus. "},
    {"imgSrc": "/static/img/logo.jpg", 
    "name": "Programming", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur convallis orci nulla, id dignissim diam vulputate a. Ut ullamcorper, ex et elementum posuere, arcu ante vulputate risus, non aliquet augue metus eget enim. Sed auctor non nibh eget porttitor. Aliquam consectetur ipsum eget mi tempus tempus. "}
]

@app.route('/hobbies')
def hobbiesPage():
    context={
        "hobbyData": hobbyData
    }
    return render_template('hobbies.html', title="MLH Fellow - Hobbies", url=os.getenv("URL"), **context)
locationData = [
    {"country": "Canada", "lat": 45.421532, "long": -75.697189},
    {"country": "Argentina", "lat": -34.603683, "long": -58.381557},
    {"country": "Mexico", "lat": 19.432608, "long": -99.133209},
    {"country": "US", "lat": 38.9071923, "long": -77.0368707},
    {"country": "Brazil", "lat": -15.793889, "long": -47.882778},
    {"country": "Panama", "lat": 8.983333, "long": -79.516670},
    {"country": "Dominican Republic", "lat": 18.483402, "long": -69.929611},
    {"country": "Jamaica", "lat": 18.017874, "long": -76.809904},
    {"country": "Paraguay", "lat": -25.263740, "long": -57.575926},
    {"country": "UK", "lat": 51.509865, "long": -0.118092},
    {"country": "France", "lat": 48.864716, "long": 2.349014},
    {"country": "Spain", "lat": 40.416775, "long": -3.703790}
]

#Location route
@app.route('/locations/')
def mapview():
    context = {
        "locationData": locationData
    }
    return render_template('locations.html', title="MLH Fellow - Locations", url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"),  **context)
