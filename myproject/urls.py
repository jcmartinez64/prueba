from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^webapp1/', include('webapp1.urls')),
    url(r'^admin/', admin.site.urls),
]
