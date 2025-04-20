from django.urls import path
from . import views

from .views import send_otp_view, verify_otp_view, home_view

urlpatterns = [
    path('login/', send_otp_view, name='send_otp'),
    path('verify/', verify_otp_view, name='verify_otp'),
    path('home/', home_view, name='home'),
    path('verify/menu.html/', views.menu, name='menu'),
    path('verify/menu.html/contact.html', views.contact, name='contact'),
    path('verify/menu.html/cart_index.html', views.cart, name='cart'),
    path('verify/menu.html/index.html', home_view, name='home2'),
    path('verify/menu.html/menu.html', views.menu, name='home2'),
]
