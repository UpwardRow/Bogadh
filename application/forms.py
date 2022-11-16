from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, DateTimeField
from wtforms.validators import InputRequired
from application.models import Customer, Ticket


# Class is being used to validate the user information being put into the form
class CustomerCredentialsCheck:
    def __init__(self, message=None):
        if not message:
            message = "The password is incorrect"
        self.message = message

    def __call__(self, form, field, auto_invoke=False):

        # This statement is a check to verify if the data entered into either username or password field is equal to db
        if field == form.username:
            other_field = form.password

            password_object = Customer.query.filter_by(password=other_field.data).first()
            username_object = Customer.query.filter_by(customer_username=field.data).first()
        else:
            other_field = form.username

            password_object = Customer.query.filter_by(password=field.data).first()
            username_object = Customer.query.filter_by(customer_username=other_field.data).first()

        # If the password or username is not found in the database, a validation error will be raised
        if password_object is None or username_object is None:
            raise ValidationError(self.message)
        return True


# A validator to make sure that the stage is in the expected range
class StageLimitCheck:
    def __init__(self, message=None):
        if not message:
            message = "Stage must not be above 3, and must be above 0"
        self.message = message

    def __call__(self, form, field):

        stage_object = Ticket.query.filter_by(stage=field.data).first()

        # If the number for stage is above 3 or below 1, a ValidationError will be raised
        if stage_object > 3 or stage_object < 1:
            raise ValidationError(self.message)
        return True


class CustomerCredentials(FlaskForm):
    # WTForms passes the value inputted into the field box as a default parameter 'field', no parameter value needed
    username = StringField("Username", validators=[InputRequired("Username required"),
                                                   CustomerCredentialsCheck(message="Username not found")
                                                   ])

    password = StringField("Password", validators=[InputRequired("Password required"),
                                                   CustomerCredentialsCheck(message="Incorrect password")
                                                   ])
    submit = SubmitField("Login")


# def destination_query():
#     return Route.query

class TicketsBuy(FlaskForm):
    destination = StringField("Destination", validators=[InputRequired("Destination required")])

    comment = StringField("Comment")

    stage = IntegerField("Stage", validators=[StageLimitCheck("The stage is not between 0-4")])

    departure_time_and_date = DateTimeField("departure_time_and_date", format='%Y-%m-%d %H:%M:%S',
                                            validators=[InputRequired()])
