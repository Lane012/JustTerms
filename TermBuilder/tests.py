from django.test import TestCase
from django.test import Client

class TestHomePage(TestCase):
    
    def test_home_page_resolves_(self):
        client = Client()
        response = client.get('/')
        
     
    def test_home_page_template_extends_base(self):
        client = Client()
        response = client.get('/')
        self.assertIn("HomePage", response.content.decode())
