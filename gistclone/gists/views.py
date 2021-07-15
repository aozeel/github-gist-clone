import re
import rest_framework
from rest_framework import serializers
from gists.permissions import IsGistOwner, IsOwnerOrReadOnly
from gists.models import Gist
from gists.serializers import GistSerializer, UserRegisterSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import mixins
from django.views.decorators.csrf import csrf_exempt
from rest_framework.documentation import include_docs_urls,get_docs_view,get_schema_view,get_schemajs_view
# Create your views here.+

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'gists':reverse('gist-list', request=request, format=format),
        'mygists':reverse('my-gists', request=request, format=format),
        
    })

@api_view(['POST'])
def give_star_to_gist(request,gist_id):
    """
    This viewset allow user to give a star any gist

    Additionally we also provide an extra `highlight` action.
    """
    gist=generics.get_object_or_404(Gist.objects.all(), pk=gist_id)
    gist.stars.add(request.user)
    serializer_context = {
        'request': request
    }
    serializer = GistSerializer(gist,context=serializer_context)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserCreate(generics.CreateAPIView):
    """
    The action that allow users to register.
    .

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer 
    permission_classes = ()
    @csrf_exempt
    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @csrf_exempt
    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data)

class GistOwnViewSet(
    mixins.ListModelMixin,mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    Retrieve user's gists and be able to delete each
    .

    Additionally we also provide an extra `highlight` action.
    """
    #queryset = Gist.objects.all()
    serializer_class = GistSerializer
    permission_classes = [IsGistOwner,]

    def get_queryset(self):
         return  Gist.objects.filter(owner=self.request.user.id)


class GistViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    This viewset provides to see public gist, its details and also post new gists.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Gist.objects.filter(is_public=True)
    serializer_class = GistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)