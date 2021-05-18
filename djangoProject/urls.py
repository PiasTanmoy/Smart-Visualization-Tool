"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Visualization import views as viz_views
from django.conf import settings
from django.conf.urls.static import static

from Visualization import views as webAccess_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', viz_views.csv_data_read, name='csv_data_read'),
    path('smartScale2/',viz_views.smartScale, name='smartScale'),
    path('bar/',viz_views.bar, name='bar'),
    path('smartScale/',viz_views.smartScale, name='smartScale'),



    path('mobile/',viz_views.smartScale2, name='smartScale2'),
    path('prev',viz_views.dataSelection, name='dataSelection'),
    path('test/',viz_views.dataSelection2, name='dataSelection2'),
    path('test-single/',viz_views.dataSelection2single, name='dataSelection2single'),
    path('test-single-col/',viz_views.dataSelection2singleCol, name='dataSelection2singleCol'),
    path('logout/', viz_views.logout, name='logout'),

    path('', webAccess_views.getCredentials, name='credentials'),
    path('getdataset/', webAccess_views.getDataSet, name='getDataset'),
    path('dashboard/', webAccess_views.getDashboard, name='getDashboard'),
    path('testground/', webAccess_views.testGroud, name='testground')
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)