from rest_framework import serializers
from .models import Expense, ExpenseCategory


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name']


class ExpenseSerializer(serializers.ModelSerializer):
    category = ExpenseCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ExpenseCategory.objects.all(),
        write_only=True,
        source='category'
    )
    
    class Meta:
        model = Expense
        fields = ['id', 'name', 'amount', 'timestamp', 'category', 'category_id']
        read_only_fields = ['id', 'timestamp']
