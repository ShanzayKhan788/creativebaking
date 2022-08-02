from django.urls import path, include
from .views import *
from . import views
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="About"),
    path('cakes/', Cakes.as_view(), name="Cake"),
    path('contact/', Message.as_view(), name="contact"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('blog_details/<id>', BlogDetailView.as_view(), name="blog"),
    path('custom/', CustomCake.as_view(), name="custom"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", views.logoutt , name="logout"),
    path("sign/", Registration.as_view(), name="SignUp"),
    path("forget-password/", forgetpassword.as_view(), name="Password"),
]