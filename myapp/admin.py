from django.contrib import admin
from .models import Income,IncomeCategory,ExpensesCategory,Expenses
# Register your models here.




@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id','name_income','category','amount','data_paid','description')
    list_display_links = ('id','name_income',)
    search_fields = ('id','name_income',)




@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name',)
    list_display_links = ('id','category_name',)
    search_fields = ('category_name',)




@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('id','name_expenses','category','amount','data_paid','description')
    list_display_links = ('id','name_expenses',)
    search_fields = ('id','name_expenses',)




@admin.register(ExpensesCategory)
class ExpensesCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name',)
    list_display_links = ('id','category_name',)
    search_fields = ('category_name',)


