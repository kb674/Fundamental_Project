
# DEVOPS CORE FUNDAMENTAL PROJECT
Started 18th April

Deadline 17th May

This read.me documents the process of creating my 'Tricktionary' application for my fundamental project.

# Brief
The aim for this project is to create a CRUD application.
The project requirements are:

* Follow an AGILE workflow and use a kanban board. *(Trello board)*

* Use a relational database with atleast two tables. *(MYSQL)*
* Produce a functional CRUD application and front end website. *(Python and Flask)*
* Carry out and document unit and integration tests. *(Pytest and Selenium)*
* Use a VCS. *(Git and Github)*
* Use a CI Sever. *(Jenkins)*
* Deploy to a cloud-based VM. *(GCP)*

# App Idea
My idea for the application is a 'Tricktionary' app. The app will allow users to create a list of skate tricks for themselves or others.

The app's CRUD functionality can be described using the following user stories:
* As a user I want to __create__ a boarder (skateboarder/longboarder) and assign them skate tricks.
* As a user I want to **create** a list of tricks.
* As a user I want to __read__ my list of tricks.
* As a user I want to **update** the name of a trick.
* As a user I want to __delete__ a trick.
* As a user I want to be able to __create__  a new boarder.
* As a user I want to be able to __update__ the name of a boarder.
* As a user I want to be able to __delete__ a boarder.

My previous ideas for the application were also skate related. The ERDs of these ideas can be seen in the documentation folder. (/documention/ERD)
After reflecting on some feedback, I modified these ideas to have a clearer CRUD functionality and a one to many relationship between two tables. This made my final idea better suited for the brief.


# Database Design 
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/ERD%20-%20used.png)


The database has two tables: **Tricks** and **Boarders** which have a one to many relationship.



The boarders table has two columns: the boarder_id which is the primary key and the boarder_name. This table stores the name of a boarder and gives it an id.

The tricks table has three columns: the trick_id which is the primary key, trick_name and fk_boarder_id. The fk_boarder_id is a foriegn key and is what establishes the one to many relationship. A boarder can have many tricks while a trick can only have one boarder.

# CI Pipeline
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/ci%20pipeline.png)

INTRODUCE THE TOPIC, WHAT IS A CI PIPELINE, ETC

* Kanban Board - For my project I am using a Trello Board to easily visualise all the tasks needed to be done for the whole project and for each sprint. Additionally, MOSCOW prioritisation can be clearly assigned so tasks which MUST be done are easily seen.

* Version Control System - Git is used as the version control system for this project with github being the host for this repository. Git is chosen becuase it makes it easy to track changes in my application over time. It has also allowed me to work on certain tasks at a time, assigning each of these tasks a new branch, following the main>dev>feature workflow.

* Developement Environment - Python and the microframework Flask are used to develop the application and the front end website. Flask is chosen as it is lightweight but contains all the core features needed to implement CRUD functionality.

* CI Server - Jenkins is used in this project to automatically run tests whenever a push is made to the main branch of this repository via a webhook. Jenkins will run the script 'test.sh' and produce test reports.

* Testing - Pytest and Selenium are used for unit and intergration testing respectively.

* Cloud Server - GCP is used to host the application on a virtual machine. 

# Agile Worflow
For the actual project week I simulated each day as a whole sprint. For each 'sprint' I carried out the following tasks: 
* Day one/Sprint_one = Basic CRUD functionality
* Day two/Sprint_two = User_input and forms
* Day three/Sprint_three = Unit and Intergration tests
* Day four/Sprint_four = Jenkins and automation
* Day five/Sprint_five = Supporting documentation

Adding onto this, I created a new git branch for each sprint following the main-dev-feature workflow. At the end of the day, when I had completed my tasks I created a pull request and merged the changes from the sprint branch to the dev branch. Finally on the last day, I merged the dev and main branches.

