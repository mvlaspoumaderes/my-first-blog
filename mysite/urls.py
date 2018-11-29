from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login_url'),
     path('logout/', LoginView.as_view(template_name='accounts/logout.html'), name='logout_url'),
    url(r'', include('blog.urls')),
]