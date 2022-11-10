from application import db


class Customer(db.Model):
    __tablename__ = 'customer'
    customer_username = db.Column(db.String(20), primary_key=True, nullable=False)
    email = db.Column(db.String(15), primary_key=False, nullable=False)
    # payment_type = db.Column(db.String(15), primary_key=False, nullable=False)
    # password = db.Column(db.String(50), primary_key=False, nullable=False)
    # first_name = db.Column(db.String(50), primary_key=False, nullable=False)
    # last_name = db.Column(db.String(50), primary_key=False, nullable=False)
    tickets = db.relationship('Ticket', backref='customer')


class Ticket(db.Model):
    __tablename__ = 'ticket'
    # ticket_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    # user_comment = db.Column(db.String(100), primary_key=False, nullable=True)
    seat_no = db.Column(db.String(3), primary_key=False, nullable=False)
    # order_date = db.Column(db.datetime, primary_key=False, nullable=False)
    # cost = db.Column(db.decimal, primary_key=False, nullable=False)
    # departure_time_and_date = db.Column(db.datetime, primary_key=False, nullable=False)
    customer_username = db.Column(db.String(20), db.ForeignKey('customer.customer_username'), nullable=False)
    # route_id = db.Column(db.Integer, db.ForeignKey('route.route_id'), nullable=False)


# class Route(db.Model):
#     __tablename__ = 'route'
#     route_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     bus_id = db.Column(db.String(4), primary_key=False, nullable=False)
#     stage = db.Column(db.Integer, primary_key=False, nullable=False)
#     destination_address = db.Column(db.String(100), primary_key=False, nullable=False)
#     origin_address = db.Column(db.String(100), primary_key=False, nullable=False)
#     tickets = db.relationship('Ticket', backref='route')



