from django.urls import path
from .views import  page_register
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
   
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", page_register, name="register"),
    path("logout/",LogoutView.as_view(),name="logout")

]