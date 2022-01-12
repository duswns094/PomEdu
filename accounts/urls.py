from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

# from accountapp.views import AccountCreateView
from accounts import views
# from accounts.views import AccountCreateView

app_name = "accounts"

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.user_signup, name= 'register'),

]