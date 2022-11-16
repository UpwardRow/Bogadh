from datetime import datetime
import random
from application import app, db
from flask import render_template, request, redirect, url_for, flash
from application.forms import CustomerCredentials, TicketsBuy
from application.models import Ticket, Route, Customer


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
    if request.method == "GET":
        return render_template("tickets_view.html", title="tickets_view")


@app.route('/ticket_buy', methods=['GET', 'POST'])
def ticket_buy():
    tickets_form = TicketsBuy()

    print("Here is the request info " + str(request.method))

    if request.method == "POST":

        # Defining the data to be inputted into the object instances
        destination = tickets_form.destination.data
        comment = tickets_form.comment.data
        stage = tickets_form.stage.data

        # Gets the datetime right now and converts it to a format readable for the database
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        departure_time_and_date = request.form.get("departure_time_and_date")

        seat_no = "A" + str(random.randrange(0, 5)) + str(random.randrange(0, 5))

        # Trying to query the data of bus_id based on the destination entered into the form
        bus_id = db.session.query(Route.bus_id).filter_by(destination_address=destination).first()

        cost = 0

        # Stages are bus stops from the destination address, the later the stage, the less expensive the journey
        if stage == 1:
            cost = 20.50
        elif stage == 2:
            cost = 15.40
        elif stage == 3:
            cost = 10.25

        route_instance = db.session.query(Route).filter_by(route_id="R01").first()
        print(route_instance)
        customer_instance = db.session.query(Customer).filter_by(customer_username="BusRider").first()

        '''
        The route_id is a foreign key in the Ticket table. By connecting the column a route could have many tickets.
        This is similar to customer which has many tickets
        '''
        ticket_to_add = Ticket(user_comment=comment,
                               stage=stage,
                               departure_time_and_date=departure_time_and_date,
                               cost=cost,
                               order_date=order_date,
                               seat_no=seat_no,
                               route=route_instance,
                               customer=customer_instance
                               )

        db.session.add(ticket_to_add)
        db.session.commit()

        flash("Ticket has been purchased")

        return redirect(url_for('tickets_view'))
