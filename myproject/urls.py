from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.views import register, verify_email, welcome
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('teachers/', include('app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
    path('verify-email/<uuid:token>/', verify_email, name='verify_email'),
]