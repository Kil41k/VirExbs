from django.test import TestCase
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('articles:home')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Exhibitions list')
        self.assertTemplateUsed(response, 'main/index.html')
