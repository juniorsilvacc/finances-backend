import uuid
from django.db import models
from categories.models import Category


class Transaction(models.Model):
    INCOME = 'income'
    OUTCOME = 'outcome'

    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (OUTCOME, 'Outcome'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transactions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
