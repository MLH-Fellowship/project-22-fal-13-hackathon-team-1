import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_googlemaps import GoogleMaps, Map, icons
from peewee import*
import datetime
import json
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)
                   
print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = mydb
        
mydb.connect()
mydb.create_tables([TimelinePost])




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
    "description": "Rivers hold a special place in my heart. My favorite rivers are the Trinity, American, Sacramento, Yuba and the Yampa River in Utah. I love exploring the geology of the river."},
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
    {"country": "Canada", "lat": 53.7267, "long": -127.6476},
    {"country": "Mexico", "lat": 19.432608, "long": -99.133209},
    {"country": "US", "lat": 36.7783, "long": -119.4179},
    {"country": "Belize", "lat": 17.1899, "long": -88.4976},
    {"country": "Guatemala", "lat": 15.7835, "long": -90.2308}
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
        "Collaborated with pod members to create a portfolio template using Flask, Jinja and Bootstrap.",
        "Deployed personal portfolio on virtual private server using Linux"
        ],
    },
    {"company_img": "static/img/indeed.png",
    "company_name": "Indeed.com",
    "job_title": "Software Developer Intern",
    "position_type": "Full-time",
    "date_worked": "Jan 2022 - Jul 2022", 
    "location": "Remote (based in San Francisco)",
    "description": [
        "Completed production-level tickets using React and TypeScript", 
        "Created and refactored unit and integration tests", 
        "Collaborated with cross-functional team members on optimizing integration tests, peer code review and team processes"
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
        "Collaborated with teammates on debugging code, peer code review and implementing new features", 
        "Led team meetings of 12+ coworkers and facilitated daily agenda items "
        ],
    },
    {"company_img": "static/img/pr.jpg",
    "company_name": "Pleasant Ridge School District",
    "job_title": "Teacher",
    "position_type": "Full-time",
    "date_worked": "Aug 2000 - Jun 2014", 
    "location": "Grass Valley, California",
    "description": [
        "Science department chair (August 2010 - June 2014)", 
        "Designed and implemented performance improvement plans for students in consultation with parents and administrative staff", 
        "Contributed to improving statewide standardized testing scores for 8th grade science by 7% during tenure. "
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

# timeline
@app.route('/timeline')
def timeline():
    timeline_posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.
    created_at.desc())]
    return render_template('timeline.html', title="MLH Fellow - Timeline", url=os.getenv("URL"), timeline_posts=timeline_posts)

# timeline POST route 
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email,content=content)
    return model_to_dict(timeline_post)

#timeline GET route
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
    
