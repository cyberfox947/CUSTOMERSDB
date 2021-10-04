from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/search/', views.search_customer, name='search_customer'),
    path('customer/<int:customer_id>/', views.customer, name='customer'),
    path('customer/<int:customer_id>/update/', views.update_customer, name='update_customer'),
    path('customer/<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),
    path('customer/new/', views.new_customer, name='new_customer'),

# # # USER AUTHENTICATION

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
