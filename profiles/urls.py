from django.urls import path, include
from .views import ProfileList, ProfileDetail, LogoutView, home

urlpatterns = [
    path('', home, name='home'),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
