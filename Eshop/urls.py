"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from store import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('home/', views.Index.as_view(), name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),

    path('cart/', views.Cart.as_view(), name="cart"),
    
    path('orders/', views.orders, name="orders"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/<id>', views.payment, name="payment"),   

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)