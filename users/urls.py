from django.urls import path
from .views import LoginInterfaceView, LogoutInterfaceView, SignupView

urlpatterns = [
    path('login/', LoginInterfaceView.as_view(), name='login'),
    path('logout/', LogoutInterfaceView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='register'),
]
