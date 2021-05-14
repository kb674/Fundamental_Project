
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
*Sprint_one = Basic CRUD functionality

*![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20User%20Stories%201.png)

*Sprint_two = User_input and forms

*![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20User%20Stories%202.png)

*Sprint_three = Unit and intergration testing

*![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20Testing%20checklist.png)

*Sprint_four = Automation

*Sprint five = Documentation


# App Developement and Testing

## App Testing Design and Summary of overall Results, reflection
Testing is used to find the errors in the code before the final application is deployed to end users. There are many categories of testing including: non-functional, functional and maintence testing. For this project, two types of functional tests are required to be carried out, unit tests and intergration tests.
Pytest is used for the unit testing. Unit tests are written to test each function in the app by asserting whether the ouput will be a certain value. For my unit tests I have aimed to test all the CRUD functionality in regards to 'boarders', I.E adding, deleting and updating the boarders. My unit tests can be seen below.
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
The results for these tests are shown below in addition to a coverage report.
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/pytest%20-%20coverage%20results.png)
While the results produce a coverage of 82%, this only means that 82% of lines were covered. As my application is currently the MVP (minimal viable product) it still has some errors.

Intergration testing is used to see how all sections of the application from front end to back end work together. For this, selenium is used. My tests have been designed to test what happens when a user clicks on the 'add boarder' and 'add trick' buttons. Additionally I have also written tests for when the user enters a boarder name and trick name. 

````
class TestAdd(TestBase):
    def add_boarder_button(self):
        button = self.driver.find_element_by_xpath('/html/body/a[2]')
        button.click()
        self.assertEqual(urlfor("create"))

class TestAdd_trick(TestBase):
    def add_boarder_trick(self):
        button = self.driver.find_element_by_xpath('/html/body/a[3]')
        button.click()
        self.assertEqual(urlfor("trick_create"))

class TestAdd_board_enter_name(TestBase):
    def add_boarder_enter_name(self):
        button = self.driver.find_element_by_xpath('/html/body/a[2]')
        button.click()
        field = self.driver.find_element_by_xpath('//*[@id="boarder_name"]')
        field = field.send_keys("skate_master_2121")
        self.assertIn(url_for('home'), field)

class TestAdd_trick_enter_name(TestBase):
    def add_trick_enter_name(self):
        button = self.driver.find_element_by_xpath('/html/body/a[2]')
        button.click()
        field1 = self.driver.find_element_by_xpath('//*[@id="trick_name"]')
        field1 = field1.send_keys("skate_master_2121")
        field2 = self.driver.find_element_by_xpath('//*[@id="fk_boarder_id"]')
        field2 = field2.send_keys('1')
        self.assertIn(url_for('home'), field1)
        self.assertIn(url_for('home'), field2)
````

The results of the tests.
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/pytest%20-%20integration%20results.png)

## The application front-end
* When navigating to the home page the user will see an emty page with three headers: Home, Add a Boarder and Add a Trick.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%201.png)

* The user can click on 'add a boarder' and be taken to the /create page. Here the user can enter the name of the boarder.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%202.png)

* Here you can see the new boarders name and their ID number.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%203.png)

* The user can also add a trick by clicking on the Add a Trick button. This will take them to the /trick_create page. Here the user specify the trick and the boarder ID number.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%204.png)

* The user has added a trick.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%205.png)

* By clicking on change name, the user can update the name of the boarder. 
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%206.png)

* The user has changed the name of the boarder.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%207.png)

* The user can change the name of a trick by clicking the change button under the trick.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%208.png)

* The trick has been updated.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%209.png)

* Finally, the user can delete a trick by clicking the delete button below the trick.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%2010.png)

* The user can also delete a boarder in a similar manner.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%2011.png)


## Jenkins and auaotmation
Jenkins is an open source automation server which can be used in CI pipelines as a CI server. For this project jenkins was used for its freestyle jobs, in particular to automatically carry testing when a push is made to the main branch of this repository. First, I set up the webhook for this repository. I then linked this repository to my jenkins job and checked the GitHub hook trigger for GITScm polling to finish setting up the webook on both end. 

When writing my script (test.sh) I used the credentials plugin for jenkins to keep the database uri and secret key secret. My testing script has the following logic:
First install the required tools for the job, i.e python, python virtual environments, python pip3 installer and the chromium browser for selenium to work.
````
sudo apt update
sudo apt install python3
sudo apt install python3-venv
sudo apt install python3-pip

sudo apt install chromium-browser -y
````
Following this the script will then run commands to create and activate the virtual environment followed by pip3 installing all the dependecies needed for testing.
````
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
````
Then the environment variables are exported.
````
export DATABASE_URI
export SECRET_KEY
````

Finally, the tests are run which will produce coverage reports.
````
python3 -m pytest --doctest-modules --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html
````

# Risk Assessment
First assessment

A risk assessment has been carried out periodically throughout the project. Here is a link `to the final document. (Screenshots of the assessment throughout the project can be found in the documentation folder) Throughout the project as we learned more about the tools and technologies used, I began to identify different risks and different methods to reduce and stop these risks which can be seen from the first assessment to the last. A good example of this is learning about the importance of keeping database URIs and secret keys private. In the case of secret keys, these are used to stop CRSF attacks.


The final assessment also has a review which states what actually happened. (Link risk assessment)

# Reflection
At the current stage of the project I have used all the tools specified in the brief and have developed an application (MVP) which has the main CRUD functionality. The testing has a ahchieved above 75% coverage and jenkins has been used to automate this testing. If i was to carry on in this project some implementations I would like to make next are:
* Resolving the error which occurs when a user types in a trickname or boarder name which is too long. Print an error message with instructions on what to do next.
* Resolve the error if the user does not enter the correct boarder ID number. Use a drop down form.
*  Change the submit button the cupdate boarder when the user tries to update the boarders name. (can be seen below that the button says add a boarder)
*  Once these changes are done I would write more comprehensive tests to achive a higher coverage.
*  Overall I would write more thoroguh integration tests to make sure each button functonality is working like it should, something lacking at this point.
