# Fundamental_Project
Started 18th April - DevOps Core Fundamental Project - Deadline 17th May

# DEVOP CORE FUNDAMENTAL PROJECT
This read.me documents the process from app idea to final reflection for my fundamental project.
# Brief
The aim for this project is to create a CRUD application using the technologies, tools and methods taught in training with the following requirements:

* Follow an AGILE workflow and use a kanban board. *(Trello board)*

* Relational database with atleast two tables *(MYSQL)*
* A functional CRUD application and front_end website. *(Python and Flask)*
* Unit and integration tests. *(Pytest and Selenium)*
* Use a VCS. *(Git and Github)*
* Use a CI Sever. *(Jenkins)*
* Deploy to a cloud-based VM. *(GCP)*

# App Idea
My final idea for the project is a tricktionary app. The goal for this app is to allow users to add boarders (as in skateboarder or longboarder) and add a list of tricks for the boarder. The app can be used by the user to write a personal trick list or a list of tricks they would like to achieve.

The CRUD functionality of the application is described below as user stories:

* As a user I want to be able to **create** a list of skate tricks.

* As a user I want to be able to __read__ my list of tricks.

* As a user I want to be able to **update** the list by adding and removing tricks.
* As a user I want to **delete** tricks from the list.

GO OVER OLD IDEAS, WHY YOU CHANGED
My initial idea for this application was also to allow users to create a skateline (a list of tricks), however this design did not allow for a clear CRUD functionality. (erd shown below)

I changed this idea which would allow users to create a list of skate tricks and longboard tricks. ERD shown below. After some reflection I changed my idea again to have a clearer one to many relationship and ended up with my final idea.

Overall these changes have resulted in my final idea which better suits the brief.

# App Design
## Database Design (ERD)
The database for this app has two tables: a **Tricks** table and a **Boarders** table. The ERD of the database can be seen below followed by a representation of the tables themselves. (Insert images)

The table **Trick** stored the tricks specified by a user. The trick would've be assigned an trick_id and a user would have also specified whether the trick was a longboard trick. If the trick was, then the longboard column would have been the boolean value True and would have been added to the table **Longboard**.

## CI Pipeline
This project used the following CI Pipeline: (Insert image)
* Trello for the kanban board. User stories were put up here.
* Git and Github for the version control system. Changes were pushed and pulled from a central repository.
* Python for app development. Specifically using the microframework: Flask.
* Jenkins for automation.
* Pytest and selenium for unit and intergration testing.
* GCP for cloud hosting.

## Testing
Pytest was used to write and carry out the unit tests for the flask application. Selenium was used for intergration testing.
# Project Management
## Kanban Board Walkthrough and Link

## Sprints breakdown
## Backlog breakdown
# Risk Assessment
## Diagram
# App Testing Design and Summary of overall Results
# App Developement
# Reflection