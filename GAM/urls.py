"""GAM URL Configuration

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
from GAM_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('About_us/', views.About_us, name='About_us'),
    path('Classes_Taught/', views.Classes_Taught, name='Classes_Taught'),
    path('Add_Subscriber/', views.Add_Subscriber, name='Add_Subscriber'),
    path('Add_Queries/', views.Add_Queries, name='Add_Queries'),
    path('add_user_data/', views.add_user_data, name='add_user_data'),
    path('After_Login/', views.After_Login, name='After_Login'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_login1/', views.admin_login1, name='admin_login1'),
    path('admin_login1/enrolled/', views.enrolled, name='enrolled'),
    path('admin_login1/enrolled/update/<int:id>/', views.update, name='update'),
    path('admin_login1/enrolled/delete/<int:id>/', views.delete, name='delete'),
    path('admin_login1/queries/', views.queries, name='queries'),
    path('admin_login1/queries/delete/<int:id>/', views.query_delete, name='query_delete'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('add_admin/', views.add_admin, name='add_admin'),
    path('forgot_adminpass/', views.forgot_adminpass, name='forgot_adminpass'),
]
