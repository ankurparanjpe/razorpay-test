from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test_path/', views.test_path, name="test_path"),

    path('create_payment/', views.create_payment, name="create_payment"),
]
