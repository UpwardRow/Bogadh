# Bogadh Introduction
An Irish bus transport full stack project for QA training. 'Bogadh' means 'to move' in Irish

# Project Overview

## Project Brief
The brief for the project at it's current state was to design a Flask web application which provided CRUD functionality from the created database. Tests were needed in this application with a project management tool and a version control system to host the source code. The brief had changed overtime, which affected my project management tool and project design. 

## App Design
Bogadh is a bus transport system for users all across the island of Ireland. It is similar to buying a ticket with the web application for Bus Éireann. A user may have many tickets associated with their account, the user will be able to access this account with their password. The tickets will include a route to differernt parts of the country. The cardinality for Ticket to Customer and Route is many-to-one.

Much of the information for the columns is self explantory. Some columns need some prior knowldge like stage, which means the position of when the customer gets on the bus relative to the destination address from the origin address, route_id is the unique route identifier in each route.

![Bogadh ERD](bogadh_erd_screenshot.png)

## CI Pipeline
As mentioned, the project needed a few stages in it's CI pipeline. In the screenshot below there is a Jira screenshot of this project's board. The board was changed and reconsidered greatly as the marking scheme changed its deliverables. Most of the project has been completed, with descriptions in each Epic containing a child issue with allocated story points and a description. 

![Bogadh Jira](bogadh_jira_screenshot.png)

![Bogadh Design ERD](design_erd_jira.png)

![Bogadh Risk Assessment](risk_assessment_jira.png)

[Link to the Jira board](https://adam-downey.atlassian.net/jira/software/projects/BOG/boards/2/roadmap?timeline=WEEKS)

## Future Development
Passwords are stored directly into the database. This is not secure as it is not hashed. Ideally in the the next sprint, the data would be hashed with bcrypt to increase data privacy.

The login system was designed by me, which took more time than I had. Implementing Flask-Login would have been easier, more realistic, and quicker. In the next sprint redoing this design would be one of my first actions.

Due to a lack of time and error handling within the application for the database relationships, the testing was not attempted. In future sprints testing the application with a high covereage would be a goal. 

