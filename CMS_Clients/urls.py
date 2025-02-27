from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


# imports views for CMS_Clients
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('clients/', include('clients.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]