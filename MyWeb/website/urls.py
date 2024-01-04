from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homePage'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('record/<int:pk>', views.customer_record, name='record')
]