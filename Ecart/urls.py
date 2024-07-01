"""
URL configuration for Ecart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from Store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', views.Home, name="home"),
    path('s1/', views.store, name="store1"),
    path('s2/', views.Home, name="store2"),
    path('s3/', views.Login, name="login1"),
    path('s4/', views.store, name="login2"),
    path('s5/', views.Cart, name="cart1"),
    path('s6/', views.store, name="cart2"),
    path('s7/', views.Checkout, name="check1"),
    path('s8/', views.Cart, name="check2"),
    path('update_item/', views.updateItem, name="update_item"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

