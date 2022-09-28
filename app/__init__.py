import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_googlemaps import GoogleMaps, Map, icons

load_dotenv()
app = Flask(__name__)

os.getenv("API_KEY") 

jsonData = open('app/data/data.json')
data = json.load(jsonData) # turns json into regular dict with obj

#Landing Page
@app.route('/')
def landingPage():
    context = {
        "educationData": data["educationData"]
    }
    return render_template('landingPage.html', title="MLH Fellow", url=os.getenv("URL"), **context)

# Hobbies
@app.route('/hobbies')
def hobbiesPage():
    context={
        "hobbyData": data["hobbyData"]
    }
    return render_template('hobbies.html', title="MLH Fellow - Hobbies", url=os.getenv("URL"), **context)

# Work Experience
@app.route('/experience')
def experiencePage():
    context={
        "experienceData": data["experienceData"]
    }
    return render_template('experience.html', title="MLH Fellow - Experience", url=os.getenv("URL"), **context)


#Location route
@app.route('/locations/')
def mapview():
    context = {
        "locationData": data["locationData"]
    }
    return render_template('locations.html', title="MLH Fellow - Locations", url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"),  **context)
