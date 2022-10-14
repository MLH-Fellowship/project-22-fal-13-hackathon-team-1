import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_googlemaps import GoogleMaps, Map, icons
#for sql connection
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import requests

load_dotenv()
app = Flask(__name__)

#MySQL DB
mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)
print(mydb)

#peewee model
    #Create a "timeline post" data table
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

#Timeline data 
    #POST
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

    #GET
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

    #DELETE by Username
@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    # deleteUser = input("Enter Post User: ")
    post = TimelinePost.get(TimelinePost.name == "Test")
    post.delete_instance()
    #return remaining posts
    return print(f"Deleted User: {deleteUser}")

#for '/data/json' to become dict
jsonData = open('app/data/data.json')
data = json.load(jsonData)

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


#fetch timeline post data

# print(response, response.json())

#Timeline route
@app.route('/timeline')
def timelinePage():
    response = requests.get("http://localhost:5000/api/timeline_post")
    context={
        "timelineData": [response.json()]
    }
    return render_template('timeline.html', title="MLH Fellow - Timeline", url=os.getenv("URL"), **context)