from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['expenseId', 'title', 'description', 'category', 'amount', 'expenseDate', 'creationDate', 'currency', 'status']