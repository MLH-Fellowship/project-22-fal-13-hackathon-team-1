# Site Realiability Engineering - Week 1 - Template Portfolio Site

In week 1, we made a reusable, responsive, scalable template portfolio. We learned new technologies in Web Development (Flask, Jinja, Google Maps API), we also implemented GitHub best practices to collaborate as a team.

# Badges
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MLH-Fellowship/project-22-fal-13-hackathon-team-1?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/MLH-Fellowship/project-22-fal-13-hackathon-team-1?style=plastic)

# Description
This is a portfolio template which can be easily reused and personalized. 

The portfolio template consists of 3 main components:

###### Landing page  
* Hero section with name, call to action button and image
* About Me section with image and text area
* Education section with school image, degree, major

###### Hobbies page 
* Cards with title, image and text area

###### Work Experience page
* Cards with title, image and text area

###### Locations page
* A Google API map that renders points that the user has visited

# Technologies used in the project
The Python microframework Flask
HTML/CSS and Bootstrap
Jinja for templating 
JavaScript for the responsive navigation and map creation
Google Maps API in JavaScript to mark locations visited in each profile page

# File Structure
main
│   README.md                               # Explains this respository
|   LICENSE.md                              # Details of this project's MIT license
│   .gitignore                              # Files to be ignored by git
|   .python-version                         # Python version used to build the project
|   .env                                    # Environmental variables for API key and URL
|   requirements.txt                        # Requirements for Python dependencies to install using pip
│
└───app
    │   __init__.py                         # The Python init file that runs upon executing "flask run"
    │
    └───static
    |   └───fonts
    |   |   |   flux-regular.otf            # The same font style used by Python (free to use)
    |   |
    |   └───img
    |   |   |   (all images for website)    # Various images used in the project
    |   |
    |   └───scripts
    |   |   |   maps.js                     # Script that loads the Google Maps API into the DO
    |   |
    |   └───styles
    |   |   |   main.css                   # Custom styles for all pages
    └───templates
        |___ globaComps 
              | footer.html                # Displays copyright and social links
              | nav.html                   # Responsive navigation menu
        |___ landingPage
              | aboutMe.html               # Template that displays about me information
              | education.html             # Template that displays education section  
              | hero.html                  # Template that hero section  
        |   experience.html                # Template for the experience page
        |   hobbies.html                   # Template for that displays the hobbies page
        |   locations.html                 # Template that displays the Google Map
        |   pageOverlay.html               # Template for overlays in other pages
        |   landingPage.html               # Template that displays the landingPage
        

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. 



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
