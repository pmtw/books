# encoding: utf-8
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class AddPost(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        User.objects.create_user(username='1234',
                                      password='4321',
                                      email='info@info.com')

    def tearDown(self):
        self.browser.quit()

    def test_adding_post_without_logging(self):
        # Kuba próbuje wejść na stronę logowania książki bez logowania
        self.browser.get(self.live_server_url+"/add")
        self.browser.set_window_size(1024, 768)
        self.assertEqual(self.browser.current_url, self.live_server_url+"/login")

    def test_adding_post_after_logging(self):
        # Czarek pracę ze stroną zaczyna od logowania
        self.browser.get(self.live_server_url+"/login")
        self.browser.set_window_size(1024, 768)
        self.assertIn('Login', self.browser.title)

        user_input = self.browser.find_element_by_id('username')
        user_input.send_keys('1234')
        passwd_input = self.browser.find_element_by_id('password')
        passwd_input.send_keys('4321')
        passwd_input.send_keys(Keys.ENTER)

        self.browser.get(self.live_server_url+"/add")
        self.browser.set_window_size(1024, 768)
        self.assertIn('Add post', self.browser.title)
        self.fail('write me')
        