import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_googlemaps import GoogleMaps, Map, icons
import json

load_dotenv()
app = Flask(__name__)

GoogleMaps(app, key=os.getenv("GOOGLEMAPSAPIKEY"))

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

#Location route
@app.route("/locations/<location>")
def mapview(location):
    data = load_profiles_from_json('locationData.json')
    if location in data:
        info = data[location]
        return render_template('locations.html', title="MLH Fellow - Locations",location=location, info=info, url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"))
    else:
        return landingPage()
    
def load_profiles_from_json(filename) -> dict:
    # Get the relative path for the JSON data
    path = f'{os.getcwd()}/{filename}'
    # Open the file and return its parsed contents
    # UTF-8 encoding is used to parse apostrophes correctly
    with open(path, "r", encoding='utf8') as file:
        return json.load(file)