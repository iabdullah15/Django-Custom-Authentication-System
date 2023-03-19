from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login_view'),
    path('logout/',
    auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html',
        next_page='/login'
    ),
    name = 'logout'
)
]