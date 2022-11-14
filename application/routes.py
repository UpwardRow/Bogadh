from application import app
from flask import render_template, request, redirect
from application.forms import CustomerCredentials


@app.route('/', methods=['GET', 'POST'])
def home():
    # Instantiated object of class UserCredentials
    login_form = CustomerCredentials()

    # This will check if the request is a GET, meaning that the page is just being opened
    if request.method == "GET":
        return render_template("homepage.html", title="home", form=login_form)

    # These statements check if the username matches to one in the database. If so, the user will be taken to tickets
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        return render_template("tickets_view.html", title="home", form=login_form, username=username, password=password)
    else:
        return render_template("homepage.html", title="home", form=login_form, username="", password="")


@app.route('/tickets_view.html', methods=['GET', 'POST'])
def tickets_view():
    return render_template("tickets_view.html", title="tickets_view")
