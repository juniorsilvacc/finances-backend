from rest_framework import serializers
from transactions.models import Transaction
from categories.models import Category


class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Transaction
        fields = ['id', 'title', 'type', 'value', 'category', 'created_at', 'updated_at']

    def get_category(self, obj):
        if obj.category:
            return {
                'id': obj.category.id,
                'title': obj.category.title,
                'created_at': obj.category.created_at,
                'updated_at': obj.category.updated_at,
            }
        return None
