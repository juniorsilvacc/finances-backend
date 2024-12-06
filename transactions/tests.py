from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from transactions.models import Category, Transaction


class TransactionAPICreateViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Despesas")
        self.client = APIClient()

    def test_create_income_transaction(self):
        data = {
            'title': 'Salário',
            'type': 'income',
            'value': 5000.00,
            'category': self.category.id
        }
        response = self.client.post('/api/v1/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Salário')
        self.assertEqual(response.data['type'], 'income')

    def test_create_outcome_transaction(self):
        data = {
            'title': 'Gasolina',
            'type': 'outcome',
            'value': 400.00,
            'category': self.category.id
        }
        response = self.client.post('/api/v1/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Gasolina')
        self.assertEqual(response.data['type'], 'outcome')

    def test_create_transaction_value_invalid(self):
        data = {
            'title': 'Gasolina',
            'type': 'outcome',
            'value': -500.00,
            'category': self.category.id
        }
        response = self.client.post('/api/v1/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn('O valor da transação deve ser maior que zero.', str(response.data))

    def test_create_transaction_type_invalid(self):
        data = {
            'title': 'Suplementação',
            'type': 'invalid',
            'value': 500.00,
            'category': self.category.id
        }
        response = self.client.post('/api/v1/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("O tipo de transação deve ser 'income' ou 'outcome'.", str(response.data))


class TransactionAPIListViewTest(TestCase):

    def setUp(self):
        self.category_1 = Category.objects.create(title="Salário")
        self.category_2 = Category.objects.create(title="Alimentação")
        self.transaction_1 = Transaction.objects.create(title='Salário', type='income', value=8500.00, category=self.category_1)
        self.transaction_2 = Transaction.objects.create(title='Compras do mês', type='outcome', value=2500.00, category=self.category_2)
        self.client = APIClient()

    def test_get_transactions_list(self):
        response = self.client.get('/api/v1/transactions/all/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['transactions']), 2)
        self.assertEqual(response.data['total_income'], 8500.00)
        self.assertEqual(response.data['total_outcome'], 2500.00)
        self.assertEqual(response.data['total_balance'], 6000.00)


class TransactionAPIDeleteViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Alimentação")
        self.transaction = Transaction.objects.create(title="Compras do mês", type="outcome", value=500.00, category=self.category)
        self.client = APIClient()

    def test_delete_transaction(self):
        response = self.client.delete(f'/api/v1/transactions/{self.transaction.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verifica se a transação foi deletada
        with self.assertRaises(Transaction.DoesNotExist):
            self.transaction.refresh_from_db()


class TransactionAPISummaryViewTest(TestCase):

    def setUp(self):
        self.category_1 = Category.objects.create(title="Casa")
        self.category_2 = Category.objects.create(title="Alimentação")
        self.transaction_1 = Transaction.objects.create(title='Compras', type='outcome', value=200.00, category=self.category_2)
        self.transaction_2 = Transaction.objects.create(title='Aluguel', type='outcome', value=600.00, category=self.category_1)
        self.transaction_3 = Transaction.objects.create(title='Internet', type='outcome', value=100.00, category=self.category_1)
        self.client = APIClient()

    def test_get_transaction_summary(self):
        response = self.client.get('/api/v1/transaction-summary/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Casa', response.data)
        self.assertIn('Alimentação', response.data)
        self.assertEqual(response.data['Casa'], 700.00)
        self.assertEqual(response.data['Alimentação'], 200.00)
