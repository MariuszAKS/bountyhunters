from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import CustomRegisterView, CustomLoginView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]