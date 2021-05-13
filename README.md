
# DEVOP CORE FUNDAMENTAL PROJECT
Started 18th April - DevOps Core Fundamental Project - Deadline 17th May

This read.me documents the process from app idea to deployement for my fundamental project.

# Brief
The aim for this project is to create a CRUD application.
The project requirements are:

* Follow an AGILE workflow and use a kanban board. *(Trello board)*

* Use a relational database with atleast two tables. *(MYSQL)*
* Produce a functional CRUD application and front_end website. *(Python and Flask)*
* Carry out and document unit and integration tests. *(Pytest and Selenium)*
* Use a VCS. *(Git and Github)*
* Use a CI Sever. *(Jenkins)*
* Deploy to a cloud-based VM. *(GCP)*

# App Idea
My idea for the application is a 'Tricktionary' app. The app will allow users to create a list of skate tricks for themselves and others.

The app's CRUD functionality can be described in the following user stories:
* As a user I want to __create__ a boarder (skateboarder/longboarder) and assign tricks to this boarder.
* As a user I want to **create** a list of tricks.
* As a user I want to __read__ my list of tricks.
* As a user I want to **update** the name of a trick.
* As a user I want to __delete__ a trick.
* As a user I want to be able to __create__ new boarders.
* As a user I want to be able to __update__ the name of boarders.
* As a user I want to be able to __delete__ boarders.



My previous ideas for the application were also skate related. The ERDs of these ideas can be seen in the documentation folder 
After getting feedback and reflection I modified these ideas so that they would have clearer CRUD functionality and a one to many relationship between two tables. This made my final idea better suited for the brief.


# App Design

## Database Design (ERD)
The database has two tables: **Tricks** and **Boarders** which have a one to many relationship.

(show erd)

The boarders table has two columns: the boarder_id which is the primary key and boarder_name. This table stores the name of the boarder and gives it a id.

The tricks table has three columns: the trick_id which is the primary key, trick_name and fk_boarder_id. The fk_boarder is a foriegn key and is what establishes the one to many relationship. A boarder can have many tricks while a trick can only have one boarder.

## CI Pipeline
(Show the CI pipeline diagram.)
* Kanban Board - For my project I have used a Trello Board as it makes it easy to visualise all the tasks needed ot be done for the whole project and the sprint. MOSCOW prioritisation can easily be assigned so tasks which MUST be done can be clearly seen.

* Version Control System - Git is used as the version control system for this project with github being the host of this repository. Git is chosen becuase it makes it easy to track changes in my application over time. It has also allowed me to work on certain tasks at a time, assigning each of these tasks a new branch, following the main>dev>feature workflow

* Developement Environment - Python and the microframework Flask has been used to develop the application and the front end website. Flask is chosen as it is lightweight but contains all the core features needed to develope needed to develope my application.

* CI Server - Jenkins has been used in this project to automatically poll the main build of the application from github and run tests on the application. 

* Testing - Pytest and Selenium are used for unit and intergration testing respectively.

* Cloud Server - GCP is used to host the application on a virtual machine. 


# Project Management
## Kanban Board Walkthrough and Link
(Link to trello board)
My trello board has a product backlog and a sprint backlog for each sprint, a review and complete backlog. 
Screenshots of the board after each sprint can be found here. (link)

## Sprints breakdown
For the actual project week I simulated each day as a whole sprint. For each 'sprint' I carried out the tasks specified in the trello board which can be seen above.
* Sprint_one = Basic CRUD functionality
* Sprint_two = User_input and forms
* Sprint_three = Unit and intergration testing
* Sprint_four = Automation
* Sprint five = Documentation
## Backlog breakdown - user stories
The specific user stories and tasks can be seen here: link the photos

# App Developement and Testing
## Flask

Explain how the basic crud functionality of the app has been achieved through routes.
Screenshots of the front end.

## App Testing Design and Summary of overall Results, reflection
Screenshot of unit tests.
Pytest is used for unit testing. The unit tests have been written to test each function in the app. The tests assert whether the ouput will be a certain value. For my unit tests I have testing all the CRUD functionality in regards to boarders. (i.e adding, deleting, updating)
The covergae for the unit tests are 84%.
In my next sprint I would like to write unit tests which cover the crud functionality for tricks.
Screenshot of results.
What were the results, coverage.

Intergration testing is used to see how well the backend front end and database work together. 
Selenium is used for intergration testing. I wrote four tests which test the buttons: add a boarder, add a trick. The results can be seen here.

When the user navigates to the home page there are three headings: home, add boarder and add trick. The use can then add a boarder, be navigated to another page where they can add a boarder name. They will then be naviagted to the home page again. Here, after taking note of the boarder id the user can click add trick, taken to add the add trick page and add a trick and specify a board number.


## Jenkins and auaotmation
Jenkins is an open source automation server which can be used as a CI server to build CI pipelines, as a build tool and deployement tool. 

Jenkins was chosen for this project for its freestyle jobs. As the application is light the aim for jenkins is to just automate the testing. I set up a webhook in my github repository. In jenkins I set up a job where everytime there is a push to the main branch, jenkins will run the following script.
The script will first install all dependencies.
Then install python.
Then create the environment
Them run the tests.
The tests can then be seen in the reports. 

The credential plugiin is used here to keep the secret key and databse uri hidden.



# Risk Assessment
A risk assessment has been carried out periodically throughout the project. Here is a link to all screenshots of assessments done. Throughout the project as we learned more about the tools and technologies used, I began to identify different risks and different methods to reduce and stop these risks which can be seen from the first assessment to the last. A good example is...

The final assessment also has a review which states what actually happened.

# Reflection
The project was a success in terms on delivering a MVP in terms of applicaiton, testing and automation tools required. Some points of success where the CRUD functionality and the use of jenkins to automate the test.

Some points to improve on next time are: intergration testing. After seeing my results I realzied that my integration tests which seemed to have passed did not actually do what I intended at all and in this sense they have failed. Form this I have learnt the importance of checking the testing reports. 

Some features I want to implement next. If I had another week to work on this project I would add to the MVP by removing all errors such as if I too long work, give the wrong longboard id. This can be resolved by actually writing error messages into the code and changing to a select form.
