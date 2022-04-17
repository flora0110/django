"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView
from .views import register
urlpatterns = [
    path('welcome/', include('welcome.urls')),  # 導向welcome的URLconf module
    # include : 將 weclome.urls 下的所有 url 前面都冠上 welcome/
    path('vendor/', include('vendor.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html')),
    path('register/', register, name='register'),
]
"""
# 只有兩行
from django.contrib import admin
from django.urls import path, include
from .views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomePage.as_view(), name='home'),
    ]
