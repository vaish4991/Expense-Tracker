
from rest_framework.viewsets import ModelViewSet

from .serializers import ExpenseCategorySerializer, ExpenseSerializer
from .models import Expense, ExpenseCategory


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseCategoryViewSet(ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer