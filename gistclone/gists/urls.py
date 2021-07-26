from django.conf.urls import url
from django.db.models import base
from django.urls import path
from gists import views
from rest_framework.urlpatterns import format_suffix_patterns
from gists import views
from gists.views import GistViewSet, StarListViewSet,UserViewSet,api_root
from rest_framework import renderers
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from gists import views
from gists.views import give_star_to_gist

router = DefaultRouter()
router.register(r'gists',views.GistViewSet)
#router.register(r'users', views.UserViewSet)   
router.register(r'mygists', views.GistOwnViewSet,basename='Gists')
router.register(r'listusersofstar', views.StarListViewSet, basename='liststar')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^givestar/(?P<gist_id>\d+)/$', give_star_to_gist,
    name='give_star_to_gist'), 
]