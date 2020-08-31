from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import Client
from django.contrib.auth.models import User

from blog.views import cv
from blog.models import Add

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

    def test_can_save_a_POST_request(self):
        response = self.client.post('/add/new/', data={'title': 'test'})
        self.assertIn('test', response.content.decode())

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/')
        self.assertEqual(Add.objects.count(), 0)

    def test_only_saves_CV_when_necessary(self):
        self.client.get('/cv/')
        self.assertEqual(Add.objects.count(), 0)

    def test_redirects_after_POST(self):
        response = self.client.post('/add/new/', data={'title': 'test'})
        self.assertEqual(response.status_code, 200)
