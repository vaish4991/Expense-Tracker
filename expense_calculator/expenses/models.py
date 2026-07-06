from django.db import models

class ExpenseCategory(models.Model):
    """
    Expense Category model
    """
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Expense Category"
        verbose_name_plural = "Expense Categories"
        ordering = ['name']


class Expense(models.Model):
    """
    Expense model
    """
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} - {self.amount}'