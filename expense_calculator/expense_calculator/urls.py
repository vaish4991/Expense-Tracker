"""
URL configuration for expense_calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls import include
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
#create a router for expenses
from rest_framework.routers import DefaultRouter
from expenses import views

router = DefaultRouter()
router.register('expenses', views.ExpenseViewSet, basename='expense')
router.register('categories', views.ExpenseCategoryViewSet, basename='category')


@ensure_csrf_cookie
def home(request):
    return render(request, 'index.html')


urlpatterns = [
    path('', home, name='home'),
    #add api url 
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
admin.site.site_header = "Expense Calculator Admin"


   
