from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import InputRequired, Length
from application.models import Customer


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


class CustomerCredentials(FlaskForm):
    # WTForms passes the value inputted into the field box as a default parameter 'field', no parameter value needed
    username = StringField("Username", validators=[InputRequired("Username required"),
                                                   CustomerCredentialsCheck(message="Username not found")
                                                   ])

    password = StringField("Password", validators=[InputRequired("Password required"),
                                                   CustomerCredentialsCheck(message="Incorrect password")
                                                   ])
    submit = SubmitField("Login")


# class Ticket(FlaskForm):
#     destination_address =
#     stage =
