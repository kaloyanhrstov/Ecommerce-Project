from django.conf import settings
from django.urls import path, include
from .views import store, cart, checkout, update_item, process_order, about, index
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/', include('ecommerce_django.accounts.urls')),

    path('', index, name='index'),
    path('store/', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('about/', about, name='about'),

    path('update_item/', update_item, name='update_item'),
    path('process_order/', process_order, name='process_order'),
]
