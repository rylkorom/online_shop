from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_slug>/', views.index, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('all_products', views.all_products, name='all_products'),
    path('about', views.about_us, name='about'),
]
