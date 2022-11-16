# Bogadh Introduction
An Irish bus transport full stack project for QA training. 'Bogadh' means 'to move' in Irish

## Project Brief
The brief for the project at it's current state was to design a Flask web application which provided CRUD functionality from the created database. Tests were needed in this application with a project management tool and a version control system to host the source code. The brief had changed overtime, which affected my project management tool and project design. 

## App Design
Bogadh is a bus transport system for users all across the island of Ireland. It is similar to buying a ticket with the web application for Bus Éireann. A user may have many tickets associated with their account, the user will be able to access this account with their password. 

[Bogadh ERD](bogadh_erd_screenshot)


## Future Development
Passwords are stored directly into the database. This is not secure as it is not hashed. Ideally in the the next sprint, the data would be hashed with bcrypt to increase data privacy


