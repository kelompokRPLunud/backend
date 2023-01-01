from django.forms import ModelForm
from .models import Usersnormal
from rest_framework import serializers
from django.contrib.auth.models import User

class Register(serializers.ModelSerializer):
    name=serializers.CharField(max_length=200)
    password=serializers.CharField(max_length=200)
    email=serializers.CharField(max_length=200)
    # class Meta:
    #     model=User
    #     fields=['username','password','email']
    # def create(self, validated_data):
    #     instance=self.Meta.model(**validated_data)
    #     instance.save()
    #     return instance
class Login(ModelForm):
    class Meta:
        model=Usersnormal
        fields=['name','password']
