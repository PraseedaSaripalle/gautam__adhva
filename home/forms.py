from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class createuserform(UserCreationForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name','mobile','email','degree']

class addQuestionform(ModelForm):
    class Meta:
        model = Questions
        #fields = ['question','op1','op2','op3','op4']
        fields = "__all__"
#class addAnswerform(ModelForm):
    #class Meta:
        #model= Answer
