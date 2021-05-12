from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Boarders, Tricks

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,
            DEBUG=True,
            TESTING=True
        )
        return app
    
    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() 

        self.driver.get(f'http://localhost:{self.TEST_PORT}')


    def tearDown(self):
        self.driver.quit()
        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):

    def add_boarder_button(self):
        button = self.driver.find_element_by_xpath('/html/body/a[2]')
        button.click()
        self.assertEqual(urlfor("create"))

    def add_boarder_button(self):
        button = self.driver.find_element_by_xpath('/html/body/a[3]')
        button.click()
        self.assertEqual(urlfor("trick_create"))
        
    def add_boarder_enter_name(self):
        button = self.driver.find_element_by_xpath('/html/body/a[2]')
        button.click()
        field = self.driver.find_element_by_xpath('//*[@id="boarder_name"]')
        field = field.send_keys("skate_master_2121")
        self.assertIn(url_for('home'), field)



        

            

