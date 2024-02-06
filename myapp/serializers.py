from rest_framework import serializers
from .models import Income, IncomeCategory, ExpensesCategory,Expenses

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields  ='__all__'



class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields  ='__all__'



class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields  ='__all__'



class ExpensesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesCategory
        fields  ='__all__'
