import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

educationData = [
    {
        "school_name": "Harvard University",
        "school_img": "/static/img/education-imgs/aerial-harvard.jpg",
        "degree": "B.S. in Computer Science"
    },
    {
        "school_name": "Massachussets Institute of Technology",
        "school_img": "/static/img/education-imgs/MIT-campus.jpg",
        "degree": "M.S. in Computer Science"
    },
    {
        "school_name": "Major League Hacking | MLH Fellowship",
        "school_img": "/static/img/education-imgs/mlh-logo-color.png",
        "degree": "PHD in Hacking"
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
    {"company_img": "static/img/favicon.ico",
    "company_name": "Major League Hacking",
    "job_title": "Site-Reliability Engineer | Fellow @ MLH",
    "position_type": "Fellowship",
    "date_worked": "Sep 2022 - Dec 2022", 
    "location": "United States",
    "description": [
        "Collaborated with some incredible people, amazing pod leader, and great mentor company.", 
        "Worked on a portfolio project, creating a reusable template for the future.", 
        "Used Python, Flask and Jinja, Bootstrap for styling "
        ],
    },
    {"company_img": "static/img/MLBLogo.png",
    "company_name": "Major League Baseball",
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
    {"company_img": "static/img/logo-Meta.png",
    "company_name": "Meta",
    "job_title": "Production Engineer",
    "position_type": "Full-time",
    "date_worked": "Jun 2020 - Aug 2022", 
    "location": "Menlo Park, California",
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