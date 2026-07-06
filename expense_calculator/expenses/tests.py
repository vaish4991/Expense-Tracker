#import for django_rest_framework tests
from rest_framework.test import APITestCase

from .models import Expense
"""
class ExpenseCategory(models.Model):
    Expense Category model
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Expense Category"
        verbose_name_plural = "Expense Categories"
        ordering = ['name']


class Expense(models.Model):
 
    Expense model

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} - {self.amount}'
"""

class ExpenseAPITestCase(APITestCase):
    def setUp(self):
            Expense.objects.bulk_create([
            Expense(name='Expense 1', amount=10.00, category_id=1),
            Expense(name='Expense 2', amount=20.00, category_id=2),
            Expense(name='Expense 3', amount=30.00, category_id=3),
        ])

    def test_expense_list(self):
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3) 

    def test_expense_create(self):
        response = self.client.post('/api/expenses/', {'name': 'Expense 4', 'amount': 40.00, 'category_id': 1})
        self.assertEqual(response.status_code, 201)

    def test_expense_update(self):
        expense = Expense.objects.first()
        response = self.client.put(f'/api/expenses/{expense.id}/', {'name': 'Updated Expense', 'amount': 50.00, 'category_id': 2})
        self.assertEqual(response.status_code, 200)
        expense.refresh_from_db()
        self.assertEqual(expense.name, 'Updated Expense')
        self.assertEqual(expense.amount, 50.00)
        self.assertEqual(expense.category_id, 2)

        def test_expense_delete(self):
            expense = Expense.objects.first()
            response = self.client.delete(f'/api/expenses/{expense.id}/')
            self.assertEqual(response.status_code, 204)
            self.assertFalse(Expense.objects.filter(id=expense.id).exists())    

            
                    
    def tearDown(self):
        Expense.objects.all().delete()
        