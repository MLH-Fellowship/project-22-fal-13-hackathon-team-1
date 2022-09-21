import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def landingPage():
    return render_template('landingPage.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbiesPage():
    return render_template('hobbies.html', title="MLH Fellow - Hobbies", url=os.getenv("URL"))