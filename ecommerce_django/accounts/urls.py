from django.urls import path, include
from ecommerce_django.accounts.views import SignInView, SignUpView, UserDetailsView, UserEditView, UserDeleteView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user')
    ]))
]
