from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet,IncomeCategoryViewSet, ExpensesCategoryViewSet,ExpensesViewSet






router = DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'incomecategory', IncomeCategoryViewSet)
router.register(r'expenses', ExpensesViewSet)
router.register(r'expensescategory', ExpensesCategoryViewSet)



urlpatterns = [
    path('', include(router.urls)),
    # path('fin_result',)

]
