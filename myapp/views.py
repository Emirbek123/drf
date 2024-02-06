from django.shortcuts import render
from rest_framework import viewsets ,generics, response
from .models import Income, IncomeCategory,ExpensesCategory,Expenses
from .serializers import IncomeSerializer,IncomeCategorySerializer,ExpensesCategorySerializer,ExpensesSerializer
# Create your views here.


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeCategoryViewSet(viewsets.ModelViewSet):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer



class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer




class ExpensesCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpensesCategory.objects.all()
    serializer_class = ExpensesCategorySerializer


# class FinancialResultView(generics.GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         1
#         2
#         3
#         return response.Response({'success' : 'ok' })
    
