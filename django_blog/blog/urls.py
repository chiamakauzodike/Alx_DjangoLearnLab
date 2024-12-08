from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView, ProfileView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    #path('profile/', profile_view, name='profile'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
]
