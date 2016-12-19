from django.test import TestCase
from splinter import Browser


class TestBaseViews(TestCase):

    def setUp(self):
        self.browser = Browser('chrome')

    def tearDown(self):
        self.browser.quit()

    def test_home(self):
        self.browser.visit('http://localhost:8000')
        if self.browser.is_text_present('[tosp]'):
            self.assertTrue(True)
            print("Si entra al home")
        else:
            self.assertTrue(False)

    def test_mantra(self):
        self.browser.visit('http://localhost:8000')
        if self.browser.is_text_present('Be Open. Be Source.'):
            self.assertTrue(True)

    def test_robots(self):
        self.browser.visit('http://localhost:8000/robots.txt')
        if self.browser.is_text_present('robotstxt'):
            self.assertTrue(True)

    def test_humans(self):
        self.browser.visit('http://localhost:8000/humans.txt')
        if self.browser.is_text_present('humanstxt'):
            self.assertTrue(True)
