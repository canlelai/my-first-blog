from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from blog.views import cv

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')

    def test_post_list_returns_correct_html(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn("<title>Canle's CV</title>", html)
        self.assertTrue(html.strip().endswith('</html>'))
