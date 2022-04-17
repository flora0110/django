from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.showtemplate),
    path('create', views.vendor_create_view),
    path('<int:id>/', views.singleVendor, name='vendor'),
]
