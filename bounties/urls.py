from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import CustomRegisterView, CustomLoginView
from .views import BountyListView, BountyCreateView, BountyUpdateView, BountyDeleteView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),

    path('', BountyListView.as_view(), name='bounties'),
    path('bounty-create/', BountyCreateView.as_view(), name='bounty-create'),
    path('bounty-update/<int:pk>/', BountyUpdateView.as_view(), name='bounty-update'),
    path('bounty-delete/<int:pk>/', BountyDeleteView.as_view(), name='bounty-delete'),
]