

import unittest
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from post.models import Post
# Create your tests here.


class PostTestCase(unittest.TestCase):
    """
    Post application unittests.
    """
    
    def setUp(self):
        """
        Setup environment before each unittest.
        """
        self.client = Client()

    def tearDown(self):
        """
        Clean environment after unittest.
        """
        pass
        
  
    def test_answer_login_page_view(self):
        """
        Sprawdzenie poprawnosci odpowiedzi strony logowania
        """       
        response = self.client.post('/user/login/',{'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200 or 302)
        self.assertIn('Login', response.content)
   
    def test_answer_home_page_view(self):
        """
        Sprawdzenie poprawnosci odpowiedzi strony glownej
        """       
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Books menu', response.content)
        
      
    def test_answer_add_page_view(self):
        """
        Sprawdzenie poprawnosci odpowiedzi strony nowej pozycji
        """       
        response = self.client.post('/add/', follow=True)
        self.assertEqual(response.status_code, 200)      
        self.assertIn('nonauthenticated', response.content)
        
      

    
if __name__ == '__main__':
    unittest.main()
       
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

 
 
 
 
 
 
 
 
 
 
 
 
 
        
'''        
    def test_welcome_of_home_page_view(self):
        """
        Sprawdzenie statusu i zawartosc wyswietlanej przez widok strony
        """
        request = HttpRequest()
        response = PostListView()
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h2>List of books</h2>', response.content)
        self.assertNotIn('<h2>Send List to pdf</h2>', response.data)
'''        
        

    
    
    
    
            
    
'''     
    

    def test_welcome_page(self):
        """
        Checks is username input field on welcome page.
        """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1>Quizer</h1>', resp.data)
        self.assertIn('<input type="text" name="username" />', resp.data)

    def test_welcome_page_empty_username(self):
        """
        Checks validation of username input field.
        """
        resp = self.client.post('/', data={'username': ''})
        self.assertEqual(resp.status_code, 200)
        self.assertIn('<input type="text" name="username" />', resp.data)

    def test_welcome_page_start(self):
        """
        Checks redirect to first question after submit of username.
        """
        username = 'TEST'
        resp = self.client.post('/', data={'username': username})
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(resp.headers['Location'].endswith('/pytanie'))

        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('<p>Witaj, {0}</p>'.format(username), resp.data)

    def test_question_page(self):
        """
        Checks question page.
        """
        resp = self.client.get('/pytanie')
        self.assertEqual(resp.status_code, 200)

    def test_result_page(self):
        """
        Checks result page.
        """
        resp = self.client.get('/wynik')
        self.assertEqual(resp.status_code, 200)
'''