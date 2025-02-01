from django.test import TestCase
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('articles:home')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Home page')
        self.assertTemplateUsed(response, 'main/home.html')


class ExhibitionsViewTestCase(TestCase):
    def test_list(self):
        path = reverse('articles:exhibitions')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/exhibition.html')
