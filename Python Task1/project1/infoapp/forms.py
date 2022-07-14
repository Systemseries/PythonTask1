from dataclasses import fields
from importlib.metadata import MetadataPathFinder
from django import forms
from .models import clientinfo,user2
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class clientform(forms.ModelForm):
    class Meta:
        model=clientinfo
        fields=['client_id','client_name','created_at','created_by']
        widgets={'client_id':forms.NumberInput(attrs={'class':'form-control'}),
                 'client_name':forms.TextInput(attrs={'class':'form-control'}),
                 'created_at':forms.DateTimeInput(attrs={'class':'form-control'}),
                 'created_by':forms.TextInput(attrs={'class':'form-control'}),
        }


class userform(forms.ModelForm):
    class Meta:
        model=user2
        fields=['user_id','user_name','project_name','created_at','created_by','updated_at']
        widgets={'user_id':forms.NumberInput(attrs={'class':'form-control'}),
                 'user_name':forms.TextInput(attrs={'class':'form-control'}),
                 'project_name':forms.TextInput(attrs={'class':'form-control'}),
                 'created_at':forms.DateTimeInput(attrs={'class':'form-control'}),
                 'created_by':forms.TextInput(attrs={'class':'form-control'}),
                 'updated_at':forms.DateTimeInput(attrs={'class':'form-control'}),
        }

class signupform(UserCreationForm):
     password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
     password2=forms.CharField(label='confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'})) 
     class Meta:
        model=User
        fields=['username','first_name','last_name','email'] 
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
 
