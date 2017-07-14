#!flask/bin/python
import unittest
from flask.ext.testing import TestCase
from app import create_app, db
from app.model import Users
from flask import request, url_for
import flask

class BaseTestCase(TestCase):

    def create_app(self):
        self.app = create_app('testing')
        return self.app
