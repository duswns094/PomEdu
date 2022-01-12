from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

# from accountapp.views import AccountCreateView
from accountapp import views

app_name = "accountapp"

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),

]