"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from learning_spaces import api

from learning_spaces.views import home_view
from learning_spaces.views import login_view


router = routers.DefaultRouter()
router.register("reservation", api.reservationViewSet)
router.register("room", api.roomViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', TemplateView.as_view(template_name='home.html'), name='homeView'),
    url(r'^home/', home_view, name='home'),
    url(r'^login/', login_view, name='login'),
    path('learning_spaces/', include('learning_spaces.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

