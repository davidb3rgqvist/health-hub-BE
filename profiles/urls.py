from django.urls import path
from .views import ProfileList, ProfileDetail, LogoutView, home

urlpatterns = [
    path('', home, name='home'),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
