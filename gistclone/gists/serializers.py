from re import S
from django.db.models.query import QuerySet
from rest_framework import serializers
from gists.models import Gist
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

class GistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    star_count = serializers.IntegerField(
        source='stars.count',
        read_only=True
    )
    class Meta:
        model = Gist
        fields=['url','id','name','description','code','owner','is_public','stars','star_count']  
        extra_kwargs = {'stars':{'read_only':True}}



class UserSerializer(serializers.ModelSerializer):
    gists = serializers.PrimaryKeyRelatedField(many=True, queryset= Gist.objects.all())

    class Meta:
        model=User
        fields = ['url','id','username','gists']

class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class GistStarSerializer(serializers.ModelSerializer):
    stars = UserRegisterSerializer(many=True, read_only=True) #stars in in Gists model with foreign key
    class Meta:
        model = Gist
        fields = ['stars',]