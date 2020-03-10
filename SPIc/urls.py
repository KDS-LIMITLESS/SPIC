"""SPIc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blogV
from django.conf import settings
from django.conf.urls.static import static
from user import views as userV
from django.contrib.auth import views as authV


urlpatterns = [
    path('register/', userV.register, name='register'),
    path('login/', authV.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', authV.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('', blogV.index, name='index'),
    path('profile', userV.profile, name='profile'),
    path('admin/', admin.site.urls),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
