from application import db, app
from application.models import Customer, Ticket

with app.app_context():
    db.drop_all()
    db.create_all()

    my_dictionary = {'BusRider': 'A03', 'WheelerMann': 'A21', 'TravelGav': 'B05'}
    email_list = ['phoneyadam@gmail.com', 'mrexample2022@gmail.com', 'inboxcrook@hotmail.com']

    default_customers = [{'customer_username': 'Busrider', 'email', 'payment_type', 'password', 'first_name':'Adam', 'last_name': 'Downey'}]

    print(my_dictionary.values())

    for cust in default_customers:
        customer = Customer(customer_username=cust.customer_username)
        db.session.add(customer)
    db.session.commit()

    for cust, seat in my_dictionary.items():
        ticket = Ticket(seat_no=seat, customer_username=cust)
        db.session.add(ticket)
    db.session.commit()

    for e in email_list:
        email = Customer(email=e)
        db.session.add(email)
    db.session.commit()

    # Checks if the customer_username is a foreign key, which it is
    var1 = Ticket.query.join(Customer).all()
    for i in var1:
        print(i.seat_no + ' ' + i.customer.customer_username)