The corresponding tasks which I completed in each sprint can be seen in my trello board (link) or the daily screenshots can be found in documentaion folder/sprint. The screenshots of my trello board at the start and end of the projects are shown below in addition to the user stories and testing tasks.
![Project start](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Sprint1%20-%201.png)
![Project end](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Sprint5%20-%20end.png)
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20User%20Stories%201.png)
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20User%20Stories%202.png)
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/Trello%20-%20Testing%20checklist.png)

# The application 
The current version of the application acts as the minimal viable product and includes create, read, update and delete functionality.

* When navigating to the home page the user will see an emty page with three headers: Home, Add a Boarder and Add a Trick.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%201.png)

* The user can click on 'add a boarder' and be taken to the /create page. Here the user can enter the name of the boarder.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%202.png)

* A new boarders has been added. (Can see their name and ID number)
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%203.png)

* The user can also add a trick by clicking on the Add a Trick button. This will take them to the /trick_create page. The user can then specify the trick and the boarder ID number.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%204.png)

* The user has added a trick.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%205.png)

* By clicking on change name, the name of the boarder can be changed.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%206.png)

* The user has changed the name of the boarder.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%207.png)

* The user can change the name of a trick by clicking the change button found under atrick.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%208.png)

* The trick has been updated.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%209.png)

* Finally, the user can delete a trick by clicking the delete button below the trick.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%2010.png)

* The user can also delete a boarder in a similar manner.
* ![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/front-end%2011.png)

# Current Errors and Future Implementations
As I aimed to build the minimal viable product by the end of the week, this app still contains some errors. If I could continue to work on this project here are the errors and which I would resolve first and features I would improve on:
* When adding a new trick if the user inputs the wrong id this will lead to an error. To resolve this I would implement a select field where instead of inputting an id the user can choose from a list of boarders which exist.
* When changing the name of a boarder, the submit button still reads 'add a boarder'. I want to change this to change name or something similar.
* Overall I would improve the functionality of the app further by making the user a boarder. Then there will a button under the boarder where the user can add a trick. I think this would make the functionality more smoother and intuitive to use for the user.

# Testing 
Testing is the process of analysing the code to find defects. Functional testing aims to identify the functions the application is expected to perform and check whether the application actually carries these out. Both unit testing and intergration testing are types of functional tesing.
Unit testing is used to test units of functionality (i.e functions) while intergration testing is used to test how all layers of the application (database layer, backend, frontend) work toegether.

For my application I have currently written and carried out tests for read, create, update and delete functionality. The general structure of the unit tests assert whether an expected outcome occurs.

In the setup of the unit test, I add a sample boarder to the test database, such that it SHOULD appear in the homepage.
````
 def setUp(self):
        db.create_all()
        test_boarder = Boarders(boarder_name = "master_skater_1000")

        db.session.add(test_boarder)
        db.session.commit()
`````
I then assert that 'master_skater_100' should appear on the home page to test for read functionality.
````
class TestRead(TestBase):
    def test_read_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"master_skater_1000",response.data) 
        
`````
For create functionality, I add the boarder 'master_skate_2000' and assert that this boarder should appear on the homepage.
````
class TestCreate(TestBase):
    def test_create_boarder(self):
        reponse = self.client.post(url_for("create"), 
            data=dict(boarder_name="master_skater_2000"),
            follow_redirects=True)
        self.assertIn(b"master_skater_2000", reponse.data)
`````
The update function test, changes the name of the 'master_skater_1000' to 'master_skater_3000' and asserts that 'master_skater_3000' should appear on the homepage.
````
class TestUpdate(TestBase):
    def test_update_boarder(self):
        reponse = self.client.post(url_for("update", id=1), 
            data=dict(boarder_name="master_boarder_3000"),
            follow_redirects=True)
        self.assertIn(b"master_boarder_3000", reponse.data)
`````
Finally the delete functionality is tested by removing the boarder with the longboard_id of 1 and asserts that 'master_skater_1000' is **not** on the homepage.
````
class TestDelete(TestBase):
    def test_delete_boarder(self):
        reponse = self.client.get(url_for("delete", id=1), 
            follow_redirects=True)
        self.assertNotIn(b"master_skater_1000", reponse.data)        
