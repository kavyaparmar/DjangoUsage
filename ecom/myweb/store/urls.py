from django import views
from . import views
from django.urls import path

urlpatterns = [
    # path('products/' , views.products , name= 'products'),
    # path('products/', views.products, name='products'),
    # path('', views.home, name='home'),
    # path('',views.template_example, name='template_example'),
    path('', views.view_example,name='view_example'),
]
