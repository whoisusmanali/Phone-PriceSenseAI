from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_price, name='predict_price'),
    path('predict/', views.predict_price, name='predict'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
]
