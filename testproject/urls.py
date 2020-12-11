"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from test2 import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('login/',views.login),
    path('register/',views.load_register),
    path('register_save/',views.Register),
    path('save_data/',views.save_datas),
    path('load_responsepage/',views.Load_Responsepage),
    path('sel_add_data/',views.check_data_fetch),
    path('update_data/',views.Update_data),
    path('delete_data/',views.Delete_data),
    path('logout/',views.Logout),
    path('admin_registration/',views.Admin_registration),
  
   

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate_account, name='activate'),
    

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,
                                                                         document_root=settings.MEDIA_ROOT)
