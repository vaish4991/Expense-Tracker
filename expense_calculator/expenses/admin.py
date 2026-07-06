from django.contrib import admin

from .models import Expense, ExpenseCategory 

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """
    Admin view for Expense model
    """
    list_display = ('name', 'amount', 'timestamp', 'category')
    list_filter = ('category', 'timestamp')
    search_fields = ('name', 'category__name')