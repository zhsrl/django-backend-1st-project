from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    path('', views.index),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>', ProductListView.get_by_id)

]
