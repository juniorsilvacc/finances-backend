import uuid
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from categories.models import Category
from rest_framework.test import APIClient


class CategoryAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.category_1 = Category.objects.create(title="Despesas")
        self.category_2 = Category.objects.create(title="Salário")

        # Definindo as URLs dinamicamente
        self.list_create_url = reverse('category-create-list')
        self.detail_url = reverse('category-detail-update-destroy', kwargs={'pk': self.category_1.id})
        self.invalid_detail_url = reverse('category-detail-update-destroy', kwargs={'pk': uuid.uuid4()})

    def test_create_category(self):
        data = {
            'title': 'Investimento',
        }
        response = self.client.post(self.list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Investimento')

    def test_list_categories(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_detail_category(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.category_1.title)

    def test_detail_category_not_found(self):
        response = self.client.get(self.invalid_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_category(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Category.DoesNotExist):
            self.category_1.refresh_from_db()

    def test_update_category(self):
        data = {
            'title': 'Despesas Atualizado',
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.category_1.refresh_from_db()
        self.assertEqual(self.category_1.title, 'Despesas Atualizado')

    def test_update_category_not_found(self):
        response = self.client.put(self.invalid_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
