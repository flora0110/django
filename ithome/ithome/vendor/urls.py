from django.contrib import admin
from django.urls import path
from . import views
from .views import VendorListView, VendorDetail, VendorCreateView, VendorUpdateView
app_name = 'vendor'
urlpatterns = [
    # path('', views.showtemplate, name='index'),
    # path('create', views.vendor_create_view, name='create'),
    path('<int:id>/', views.singleVendor, name='vendor_id'),
    path('', VendorListView.as_view(), name='index'),
    path('create/', VendorCreateView.as_view(), name='create'),
    path('<int:pk>/update/', VendorUpdateView.as_view(), name='update'),
    # path('<int:id>/', views.VendorDetail.as_view(), name='vendor_id'),
]
