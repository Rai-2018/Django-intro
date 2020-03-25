"""djangointro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include

from pages.views import home_view
from product.views import product_forms


urlpatterns = [
	path('',home_view,name="home"),
    #can be slug type or any time you specify, the name in the tag has to match the one in the view
	# path("product/<int:my_id>/",dynamic_lookup_view,name = "product_detail"),
 #    path("product/<int:my_id>/delete",product_delete_view),
 #    path("product/list/",product_list_all),
    path("create/",product_forms),
	path('home/',home_view,name="home"),
    path('admin/', admin.site.urls),
    path("product/",include("product.urls"))
]
