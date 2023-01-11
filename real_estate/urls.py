"""real_estate URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from listings.views import listing_list, listing_retrieve, listing_create, listing_update, listing_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', listing_list), # can create new urls here -> put listings/ and you can have this view in that URL
    path('listings/<pk>/', listing_retrieve), #pk = primary key -> id -> <pk> is a smart url 
    path('add-listing', listing_create),
    path('listings/<pk>/edit/', listing_update),
    path('listings/<pk>/delete/', listing_delete)
]


# configure that django should upload all files in media folder! 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

