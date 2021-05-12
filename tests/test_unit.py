import unittest
import pytest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Boarders, Tricks

class TestBase(TestCase):
    def create_app(self):       
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app
    
    def setUp(self):
        db.create_all()
        test_boarder = Boarders(boarder_name = "master_skater_1000")

        db.session.add(test_boarder)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_boarder_view_get(self):
        response = self.client.get(url_for('boarder_view'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
       response = self.client.get(url_for('update', id=1), follow_redirects=True)
       self.assertEqual(response.status_code, 200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_trick_view_get(self):
        response = self.client.get(url_for('trick_view'))
        self.assertEqual(response.status_code, 200)

    def test_trick_create_get(self):
        response = self.client.get(url_for('trick_create'))
        self.assertEqual(response.status_code, 200)

    def test_trick_update_get(self):
       response = self.client.get(url_for('trick_update', id=1), follow_redirects=True)
       self.assertEqual(response.status_code, 200)

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


    

    
    