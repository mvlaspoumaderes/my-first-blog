from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from django.urls import path, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # new for Login/Logout,
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]