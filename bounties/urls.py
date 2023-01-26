from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import CustomRegisterView, CustomLoginView, UserProfileView, UserProfileUpdateView
from .views import BountyListView, BountyCreateView, BountyUpdateView, BountyDeleteView
from .views import update_observe


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),

    path('', BountyListView.as_view(), name='bounties'),
    path('bounty-create/', BountyCreateView.as_view(), name='bounty-create'),
    path('bounty-update/<int:pk>/', BountyUpdateView.as_view(), name='bounty-update'),
    path('bounty-delete/<int:pk>/', BountyDeleteView.as_view(), name='bounty-delete'),

    path('update-observe/', update_observe, name='update-observe'),
    
    path('user-profile/<int:pk>/<str:category>/', UserProfileView.as_view(), name='user-profile'),
    path('user-profile-update/<int:pk>/', UserProfileUpdateView.as_view(), name='user-profile-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)