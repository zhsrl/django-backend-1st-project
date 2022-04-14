from django.urls import path
from requests import request

from api import views

from .views import CategoriesView, ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:id>', ProductListView.get_single),
    path('categories', CategoriesView.as_view())

]
