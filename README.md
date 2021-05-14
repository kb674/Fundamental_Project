
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



My previous ideas for the application were also skate related. The ERDs of these ideas can be seen in the documentation folder. (/documention/ERD)
After getting feedback and reflection I modified these ideas so that they would have clearer CRUD functionality and a one to many relationship between two tables. This made my final idea better suited for the brief.


# App Design

## Database Design (ERD)
The database has two tables: **Tricks** and **Boarders** which have a one to many relationship.

![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/ERD%20-%20used.png)

The boarders table has two columns: the boarder_id which is the primary key and the boarder_name. This table stores the name of a boarder and gives it an id.

The tricks table has three columns: the trick_id which is the primary key, trick_name and fk_boarder_id. The fk_boarder_id is a foriegn key and is what establishes the one to many relationship. A boarder can have many tricks while a trick can only have one boarder.

## CI Pipeline
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/ci%20pipeline.png)

* Kanban Board - For my project I have used a Trello Board as it makes it easy to visualise all the tasks needed ot be done for the whole project and the sprint. MOSCOW prioritisation can easily be assigned so tasks which MUST be done can be clearly seen.

* Version Control System - Git is used as the version control system for this project with github being the host of this repository. Git is chosen becuase it makes it easy to track changes in my application over time. It has also allowed me to work on certain tasks at a time, assigning each of these tasks a new branch, following the main>dev>feature workflow

* Developement Environment - Python and the microframework Flask has been used to develop the application and the front end website. Flask is chosen as it is lightweight but contains all the core features needed to implement CRUD functionality.

* CI Server - Jenkins has been used in this project to automatically run tests whenever a push is made to the main branch of this repository via a webhook. Jenkins will run the script in test.sh and produce test reports.

* Testing - Pytest and Selenium are used for unit and intergration testing respectively.

* Cloud Server - GCP is used to host the application on a virtual machine. 


# Project Management
## Kanban Board Walkthrough and Link
![](https://trello.com/b/CJe8Yb4T/01fundamentalproject)
My trello board has a product backlog and a sprint backlog for each sprint, a review and complete backlog. 
Screenshots of the board at the beggining and at the end of the project are shown below.
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Sprint1%20-%201.png)
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Sprint5%20-%20end.png)
Screenshots after each sprint can be founds in the documents folder. (Screenshots will start with sprint and trello)



## Sprints breakdown
For the actual project week I simulated each day as a whole sprint. For each 'sprint' I carried out the following tasks: 
* Sprint_one = Basic CRUD functionality
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20User%20Stories%201.png)

* Sprint_two = User_input and forms
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20User%20Stories%202.png)
* Sprint_three = Unit and intergration testing
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20Testing%20checklist.png)
* Sprint_four = Automation
* Sprint five = Documentation

# App Developement and Testing

## App Testing Design and Summary of overall Results, reflection

Pytest is used for unit testing. Unit tests are written to test each function in the app by asserting whether the ouput will be a certain value. For my unit tests I have aimed to test all the CRUD functionality in regards to 'boarders', I.E adding, deleting and updating the boarders. My unit tests can be seen below.
```
class TestRead(TestBase):
    def test_read_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"master_skater_1000",response.data) 

class TestCreate(TestBase):
    def test_create_boarder(self):
        reponse = self.client.post(url_for("create"), 
            data=dict(boarder_name="master_skater_2000"),
            follow_redirects=True)
        self.assertIn(b"master_skater_2000", reponse.data)

class TestUpdate(TestBase):
    def test_update_boarder(self):
        reponse = self.client.post(url_for("update", id=1), 
            data=dict(boarder_name="master_boarder_3000"),
            follow_redirects=True)
        self.assertIn(b"master_boarder_3000", reponse.data)

class TestDelete(TestBase):
    def test_delete_boarder(self):
        reponse = self.client.get(url_for("delete", id=1), 
            follow_redirects=True)
        self.assertNotIn(b"master_skater_1000", reponse.data)
        
```



written all the CRUD functionality in regards to boarders, (i.e adding, deleting, updating)
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

The final assessment also has a review which states what actually happened. (Link risk assessment)

# Reflection
The project was a success in terms on delivering a MVP in terms of applicaiton, testing and automation tools required. Some points of success where the CRUD functionality and the use of jenkins to automate the test.

Some features I want to implement next. If I had another week to work on this project I would add to the MVP by removing all errors such as if I too long work, give the wrong longboard id. This can be resolved by actually writing error messages into the code and changing to a select form.
