import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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

# Hobbies data
experienceData = [
    {"company-img": "static/img/Portrait_Placeholder.png",
    "job-title": "Site-Reliability Engineer | Fellow @ MLH",
    "position-type": "Fellowship",
    "date-worked": "Sept 2022 - Dec 2022", 
    "location": "United States",
    "description": [
        "Collaborated with some incredible people, amazing pod leader, and great mentor company.", 
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