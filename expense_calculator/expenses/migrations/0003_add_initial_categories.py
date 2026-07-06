# Generated migration to add initial expense categories

from django.db import migrations

def add_initial_categories(apps, schema_editor):
    ExpenseCategory = apps.get_model('expenses', 'ExpenseCategory')
    categories = ['Food', 'Transportation', 'Entertainment', 'Others']
    for category_name in categories:
        ExpenseCategory.objects.get_or_create(name=category_name)

def remove_categories(apps, schema_editor):
    ExpenseCategory = apps.get_model('expenses', 'ExpenseCategory')
    ExpenseCategory.objects.filter(name__in=['Food', 'Transportation', 'Entertainment', 'Others']).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expensecategory_options'),
    ]

    operations = [
        migrations.RunPython(add_initial_categories, remove_categories),
    ]
