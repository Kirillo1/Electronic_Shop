from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views.views import RegisterView, UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('<int:pk>', UserProfileView.as_view(), name='user_profile'),
]
