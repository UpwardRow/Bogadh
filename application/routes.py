from application import app
# from application.models import Subjects, Staff
from flask import render_template
# from flask import request
# from application.forms import NameForm, exampleSelectField, SubjectList


@app.route('/home')
def home():
    return render_template("homepage.html")
