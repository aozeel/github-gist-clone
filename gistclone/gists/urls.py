from django.urls import path
from gists import views
from rest_framework.urlpatterns import format_suffix_patterns
from gists import views
from gists.views import GistViewSet,UserViewSet,api_root
from rest_framework import renderers
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from gists import views

router = DefaultRouter()
router.register(r'gists',views.GistViewSet)
router.register(r'users', views.UserViewSet)  
#router.register(r'mygists', views.GistOwnViewSet)

urlpatterns = [
    path('', include(router.urls)),
]