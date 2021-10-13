# GALLERY Studio App

#### Author: 
* Peter Gakure

## Visit Live App
* Link to live site: [GALLERY Studio App](https://personalgalapp.herokuapp.com/)


## Description

This is a Django application for personal gallery that allows a user to upload images for other to see. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also search for photos based on the categories.

## User stories
- The home page allows users to see various images:
- User can see all images per location they were taken
- Users can also search for images based categories
- Admin can upload images from a django dashboard

## Technologies Used
    - Python 3.8
    - Django MVC framework
    - HTML, CSS and Bootstrap
    - JavaScript

## Specifications
To view the user dtories or BDD check the [specs file](specs.md).

### Prerequisite
This GALLERY Studio App requires a prerequisite understanding of the following:
- Django Framework
- Python3.8
- Postgres
- Python virtualenv

## Setup and installation

#### Clone the Repo

-Navigate to my github page and clone https://github.com/Gakur/PersonalGalApp.git


## Navigate into the folder
cd PersonalGalleryApp

####  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `python3.8 -m venv --without-pip virtual`
####  Install dependencies
Install dependencies that will create an environment for the app to run `pip freeze -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE galleryapp;

#### Run initial Migration
    ** python3.8 manage.py makemigrations**

    **python3.8 manage.py migrate**
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000

## Known bugs
For now a user cant copy an image and paste it as he/she wants. For assistance eamil me at |'petergakure97@gmail.com'.


## Contributors
    *Peter Gakure

### Contact Information
If you have any question or contributions, please email me at |[petergakure97@gmail.com]

## License 

#### [*MIT*](LICENSE)