`````
The results for these tests are shown below in addition to a coverage report.
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/pytest%20-%20coverage%20results.png)

A positive of these results is that the tests achieve a coverage of 82% and tests the CRUD functionality works as it should. A negative is the functionality of adding, updating and deleting a trick is still not covered. If I was to continue the project, I would aim to test this 'trick' functionality by inserting a trick in the setup of the trick and making analogous assertions to what I have done for the boarders.

While these tests are unit tests, they do show how the database layer and backend work together and in that context fall into the defintion of an intergration test. 

Additionally, selenium has also been used to carry out more extensive intergration tests which aimed to test what happens when users click on buttons. In contrast to the unit tests, I have written these tests to also cover the functionaly which deals with the tricks. Selenium uses a webdrive which emulates clicking on submite buttons and writing test.

This first test asserts that when you click on the 'Add a Boarder' button you will be taken the to /create page.
````
class TestAdd(TestBase):
    def add_boarder_button(self):
        button = self.driver.find_element_by_xpath('/html/body/a[2]')
        button.click()
        self.assertEqual(urlfor("create"))
````
This test asserts that when you click on the 'Add a Trick' button you will be taken to the /trick_create page.
````
class TestAdd_trick(TestBase):
    def add_boarder_trick(self):
        button = self.driver.find_element_by_xpath('/html/body/a[3]')
        button.click()
        self.assertEqual(urlfor("trick_create"))
````
This test will click on 'Add a Boarder' and type in 'skate_master_2121'. The test then asserts that the user will then be taken to the home page.

````
class TestAdd_board_enter_name(TestBase):
    def add_boarder_enter_name(self):
        button = self.driver.find_element_by_xpath('/html/body/a[2]')
        button.click()
        field = self.driver.find_element_by_xpath('//*[@id="boarder_name"]')
        field = field.send_keys("skate_master_2121")
        self.assertIn(url_for('home'), field)
 ````
 This test clicks on the 'Add a Trick' button, then adds the trick 'shuv', and a the boarder id 1. The test then asserts that the user will be taken to the home page. 
 ````
class TestAdd_trick_enter_name(TestBase):
    def add_trick_enter_name(self):
        button = self.driver.find_element_by_xpath('/html/body/a[2]')
        button.click()
        field1 = self.driver.find_element_by_xpath('//*[@id="trick_name"]')
        field1 = field1.send_keys("shuv")
        field2 = self.driver.find_element_by_xpath('//*[@id="fk_boarder_id"]')
        field2 = field2.send_keys('1')
        self.assertIn(url_for('home'), field1)
        self.assertIn(url_for('home'), field2)
````

The results show four out four test have passed, not including the test base.
![](https://github.com/kb674/Fundamental_Project/blob/documentation/documentation/pytest%20-%20integration%20results.png)

In order to run the selenium intergration tests, you will have to first install the chomium browser:
````
sudo apt install chromium-browser -y
````
Then install the webdriver with the following commands.
````

sudo apt install wget unzip -y
version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version | grep -oP 'Chromium \K\d+'))
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip
````
After the tests are written you can run the tests in the same way as unit tests by running pytest.

# Automation
Jenkins is an open source automation server which can be used in CI pipelines as a CI server. For this project jenkins was used for its freestyle jobs, in particular to automatically carry out testing and produce reports when a push is made to the main branch of this git repository. 

The was setup by first creating a webhook in this repository. I then linked this repository to my jenkins job and checked the 'GitHub hook trigger for GITScm polling' option to finish setting up the webook on both ends. 

When writing my script (test.sh) I used the credentials plugin for jenkins to keep the database uri and secret key secret. 
My testing script has the following logic:
First install the required tools for the job, i.e python, python virtual environments, python pip3 installer and the chromium browser for selenium to work.
````
sudo apt update
sudo apt install python3
sudo apt install python3-venv
sudo apt install python3-pip

sudo apt install chromium-browser -y
````
Run the commands to create and activate the virtual environment followed by pip3 installing all the dependecies needed for testing.
````
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
````
Then export the environment variables.
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
