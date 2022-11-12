from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import InputRequired
from application.models import Customer


class CustomerCredentials(FlaskForm):
    username = StringField("Username", validators=[InputRequired("Username required")])
    password = StringField("Password", validators=[InputRequired("Password required")])
    submit = SubmitField("Login")

    def validate_username(self, username):
        username_object = Customer.query.filter_by(username=username.data).first()
        if not username_object:
            raise ValidationError("Username was not found")

# class Ticket(FlaskForm):
#     destination_address =
#     stage =
