"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

from django.test import TestCase
from django.test.client import Client

class CityViewTest(TestCase):
  def test_index_should_redirect_to_default_city(self):
    response = self.client.get('/')
    self.failUnlessEqual(response.status_code, 302)
    self.failUnlessEqual(response['location'], 'http://testserver/florianopolis/')

  def test_current_city_should_set_city_on_cookies(self):
    response = self.client.get('/florianopolis/')
    self.failUnlessEqual(response.cookies['current_city'].value, 'florianopolis')

  def test_index_should_redirect_to_current_city(self):
    self.client.get('/rio-de-janeiro/')
    response = self.client.get('/')
    self.failUnlessEqual(response.status_code, 302)
    self.failUnlessEqual(response['location'], 'http://testserver/rio-de-janeiro/')

class DealViewTest(TestCase):
  fixtures = ['deals.yaml']

  def test_current_city_should_show_current_deal(self):
    response = self.client.get('/florianopolis/')
    self.failUnlessEqual(response.status_code, 302)
    self.failUnlessEqual(response['location'], 'http://testserver/florianopolis/deals/60-em-2-chopps/')

  def test_current_city_should_show_subscribe_when_deal_not_found(self):
    response = self.client.get('/rio-de-janeiro/')
    self.failUnlessEqual(response.status_code, 302)
    self.failUnlessEqual(response['location'], 'http://testserver/rio-de-janeiro/subscribe/')

