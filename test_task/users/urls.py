from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('login')), name='redirect-to-login-page'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('home/', views.HomeView.as_view(), name='home'),
]