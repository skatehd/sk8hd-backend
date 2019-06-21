"""sk8hd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from dates import views as dateViews
from users import views as userViews
from django.conf.urls.static import static

from rest_framework import routers
from django.conf import settings
from allauth.account.views import confirm_email, login, logout

router = routers.DefaultRouter()
router.register(r'events', dateViews.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #Event
    path('event/<int:pk>/', dateViews.EventDetailViewSet.as_view()),
    path('event/<int:pk>/comments/', dateViews.EventCommentCreateListViewSet.as_view()),
    
    path('users/<int:pk>/', userViews.UserDetailViewSet.as_view()),


    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    # path('', include('django.contrib.auth.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/logout/', logout, name='account_logout'),
    path('auth/registration/login/', login, name='account_login'),
    path('auth/registration/account-confirm-email/', confirm_email, name='account_email'),
    path('auth/registration/account-confirm-email/<str:key>/', confirm_email, name='account_confirm_email'),
    path('auth/registration/', include('rest_auth.registration.urls')),
]


# Serve media files in development
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)