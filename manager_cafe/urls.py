"""
URL configuration for manager_cafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from orders import views

urlpatterns = [
	path('admin/', admin.site.urls),
	
	path('search_order/', views.search_order),
	path('view_orders/', views.view_orders),
	
	path('new_order/', views.new_order),
	path('edit_order/', views.edit_order),
	path('create_order/', views.create_order),
	path('delete_order/', views.delete_order),
	path('update_order/', views.update_order),
	
	path('calc_profit/', views.calc_profit),
	
	path('status_order_in_waiting/', views.status_order_in_waiting),
	path('status_order_complete/', views.status_order_complete),
	path('status_order_payment_ok/', views.status_order_payment_ok),

]
