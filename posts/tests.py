from django.test import TestCase
from django.urls import reverse

from .models import Post
# Create your tests here.

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is text')

    def test_homepage_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_view_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class AboutPageViewTest(TestCase):
    def test_aboutpage_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_view_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_template(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is test')
        
    def test_post_add(self):
        post = Post.objects.get(id=1)
        exp_name = f'{post.text}'
        self.assertEqual(exp_name, 'this is test')