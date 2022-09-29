import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_googlemaps import GoogleMaps, Map, icons
import json

load_dotenv()
app = Flask(__name__)

os.getenv("API_KEY") 
educationData = [
    {
        "school_name": "Major Leauge Hacking | MLH Fellowship",
        "school_img": "/static/img/education-imgs/mlh-logo-color.png",
        "degree": "Certificate: Site Realiability Software Engineering"
    },
    {
        "school_name": "Techtonica",
        "school_img": "/static/img/education-imgs/techtonica.png",
        "degree": "Certificate: Software Engineering"
    },
    {
        "school_name": "University Massachussetts, Lowell",
        "school_img": "/static/img/education-imgs/uMassLowell.png",
        "degree": "Bachelor of Science: Information Technology"
    },
    {
        "school_name": "California State University, Chico",
        "school_img": "/static/img/education-imgs/chicoState3.jpg",
        "degree": "Bachelor of Science: Parks and Natural Resources"
    },
]


@app.route('/')
def landingPage():
    context = {
        "educationData": educationData
    }
    return render_template('landingPage.html', title="MLH Fellow", url=os.getenv("URL"), **context)

# Hobbies data
hobbyData = [
    {"imgSrc": "/static/img/rivers.jpg",
    "name": "Rafting", 
    "description": "Rivers hold a special place in my heart. My favorite rivers are the Trinity, American, Sacramento, Yuba and the Yampa River in Utah"},
    {"imgSrc": "/static/img/backpacking.jpg", 
    "name": "Backpacking", 
    "description": "The wilderness is a place that I go to rejuvenate. Naturalist John Muir best summed it up in his writings, “Climb the mountains and get their good tidings. Nature's peace will flow into you as sunshine flows into trees. The winds will blow their own freshness into you, and the storms their energy, while cares will drop away from you like the leaves of Autumn.”"}
]

@app.route('/hobbies')
def hobbiesPage():
    context={
        "hobbyData": hobbyData
    }
    return render_template('hobbies.html', title="MLH Fellow - Hobbies", url=os.getenv("URL"), **context)

#Location Data
locationData = [
    {"country": "Canada", "lat": 45.421532, "long": -75.697189},
    {"country": "Mexico", "lat": 19.432608, "long": -99.133209},
    {"country": "US", "lat": 38.9071923, "long": -77.0368707},
    {"country": "Belize", "lat": 17.1899, "long": 88.4976},
    {"country": "Guatemala", "lat": 15.7835, "long": 90.2308},
]

#Location route
@app.route('/locations/')
def mapview():
    context = {
        "locationData": locationData
    }
    return render_template('locations.html', title="MLH Fellow - Locations", url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"),  **context)

# Experience data
experienceData = [
    {"company_img": "static/img/favicon.ico",
    "company_name": "Major League Hacking",
    "job_title": "Site-Reliability Engineer | Fellow @ MLH",
    "position_type": "Fellowship",
    "date_worked": "Sep 2022 - Dec 2022", 
    "location": "United States",
    "description": [
        "Collaborated with pod members to create a portfolio template." 
        "Worked on a portfolio project, creating a reusable template for the future.", 
        "Used Python, Flask and Jinja, Bootstrap for styling "
        ],
    },
    {"company_img": "static/img/indeed.png",
    "company_name": "Indeed.com",
    "job_title": "Site-Reliability Engineer",
    "position_type": "Full-time",
    "date_worked": "Sep 2022 - Present", 
    "location": "New York, New York",
    "description": [
        "Collaborated with some incredible people, amazing pod leader, and great mentor company.", 
        "Worked on a portfolio project, creating a reusable template for the future.", 
        "Used Python, Flask and Jinja, Bootstrap for styling "
        ],
    },
    {"company_img": "static/img/techtonica.jpg",
    "company_name": "Techtonica",
    "job_title": "Software Engineer Apprentice",
    "position_type": "Full-time",
    "date_worked": "Jul 2021 - Dec 2021", 
    "location": "Remote (based in San Francisco)",
    "description": [
        "Learned new technologies under a deadline, developed and deployed full-stack applications using PostgreSQl, Express, React, Node.", 
        "Worked on a portfolio project, creating a reusable template for the future.", 
        "Used Python, Flask and Jinja, Bootstrap for styling "
        ],
    },
]

# Work Experience
@app.route('/experience')
def experiencePage():
    context={
        "experienceData": experienceData
    }
    return render_template('experience.html', title="MLH Fellow - Experience", url=os.getenv("URL"), **context)
