from application import app
from application.models import Customer, Ticket
from flask import render_template, request
from application.forms import CustomerCredentials


@app.route('/home', methods=['GET', 'POST'])
def home():
    # Instantiated object of class UserCredentials
    login_form = CustomerCredentials()

    if login_form.validate_on_submit():
        if request.method == 'POST':
            check_customer = Customer(customer_username=login_form.username.data,
                                      customer_password=login_form.password.data)

            return "I did something?"

    return render_template("homepage.html")
