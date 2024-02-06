from django.db import models

# Create your models here.
class IncomeCategory(models.Model):
    category_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.category_name
    
class Income(models.Model): 
    name_income = models.CharField(max_length = 200)
    category = models.ForeignKey(IncomeCategory, on_delete = models.CASCADE , related_name = 'категория')
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    data_paid = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name_income

class ExpensesCategory(models.Model):
    category_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.category_name



class Expenses(models.Model):
    name_expenses = models.CharField(max_length = 200)
    category = models.ForeignKey(ExpensesCategory, on_delete = models.CASCADE , related_name = 'категория')
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    data_paid = models.DateTimeField()
    description = models.TextField()


    def __str__(self):
        return f'{self.name_expenses} -{self.amount}'
    

